# Anti-Grammy-Scammy 💕🛡️

**AI Companion for Elderly Scam Prevention**

An AI-powered boyfriend/girlfriend companion for elderly people to help them avoid romance scams. This application uses the Swarms framework to create a personalized, caring AI companion that can generate messages, images, and voice content while protecting against scammers.

## 🎯 Purpose

Romance scams targeting the elderly are a serious problem. This app provides a safe, AI-powered companion that:
- Sends caring, personalized messages throughout the day
- Generates images and voice messages
- Can receive "gifts" to a user-controlled Cash App account (protecting the elderly from sending money to scammers)
- Provides genuine companionship without any malicious intent

## ✨ Features

- **🤖 AI-Powered Persona**: Customizable boyfriend/girlfriend with unique personality, interests, and backstory
- **📱 Scheduled Messages**: Configurable message frequency (morning, afternoon, evening)
- **📲 SMS/Text Messaging**: Send messages directly to phone numbers via Twilio
- **🎨 Image Generation**: AI-generated images (requires setup)
- **🎤 Voice Messages**: Text-to-speech capabilities for audio messages
- **💰 Payment Protection**: Redirect "gifts" to user's own Cash App (prevents money going to scammers)
- **⚙️ Highly Configurable**: Easy setup wizard and JSON configuration
- **🧠 Swarms Framework**: Powered by Swarms for advanced AI agent capabilities

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection
- (Optional) Twilio account for SMS/text messaging

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/ZackBradshaw/Anti-Grammy-Scammy.git
cd Anti-Grammy-Scammy
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. **Run the setup wizard**:
```bash
python anti_scammy.py --setup
```

## 🎮 Usage

### Initial Setup
Run the interactive setup wizard to configure your AI companion:
```bash
python anti_scammy.py --setup
```

This will guide you through:
- Creating a persona (name, age, personality, interests)
- Setting message schedules
- Enabling SMS/text messaging
- Enabling image/voice generation
- Configuring Cash App payment protection
- Adding API keys

### Running the Companion
Start the AI companion with scheduled messages:
```bash
python anti_scammy.py --run
```

The companion will send messages according to your configured schedule.

### Generate a Single Message
Get a message immediately without running the scheduler:
```bash
python anti_scammy.py --message
```

### Custom Configuration
Use a custom configuration file:
```bash
python anti_scammy.py --config my_config.json --run
```

### Test SMS Configuration
Test your SMS/text messaging setup:
```bash
python anti_scammy.py --test-sms
```

### Interactive Chat Mode
Test the conversational payment protection by chatting with your companion:
```bash
python anti_scammy.py --chat
```

In chat mode, you can:
- Have a natural conversation with the AI companion
- Test how it responds when you mention wanting or needing something
- See the payment protection in action
- Type 'quit' or 'exit' to end the conversation

**Example conversation:**
```
You: I really want to get a new sweater for the winter
AI: I'd be happy to help you get that! If you'd like, you could send me 
     the money via my Cash App $YourCashApp and I'll order it and have 
     it sent right to you as a gift!
```

## 📝 Configuration

The `config.json` file contains all settings:

```json
{
  "persona": {
    "name": "Alex",
    "age": 65,
    "gender": "neutral",
    "personality": "kind, caring, thoughtful, good listener",
    "interests": "gardening, reading, cooking, traveling",
    "backstory": "Retired teacher who loves spending time with family"
  },
  "schedule": {
    "morning_message": "08:00",
    "afternoon_message": "14:00",
    "evening_message": "19:00",
    "messages_per_day": 3
  },
  "content_settings": {
    "use_images": true,
    "use_voice": true,
    "image_frequency": "daily",
    "voice_frequency": "weekly"
  },
  "sms": {
    "enabled": false,
    "phone_number": "+1234567890",
    "send_via_sms": false
  },
  "payment": {
    "cashapp_tag": "$YourCashApp",
    "enabled": true
  }
}
```

## 🛡️ How It Protects Against Scams

1. **Genuine Companionship**: Provides real emotional support without manipulation
2. **No Requests for Personal Info**: Never asks for sensitive information
3. **Contextual Payment Protection**: Only mentions Cash App when the user mentions wanting or needing something, then offers to buy it and send it as a gift
4. **Consistent Persona**: Maintains a believable, caring personality
5. **No Red Flags**: Never exhibits typical scammer behaviors (urgency, secrecy, financial pressure)

### How Payment Protection Works

Unlike scammers who constantly ask for money, the AI companion:
- **NEVER randomly asks for money or gifts**
- **ONLY responds** when grandma mentions wanting or needing something
- **Offers to help** by having grandma send money to buy the item and ship it as a gift
- Money goes to **grandma's own Cash App** (or family's controlled account)
- Protects grandma from sending money to real scammers

## 🎨 Advanced Features

### SMS/Text Messaging
Send messages directly to a phone number using Twilio:

1. **Sign up for Twilio**: Visit https://www.twilio.com/ and create an account
2. **Get credentials**: Find your Account SID, Auth Token, and get a Twilio phone number
3. **Configure environment**: Add to your `.env` file:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   ```
4. **Enable in setup**: Run `python anti_scammy.py --setup` and enable SMS
5. **Test it**: Run `python anti_scammy.py --test-sms` to verify

Once configured, messages will be automatically sent via SMS when scheduled or generated.

### Image Generation
To enable image generation, you'll need to set up DALL-E or Stability AI:
```python
# Coming soon: Full image generation integration
```

### Voice Capabilities
Voice messages are generated using Google Text-to-Speech (gTTS):
```bash
# Voice files are saved in generated_voices/
```

### Control Net
For advanced image generation with pose control:
```python
# Coming soon: ControlNet integration for persona consistency
```

## 📊 Message Log

All messages are logged to `message_log.txt` with timestamps:
```
[2024-01-21 08:00:00]
Good morning! Hope you slept well...

[2024-01-21 14:00:00]
Just thinking about you...
```

## 🔧 Development

### Project Structure
```
Anti-Grammy-Scammy/
├── anti_scammy.py          # Main application
├── config.json             # User configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── generated_images/       # Generated image files
├── generated_voices/       # Generated voice files
├── personas/              # Agent state files
└── message_log.txt        # Message history
```

### Dependencies
- **swarms**: Core AI agent framework
- **openai**: GPT-4 integration
- **gTTS**: Text-to-speech generation
- **schedule**: Message scheduling
- **python-dotenv**: Environment management

## 🤝 Contributing

Contributions are welcome! This project aims to protect vulnerable elderly people from scams.

## ⚠️ Disclaimer

This tool is designed for protection and education. Always ensure:
- The elderly person understands this is an AI companion
- Family members are aware of this protective measure
- The Cash App account is controlled by the elderly person or their trusted family
- This is used as part of a broader education about online scams

## 📜 License

MIT License - see LICENSE file for details

## 🆘 Support

If you or someone you know is affected by romance scams:
- **FTC**: https://reportfraud.ftc.gov/
- **FBI IC3**: https://www.ic3.gov/
- **AARP Fraud Watch**: https://www.aarp.org/money/scams-fraud/

## 🙏 Acknowledgments

- Built with the [Swarms Framework](https://github.com/kyegomez/swarms)
- Inspired by the need to protect vulnerable populations from romance scams
- Thanks to all contributors working to make the internet safer for everyone
