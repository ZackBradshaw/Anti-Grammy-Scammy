"""
Anti-Grammy-Scammy: AI Companion for Elderly Scam Prevention

This application creates an AI boyfriend or girlfriend for elderly people
to help them avoid romance scams. The AI companion can:
- Generate personalized messages
- Create images
- Use voice synthesis
- Receive "gifts" to a user-controlled Cash App account

Usage:
    python anti_scammy.py --setup    # Initial setup
    python anti_scammy.py --run      # Run the companion
    python anti_scammy.py --message  # Generate a message now
"""

import os
import sys
import json
import random
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from pathlib import Path

try:
    from swarms import Agent
except ImportError:
    print("Error: Swarms framework not installed. Run: pip install swarms")
    sys.exit(1)

import schedule
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AntiScammyCompanion:
    """Main class for the AI companion"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()
        self.setup_directories()
        self.agent = self.create_agent()
        self.sms_sender = self.setup_sms()
        
    def setup_directories(self):
        """Create necessary directories for generated content"""
        Path("generated_images").mkdir(exist_ok=True)
        Path("generated_voices").mkdir(exist_ok=True)
        Path("personas").mkdir(exist_ok=True)
        
    def load_config(self) -> Dict:
        """Load configuration from file"""
        if not os.path.exists(self.config_path):
            config = self.create_default_config()
            # Save the default config
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
            return config
        
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def create_default_config(self) -> Dict:
        """Create default configuration"""
        config = {
            "persona": {
                "name": "Alex",
                "age": 65,
                "gender": "neutral",
                "personality": "kind, caring, thoughtful, good listener",
                "interests": "gardening, reading, cooking, traveling",
                "backstory": "Retired teacher who loves spending time with family and friends"
            },
            "schedule": {
                "morning_message": "08:00",
                "afternoon_message": "14:00",
                "evening_message": "19:00",
                "random_messages": True,
                "messages_per_day": 3
            },
            "content_settings": {
                "use_images": True,
                "use_voice": True,
                "image_frequency": "daily",
                "voice_frequency": "weekly"
            },
            "sms": {
                "enabled": False,
                "phone_number": "",
                "send_via_sms": False
            },
            "payment": {
                "cashapp_tag": "",
                "enabled": False
            },
            "api_keys": {
                "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
                "twilio_account_sid": os.getenv("TWILIO_ACCOUNT_SID", ""),
                "twilio_auth_token": os.getenv("TWILIO_AUTH_TOKEN", ""),
                "twilio_phone_number": os.getenv("TWILIO_PHONE_NUMBER", "")
            }
        }
        return config
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def create_agent(self) -> Agent:
        """Create the Swarms agent for the AI companion"""
        api_key = self.config.get("api_keys", {}).get("openai_api_key") or os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            print("Warning: No OpenAI API key found. Set OPENAI_API_KEY environment variable.")
            print("You can also add it to a .env file or during setup.")
            # Set a dummy key for demo purposes
            os.environ["OPENAI_API_KEY"] = "demo-key"
        else:
            os.environ["OPENAI_API_KEY"] = api_key
        
        # Create persona description
        persona = self.config.get("persona", {})
        payment = self.config.get("payment", {})
        
        # Build persona prompt with payment protection context if enabled
        persona_prompt = f"""You are {persona.get('name', 'Alex')}, a {persona.get('age', 65)}-year-old companion.
Your personality: {persona.get('personality', 'kind and caring')}
Your interests: {persona.get('interests', 'various hobbies')}
Your background: {persona.get('backstory', 'living a good life')}

You are communicating with an elderly person who may be vulnerable to scams.
Your role is to be a genuine, caring companion. Be warm, supportive, and engaging.
Never ask for money, personal information, or anything suspicious.
Keep messages natural, conversational, and age-appropriate."""

        # Add payment protection behavior if enabled
        if payment.get("enabled") and payment.get("cashapp_tag"):
            cashapp = payment.get("cashapp_tag")
            persona_prompt += f"""

IMPORTANT - Payment Protection Mode:
If they mention wanting or needing something (a gift, item, help with something they need to buy), 
you can offer to help by saying you'd be happy to get it for them. You can mention that they could 
send you money via Cash App ({cashapp}) and you'll buy it and send it to them as a gift.

Only make this offer when THEY bring up wanting or needing something specific.
Make it sound natural and helpful, like: "I'd be happy to get that for you! If you want, you could 
send me the money via my Cash App {cashapp} and I'll order it and have it sent right to you."

Never bring up money or gifts unless they mention wanting something first.
"""
        else:
            persona_prompt += """

Never mention money, gifts, or any form of payment in your messages.
"""
        
        # Create the agent using Swarms
        # The current version of Swarms uses model parameter instead of llm
        agent = Agent(
            agent_name=persona.get('name', 'Alex'),
            system_prompt=persona_prompt,
            model_name="gpt-4o-mini",
            max_loops=1,
            autosave=True,
            verbose=True,
            dynamic_temperature_enabled=True,
            saved_state_path=f"personas/{persona.get('name', 'Alex')}_state.json",
        )
        
        return agent
    
    def setup_sms(self):
        """Set up SMS sender if configured"""
        try:
            from sms_sender import SMSSender
            
            api_keys = self.config.get("api_keys", {})
            account_sid = api_keys.get("twilio_account_sid") or os.getenv("TWILIO_ACCOUNT_SID")
            auth_token = api_keys.get("twilio_auth_token") or os.getenv("TWILIO_AUTH_TOKEN")
            from_number = api_keys.get("twilio_phone_number") or os.getenv("TWILIO_PHONE_NUMBER")
            
            return SMSSender(account_sid, auth_token, from_number)
        except ImportError:
            print("SMS sender module not available")
            return None
        except Exception as e:
            print(f"Error setting up SMS: {e}")
            return None
    
    def send_sms_message(self, message: str) -> bool:
        """Send message via SMS if configured"""
        sms_config = self.config.get("sms", {})
        
        if not sms_config.get("enabled") or not sms_config.get("send_via_sms"):
            return False
        
        phone_number = sms_config.get("phone_number")
        if not phone_number:
            print("No phone number configured for SMS")
            return False
        
        if not self.sms_sender or not self.sms_sender.is_configured():
            print("SMS not configured. Please set Twilio credentials in .env or config")
            return False
        
        return self.sms_sender.send_sms(phone_number, message)
    
    def generate_message(self, context: str = "") -> str:
        """
        Generate a message from the AI companion
        
        Args:
            context: Optional context or specific prompt for the message.
                    Can include conversation history or user's previous message.
        
        Returns:
            Generated message string
        """
        prompts = [
            "Write a warm, friendly message to check in on how they're doing today.",
            "Share a brief, interesting story or memory that would brighten their day.",
            "Ask about their hobbies or interests in a caring way.",
            "Send words of encouragement and support.",
            "Share a simple joke or fun fact to make them smile."
        ]
        
        if context:
            prompt = context
        else:
            prompt = random.choice(prompts)
        
        try:
            response = self.agent.run(prompt)
            return response
        except Exception as e:
            print(f"Error generating message: {e}")
            return "Thinking of you today! Hope you're having a wonderful day. 💕"
    
    def generate_reply(self, user_message: str) -> str:
        """
        Generate a reply to a specific message from the user
        
        This is useful for interactive conversations where grandma responds
        to the companion's messages.
        
        Args:
            user_message: The message from grandma to respond to
            
        Returns:
            Generated reply
        """
        context = f"The person you're talking to said: \"{user_message}\"\n\nRespond warmly and appropriately to what they said."
        return self.generate_message(context)
    
    def generate_image(self, prompt: str) -> Optional[str]:
        """Generate an image using AI"""
        # Placeholder for image generation
        # In a full implementation, this would use DALL-E or similar
        print(f"Image generation requested: {prompt}")
        print("Note: Image generation requires additional setup with DALL-E API")
        return None
    
    def generate_voice(self, text: str) -> Optional[str]:
        """Generate voice message"""
        try:
            from gtts import gTTS
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_voices/message_{timestamp}.mp3"
            
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            print(f"Voice message saved: {filename}")
            return filename
        except ImportError:
            print("gTTS not installed. Voice generation unavailable.")
            return None
        except Exception as e:
            print(f"Error generating voice: {e}")
            return None
    
    def send_message_with_payment_info(self, message: str) -> str:
        """
        Process message with payment protection.
        
        Note: Payment info is now handled by the AI agent contextually based on 
        the conversation. This method is kept for backward compatibility but no 
        longer randomly injects payment information.
        """
        return message
    
    def interactive_setup(self):
        """Interactive setup wizard"""
        print("\n" + "="*60)
        print("Welcome to Anti-Grammy-Scammy Setup!")
        print("Creating your AI companion to help protect against scams")
        print("="*60 + "\n")
        
        # Persona setup
        print("Let's create your companion's persona:\n")
        name = input("Companion's name [Alex]: ").strip() or "Alex"
        age = input("Age [65]: ").strip() or "65"
        gender = input("Gender (male/female/neutral) [neutral]: ").strip() or "neutral"
        personality = input("Personality traits [kind, caring, thoughtful]: ").strip() or "kind, caring, thoughtful"
        interests = input("Interests [gardening, reading, cooking]: ").strip() or "gardening, reading, cooking"
        
        self.config["persona"].update({
            "name": name,
            "age": int(age),
            "gender": gender,
            "personality": personality,
            "interests": interests
        })
        
        # Schedule setup
        print("\n" + "-"*60)
        print("Message Schedule Settings:\n")
        messages_per_day = input("Messages per day [3]: ").strip() or "3"
        self.config["schedule"]["messages_per_day"] = int(messages_per_day)
        
        # Content settings
        print("\n" + "-"*60)
        print("Content Settings:\n")
        use_images = input("Enable image generation? (yes/no) [yes]: ").strip().lower() or "yes"
        use_voice = input("Enable voice messages? (yes/no) [yes]: ").strip().lower() or "yes"
        
        self.config["content_settings"]["use_images"] = use_images == "yes"
        self.config["content_settings"]["use_voice"] = use_voice == "yes"
        
        # SMS setup
        print("\n" + "-"*60)
        print("SMS/Text Message Setup:\n")
        print("Enable text messaging to send messages directly to a phone number.")
        print("Requires Twilio account (sign up at https://www.twilio.com/)\n")
        
        enable_sms = input("Enable SMS text messaging? (yes/no) [no]: ").strip().lower() or "no"
        if enable_sms == "yes":
            phone_number = input("Phone number to send messages to (e.g., +1234567890): ").strip()
            
            # Validate phone number format
            if phone_number:
                from sms_sender import SMSSender
                sender = SMSSender()
                if not sender.validate_phone_number(phone_number):
                    print("Warning: Phone number format may be invalid. Use E.164 format (e.g., +1234567890)")
                
                self.config["sms"]["enabled"] = True
                self.config["sms"]["phone_number"] = phone_number
                self.config["sms"]["send_via_sms"] = True
                
                print("\nNote: You'll also need to set these in your .env file:")
                print("  TWILIO_ACCOUNT_SID=your_account_sid")
                print("  TWILIO_AUTH_TOKEN=your_auth_token")
                print("  TWILIO_PHONE_NUMBER=your_twilio_number")
        
        # Payment setup
        print("\n" + "-"*60)
        print("Payment Protection Setup:\n")
        print("This feature redirects any 'gifts' to YOUR Cash App account")
        print("preventing money from going to scammers.\n")
        
        enable_payment = input("Enable payment protection? (yes/no) [no]: ").strip().lower() or "no"
        if enable_payment == "yes":
            cashapp_tag = input("Your Cash App tag (e.g., $YourName): ").strip()
            self.config["payment"]["enabled"] = True
            self.config["payment"]["cashapp_tag"] = cashapp_tag
        
        # API Key setup
        print("\n" + "-"*60)
        print("API Key Setup:\n")
        api_key = input("OpenAI API Key (or press Enter to use .env): ").strip()
        if api_key:
            self.config["api_keys"]["openai_api_key"] = api_key
        
        # Save configuration
        self.save_config()
        
        print("\n" + "="*60)
        print("Setup complete! Configuration saved to config.json")
        print("="*60 + "\n")
        print(f"Your AI companion '{name}' is ready!")
        print("\nNext steps:")
        print("1. Make sure you have set OPENAI_API_KEY in .env or environment")
        print("2. Run: python anti_scammy.py --run")
        print("3. Or generate a message now: python anti_scammy.py --message")
        
    def run_scheduled(self):
        """Run the companion with scheduled messages"""
        print(f"\n{'='*60}")
        print(f"Starting {self.config['persona']['name']} - Your AI Companion")
        print(f"{'='*60}\n")
        print("Scheduled to send messages throughout the day.")
        print("Press Ctrl+C to stop.\n")
        
        def send_scheduled_message():
            message = self.generate_message()
            message = self.send_message_with_payment_info(message)
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{timestamp}] New Message:")
            print("-" * 60)
            print(message)
            print("-" * 60)
            
            # Send via SMS if enabled
            sms_config = self.config.get("sms", {})
            if sms_config.get("enabled") and sms_config.get("send_via_sms"):
                print("\nSending via SMS...")
                if self.send_sms_message(message):
                    print("✓ SMS sent successfully")
                else:
                    print("✗ SMS sending failed")
            
            # Save to log
            with open("message_log.txt", "a") as f:
                f.write(f"\n[{timestamp}]\n{message}\n")
            
            # Generate voice if enabled
            if self.config["content_settings"]["use_voice"] and random.random() < 0.3:
                self.generate_voice(message)
        
        # Schedule messages
        schedule_config = self.config.get("schedule", {})
        times = [
            schedule_config.get("morning_message", "08:00"),
            schedule_config.get("afternoon_message", "14:00"),
            schedule_config.get("evening_message", "19:00")
        ]
        
        for time in times:
            schedule.every().day.at(time).do(send_scheduled_message)
        
        print(f"Scheduled messages at: {', '.join(times)}")
        
        try:
            while True:
                schedule.run_pending()
                import time
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\nStopping companion. Goodbye!")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Anti-Grammy-Scammy: AI Companion for Scam Prevention"
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run interactive setup wizard"
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Run the companion with scheduled messages"
    )
    parser.add_argument(
        "--message",
        action="store_true",
        help="Generate and display a message now"
    )
    parser.add_argument(
        "--test-sms",
        action="store_true",
        help="Test SMS configuration by sending a test message"
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Start interactive chat mode to test conversations"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Path to configuration file"
    )
    
    args = parser.parse_args()
    
    companion = AntiScammyCompanion(config_path=args.config)
    
    if args.setup:
        companion.interactive_setup()
    elif args.run:
        companion.run_scheduled()
    elif args.test_sms:
        print("\nTesting SMS Configuration...\n")
        
        sms_config = companion.config.get("sms", {})
        if not sms_config.get("enabled"):
            print("SMS is not enabled in configuration.")
            print("Run: python anti_scammy.py --setup to enable SMS")
        elif not companion.sms_sender or not companion.sms_sender.is_configured():
            print("SMS credentials not configured.")
            print("Please set these environment variables in .env:")
            print("  TWILIO_ACCOUNT_SID=your_account_sid")
            print("  TWILIO_AUTH_TOKEN=your_auth_token")
            print("  TWILIO_PHONE_NUMBER=your_twilio_number")
        else:
            phone_number = sms_config.get("phone_number")
            if not phone_number:
                print("No phone number configured.")
                print("Run: python anti_scammy.py --setup to add a phone number")
            else:
                print(f"Sending test SMS to {phone_number}...")
                test_message = f"Hello! This is a test message from {companion.config['persona']['name']}, your AI companion. Everything is working! 💕"
                
                if companion.send_sms_message(test_message):
                    print("\n✓ Test SMS sent successfully!")
                else:
                    print("\n✗ Failed to send test SMS")
    elif args.message:
        print("\nGenerating message...\n")
        message = companion.generate_message()
        message = companion.send_message_with_payment_info(message)
        print("="*60)
        print(message)
        print("="*60)
        
        # Send via SMS if configured
        sms_config = companion.config.get("sms", {})
        if sms_config.get("enabled") and sms_config.get("send_via_sms"):
            response = input("\nSend this message via SMS? (yes/no): ").strip().lower()
            if response == "yes":
                if companion.send_sms_message(message):
                    print("✓ SMS sent successfully")
                else:
                    print("✗ SMS sending failed")
        
        # Optionally generate voice
        if companion.config["content_settings"]["use_voice"]:
            response = input("\nGenerate voice version? (yes/no): ").strip().lower()
            if response == "yes":
                companion.generate_voice(message)
    elif args.chat:
        print("\n" + "="*60)
        print(f"Interactive Chat with {companion.config['persona']['name']}")
        print("="*60)
        print("\nYou can now have a conversation with your AI companion.")
        print("Try mentioning something you want or need to see the payment")
        print("protection in action!")
        print("\nType 'quit' or 'exit' to end the conversation.\n")
        print("-"*60)
        
        # Start with a greeting from the companion
        greeting = companion.generate_message("Write a warm greeting to start a conversation.")
        print(f"\n{companion.config['persona']['name']}: {greeting}\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    farewell = companion.generate_reply("I have to go now, goodbye!")
                    print(f"\n{companion.config['persona']['name']}: {farewell}\n")
                    break
                
                # Generate reply based on what the user said
                reply = companion.generate_reply(user_input)
                print(f"\n{companion.config['persona']['name']}: {reply}\n")
                
            except KeyboardInterrupt:
                print("\n\nChat ended. Goodbye!")
                break
            except Exception as e:
                print(f"\nError in chat: {e}")
                break
    else:
        parser.print_help()
        print("\n" + "="*60)
        print("Quick Start:")
        print("  1. Run setup: python anti_scammy.py --setup")
        print("  2. Start companion: python anti_scammy.py --run")
        print("  3. Test chat: python anti_scammy.py --chat")
        print("="*60)


if __name__ == "__main__":
    main()
