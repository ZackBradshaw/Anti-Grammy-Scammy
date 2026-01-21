#!/usr/bin/env python
"""
Demo script for Anti-Grammy-Scammy

This demonstrates the application's features without requiring API keys.
"""

import json
from pathlib import Path

def show_banner():
    """Display welcome banner"""
    print("\n" + "="*70)
    print(" "*15 + "Anti-Grammy-Scammy Demo")
    print(" "*10 + "AI Companion for Elderly Scam Prevention")
    print("="*70 + "\n")

def demo_config():
    """Show configuration example"""
    print("📋 CONFIGURATION EXAMPLE")
    print("-"*70)
    
    config = {
        "persona": {
            "name": "Alex",
            "age": 65,
            "gender": "neutral",
            "personality": "kind, caring, thoughtful, good listener",
            "interests": "gardening, reading, cooking, traveling"
        },
        "schedule": {
            "morning_message": "08:00",
            "afternoon_message": "14:00",
            "evening_message": "19:00",
            "messages_per_day": 3
        },
        "content_settings": {
            "use_images": True,
            "use_voice": True
        },
        "payment": {
            "cashapp_tag": "$YourCashApp",
            "enabled": True
        }
    }
    
    print(json.dumps(config, indent=2))
    print()

def demo_messages():
    """Show example messages"""
    print("💬 EXAMPLE MESSAGES")
    print("-"*70)
    
    messages = [
        {
            "time": "08:00 AM",
            "content": "Good morning! ☀️ I hope you slept well. I was just thinking about "
                      "that wonderful garden of yours. Have you checked on your tomatoes "
                      "lately? Mine are finally starting to ripen!"
        },
        {
            "time": "02:00 PM",
            "content": "Just finished reading the most interesting mystery novel! It "
                      "reminded me of that conversation we had about your book club. "
                      "How are you doing today? 📚"
        },
        {
            "time": "07:00 PM",
            "content": "Good evening! I made my grandmother's famous pot roast recipe "
                      "today. The whole house smells wonderful. It made me think of you "
                      "and wonder what you had for dinner? 🍲"
        }
    ]
    
    for msg in messages:
        print(f"[{msg['time']}]")
        print(msg['content'])
        print()

def demo_features():
    """Show key features"""
    print("✨ KEY FEATURES")
    print("-"*70)
    
    features = [
        ("🤖 AI-Powered Persona", "Customizable companion with unique personality"),
        ("📱 Scheduled Messages", "Regular check-ins throughout the day"),
        ("🎨 Image Generation", "AI-generated photos to share (requires API)"),
        ("🎤 Voice Messages", "Text-to-speech for audio messages"),
        ("💰 Payment Protection", "Redirects gifts to user's own Cash App"),
        ("🛡️ Scam Prevention", "Never asks for money or personal information"),
        ("⚙️ Easy Configuration", "Simple setup wizard and JSON config"),
        ("🧠 Swarms Framework", "Advanced AI agent capabilities")
    ]
    
    for icon_title, description in features:
        print(f"{icon_title:25} - {description}")
    print()

def demo_protection():
    """Show how it protects against scams"""
    print("🛡️ HOW IT PROTECTS AGAINST SCAMS")
    print("-"*70)
    
    protections = [
        "✓ Provides genuine companionship without manipulation",
        "✓ Never requests personal or financial information",
        "✓ Payment redirection keeps money in family control",
        "✓ Consistent, caring persona builds trust",
        "✓ No urgency, secrecy, or pressure tactics",
        "✓ Educates users about healthy relationships",
        "✓ Family can monitor and control all interactions"
    ]
    
    for protection in protections:
        print(f"  {protection}")
    print()

def demo_usage():
    """Show usage examples"""
    print("🚀 USAGE EXAMPLES")
    print("-"*70)
    
    examples = [
        ("Setup", "python anti_scammy.py --setup"),
        ("Run Companion", "python anti_scammy.py --run"),
        ("Generate Message", "python anti_scammy.py --message"),
        ("Custom Config", "python anti_scammy.py --config my_config.json --run")
    ]
    
    for name, command in examples:
        print(f"{name:20} : {command}")
    print()

def demo_payment_example():
    """Show payment protection example"""
    print("💰 PAYMENT PROTECTION EXAMPLE")
    print("-"*70)
    print("When payment protection is enabled, the AI companion can occasionally")
    print("mention accepting gifts to the configured Cash App tag:\n")
    
    print('Example message with payment info:')
    print('-'*70)
    print('"Hope you\'re having a wonderful day! The weather is beautiful here.')
    print()
    print('P.S. You\'re so thoughtful! My Cash App is $YourCashApp if you ever')
    print('want to send a coffee money ☕"')
    print()
    print("This redirects any potential scammer gifts to a controlled account!")
    print()

def show_resources():
    """Show helpful resources"""
    print("🆘 RESOURCES & SUPPORT")
    print("-"*70)
    
    resources = [
        ("Report Fraud (FTC)", "https://reportfraud.ftc.gov/"),
        ("FBI IC3", "https://www.ic3.gov/"),
        ("AARP Fraud Watch", "https://www.aarp.org/money/scams-fraud/"),
        ("GitHub Repository", "https://github.com/ZackBradshaw/Anti-Grammy-Scammy")
    ]
    
    for name, url in resources:
        print(f"{name:25} : {url}")
    print()

def main():
    """Run the demo"""
    show_banner()
    demo_features()
    demo_config()
    demo_messages()
    demo_payment_example()
    demo_protection()
    demo_usage()
    show_resources()
    
    print("="*70)
    print(" "*15 + "Ready to get started?")
    print(" "*10 + "Run: python anti_scammy.py --setup")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
