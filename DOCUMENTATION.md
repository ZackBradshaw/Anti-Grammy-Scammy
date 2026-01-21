# Anti-Grammy-Scammy: Complete Project Documentation

## 📚 Documentation Index

This project includes multiple documentation files for different needs:

### For First-Time Users
- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[demo.py](demo.py)** - Run to see feature examples without API keys
- **[interactive_demo.py](interactive_demo.py)** - Interactive walkthrough of features

### For All Users
- **[README.md](README.md)** - Complete overview, features, and basic usage
- **[config.example.json](config.example.json)** - Example configuration file

### For Advanced Users
- **[ADVANCED.md](ADVANCED.md)** - Advanced configuration, integrations, and customization

### For Developers
- **[test_anti_scammy.py](test_anti_scammy.py)** - Test suite
- **[content_generator.py](content_generator.py)** - Image and voice generation module

## 🎯 Project Overview

### What Is This?

Anti-Grammy-Scammy is an AI-powered companion application designed to protect elderly people from romance scams. It creates a safe, caring AI boyfriend or girlfriend that:

1. **Provides Genuine Companionship** - Regular caring messages throughout the day
2. **Protects Against Scams** - Never asks for personal info or exhibits scammer behavior  
3. **Redirects Gift Money** - Optional Cash App integration sends money to user's own account
4. **Uses Advanced AI** - Powered by the Swarms framework and GPT-4

### Why Was This Built?

Romance scams targeting the elderly are a serious problem:
- Over $1 billion lost to romance scams in 2022 (FTC)
- Elderly are prime targets due to loneliness and trusting nature
- Scammers build fake relationships over weeks/months
- Victims often ashamed to report or get help

This app provides a protective alternative - a genuine AI companion that gives emotional support without any malicious intent.

## 🏗️ Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Anti-Grammy-Scammy                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌────────────────┐    ┌──────────────────┐               │
│  │  Configuration │───▶│ Persona System   │               │
│  │  Management    │    │ (Swarms Agent)   │               │
│  └────────────────┘    └──────────────────┘               │
│           │                      │                          │
│           ▼                      ▼                          │
│  ┌────────────────┐    ┌──────────────────┐               │
│  │   Scheduler    │───▶│ Message Generator│               │
│  │   (schedule)   │    │ (GPT-4 via       │               │
│  └────────────────┘    │  Swarms)         │               │
│           │             └──────────────────┘               │
│           │                      │                          │
│           ▼                      ▼                          │
│  ┌────────────────────────────────────────┐               │
│  │        Content Generation              │               │
│  │  ┌──────────┐ ┌──────────┐ ┌────────┐ │               │
│  │  │  Text    │ │  Images  │ │ Voice  │ │               │
│  │  │ Messages │ │ (DALL-E) │ │ (gTTS) │ │               │
│  │  └──────────┘ └──────────┘ └────────┘ │               │
│  └────────────────────────────────────────┘               │
│           │                                                 │
│           ▼                                                 │
│  ┌────────────────┐                                        │
│  │ Output Manager │                                        │
│  │ - Console      │                                        │
│  │ - Log file     │                                        │
│  │ - Voice files  │                                        │
│  │ - Image files  │                                        │
│  └────────────────┘                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **Python 3.8+** - Core language
- **Swarms Framework** - AI agent orchestration
- **OpenAI GPT-4** - Natural language generation
- **gTTS / pyttsx3** - Text-to-speech
- **schedule** - Message scheduling
- **Pillow** - Image processing (for future features)
- **python-dotenv** - Environment management

### File Structure

```
Anti-Grammy-Scammy/
├── README.md                    # Main documentation
├── QUICKSTART.md               # Quick start guide
├── ADVANCED.md                 # Advanced usage guide
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignore rules
│
├── anti_scammy.py             # Main application
├── content_generator.py       # Image/voice generation
├── config.example.json        # Example configuration
│
├── demo.py                    # Feature demonstration
├── interactive_demo.py        # Interactive walkthrough
├── test_anti_scammy.py       # Test suite
│
└── [Runtime Directories]
    ├── generated_images/      # AI-generated images
    ├── generated_voices/      # Voice message files
    ├── personas/             # Agent state files
    └── config.json           # User configuration (created by user)
```

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/ZackBradshaw/Anti-Grammy-Scammy.git
cd Anti-Grammy-Scammy
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 3. Setup

```bash
python anti_scammy.py --setup
```

### 4. Use

```bash
# Generate a single message
python anti_scammy.py --message

# Run with scheduled messages
python anti_scammy.py --run
```

## 🎨 Key Features

### 1. Customizable Persona

Create any type of companion:
- Name, age, gender
- Personality traits
- Interests and hobbies
- Background story
- Communication style

### 2. Smart Messaging

- **Scheduled**: Set specific times (morning, afternoon, evening)
- **Random**: Natural variation in timing
- **Contextual**: Messages consider time of day and previous conversations
- **Engaging**: Asks questions, shares stories, shows genuine interest

### 3. Content Generation

- **Text**: Natural, conversational messages
- **Images**: AI-generated photos (gardens, sunsets, etc.)
- **Voice**: Audio messages for more personal touch

### 4. Payment Protection

The killer feature:
- Companion occasionally mentions accepting "gifts"
- Payment info points to user's own Cash App account
- Money stays in family control
- Prevents funds going to real scammers

### 5. Safety Features

- Never asks for personal information
- No urgency or pressure tactics
- Consistent personality (not erratic like scammers)
- Family can monitor all activity
- All data stored locally

## 📊 Usage Scenarios

### Scenario 1: Basic Protection

**Goal**: Provide companionship, no payment features

```json
{
  "persona": { "name": "Alex", "personality": "kind, caring" },
  "schedule": { "messages_per_day": 2 },
  "payment": { "enabled": false }
}
```

### Scenario 2: Full Protection

**Goal**: Maximum scam protection with payment redirection

```json
{
  "persona": { "name": "Robert", "personality": "protective, wise" },
  "schedule": { "messages_per_day": 3 },
  "payment": { "enabled": true, "cashapp_tag": "$FamilyAccount" },
  "content_settings": { "use_images": true, "use_voice": true }
}
```

### Scenario 3: Multiple Personas

**Goal**: Different companions for different moods

```bash
# Morning companion - energetic and upbeat
python anti_scammy.py --config morning_alex.json --message

# Evening companion - calm and reflective
python anti_scammy.py --config evening_margaret.json --message
```

## 🛡️ Security & Privacy

### What Gets Stored

- **Locally**: Configuration, message logs, generated files
- **In Memory**: Current conversation context
- **Sent to OpenAI**: Message prompts only (no personal data)
- **Not Stored**: No user personal information, no financial data

### Best Practices

1. **API Keys**: Never commit to git, use .env files
2. **Cash App**: Use dedicated account, monitor regularly
3. **Family Oversight**: Share access with trusted family members
4. **Regular Reviews**: Check message logs periodically
5. **Education**: Ensure user understands this is AI

## 🧪 Testing

### Run Tests

```bash
python test_anti_scammy.py
```

### What Gets Tested

- Configuration creation and persistence
- Directory structure setup
- Agent initialization
- Message generation
- Payment info handling

### Test Coverage

- Core functionality: ✓
- Configuration management: ✓
- Agent creation: ✓
- File operations: ✓
- Error handling: ✓

## 🔧 Development

### Adding New Features

1. **New Persona Type**: Edit `create_agent()` in `anti_scammy.py`
2. **New Message Style**: Add templates to `generate_message()`
3. **New Content Type**: Extend `content_generator.py`
4. **New Integration**: See ADVANCED.md for examples

### Contributing

See main repository for contribution guidelines. Areas welcome:
- ControlNet integration for consistent persona images
- Multi-language support
- Mobile app interface
- More sophisticated conversation memory
- Integration with messaging platforms

## 📈 Future Enhancements

### Planned Features

- [ ] ControlNet for consistent persona appearance in images
- [ ] Voice cloning for consistent audio persona
- [ ] Web dashboard for family monitoring
- [ ] Mobile app (iOS/Android)
- [ ] Multi-language support
- [ ] SMS/WhatsApp integration
- [ ] Conversation memory and learning
- [ ] Scam detection and alerts
- [ ] Family notification system
- [ ] Analytics and usage reports

### Community Ideas

Have an idea? Open an issue on GitHub!

## 🆘 Support Resources

### For Scam Victims

- **FTC Report Fraud**: https://reportfraud.ftc.gov/
- **FBI Internet Crime Complaint Center**: https://www.ic3.gov/
- **AARP Fraud Watch**: https://www.aarp.org/money/scams-fraud/
- **Eldercare Locator**: 1-800-677-1116

### For This Project

- **GitHub Issues**: Report bugs or request features
- **Documentation**: See README.md, QUICKSTART.md, ADVANCED.md
- **Demos**: Run `python demo.py` or `python interactive_demo.py`

## 📜 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- **Swarms Framework**: https://github.com/kyegomez/swarms
- **OpenAI**: For GPT-4 API
- **The Community**: For fighting against scams targeting vulnerable populations

## 🎯 Mission Statement

**Our mission is to protect vulnerable elderly people from romance scams while providing genuine companionship and maintaining their dignity and independence.**

This tool is part of a broader strategy that should include:
- Family communication and support
- Education about online scams
- Regular check-ins and oversight
- Professional help when needed

The goal is not to replace human connection, but to provide a safe alternative to malicious actors who seek to exploit loneliness and trust.

---

**Remember**: This is a protective tool. Always ensure:
- The elderly person understands this is an AI companion
- Family members are aware and monitoring
- Payment accounts are controlled by family
- This is used alongside scam education
- Human connections remain the priority

---

Built with ❤️ to protect our elderly community from scams.

For more information, visit: https://github.com/ZackBradshaw/Anti-Grammy-Scammy
