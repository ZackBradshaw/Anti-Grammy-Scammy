# Quick Start Guide

Get Anti-Grammy-Scammy up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/)
- (Optional) Twilio account for SMS/text messaging
- 5 minutes of your time

## Installation

### Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/ZackBradshaw/Anti-Grammy-Scammy.git
cd Anti-Grammy-Scammy

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Set Up API Key

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-key-here
```

**Optional - For SMS/Text Messaging:**
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

### Step 3: Run Setup Wizard

```bash
python anti_scammy.py --setup
```

Follow the prompts to configure:
- Your companion's name and personality
- Message schedule
- SMS/text messaging (optional)
- Cash App payment protection (optional)

## Quick Examples

### Generate a Single Message

```bash
python anti_scammy.py --message
```

Example output:
```
============================================================
Good morning! ☀️ I hope you're having a wonderful day. 
I was just thinking about you and wanted to check in. 
How's your garden doing? Mine is finally blooming!
============================================================
```

### Run Scheduled Messages

```bash
python anti_scammy.py --run
```

This will send messages at your configured times (e.g., morning, afternoon, evening).

Press `Ctrl+C` to stop.

### Test SMS Setup

If you enabled SMS, test it:

```bash
python anti_scammy.py --test-sms
```

This sends a test message to verify your Twilio configuration.

## See It In Action

### Demo Mode

Want to see what it can do without setting up API keys?

```bash
python demo.py
```

This shows:
- Example messages
- Features overview
- Configuration examples
- How payment protection works

## Understanding the Config

After setup, you'll have a `config.json` file. Here's what it looks like:

```json
{
  "persona": {
    "name": "Alex",
    "personality": "kind, caring, thoughtful"
  },
  "schedule": {
    "morning_message": "08:00",
    "evening_message": "19:00"
  },
  "sms": {
    "enabled": true,
    "phone_number": "+1234567890",
    "send_via_sms": true
  },
  "payment": {
    "cashapp_tag": "$YourCashApp",
    "enabled": true
  }
}
```

You can edit this file directly to customize behavior.

## Common Use Cases

### Use Case 1: Basic Companion

Just want regular check-in messages:

```bash
python anti_scammy.py --setup
# Choose 2-3 messages per day
# Disable payment protection
python anti_scammy.py --run
```

### Use Case 2: Full Protection Mode

Want payment redirection for maximum scam protection:

```bash
python anti_scammy.py --setup
# Enable payment protection
# Add your Cash App tag
# Enable images and voice
python anti_scammy.py --run
```

### Use Case 3: On-Demand Messages

Just generate messages when needed:

```bash
# Morning check-in
python anti_scammy.py --message

# Afternoon update  
python anti_scammy.py --message

# Evening chat
python anti_scammy.py --message
```

## Customizing Your Companion

### Male Persona Example

Edit `config.json`:

```json
{
  "persona": {
    "name": "Robert",
    "age": 68,
    "gender": "male",
    "personality": "warm, protective, wise, good listener",
    "interests": "woodworking, classic cars, fishing, history",
    "backstory": "Retired police officer who now enjoys working on his classic Mustang"
  }
}
```

### Female Persona Example

```json
{
  "persona": {
    "name": "Margaret",
    "age": 63,
    "gender": "female",
    "personality": "nurturing, cheerful, creative, loves to share stories",
    "interests": "baking, quilting, gardening, romance novels",
    "backstory": "Retired nurse who loves baking cookies for the neighborhood"
  }
}
```

## Testing Your Setup

Run the test suite:

```bash
python test_anti_scammy.py
```

Expected output:
```
======================================================================
                    Running Anti-Grammy-Scammy Tests
======================================================================

✓ Configuration creation test passed
✓ Configuration save/load test passed
✓ Directory creation test passed
✓ Agent creation test passed
✓ Payment info addition test passed

Tests passed: 5/5
All tests passed! ✓
```

## Troubleshooting

### "No OpenAI API key found"

Make sure you have either:
1. Created a `.env` file with `OPENAI_API_KEY=your-key`
2. Set the environment variable: `export OPENAI_API_KEY=your-key`
3. Entered it during the setup wizard

### "Module not found"

Install all dependencies:
```bash
pip install -r requirements.txt
```

### "Permission denied"

Make sure the script is executable:
```bash
chmod +x anti_scammy.py
```

### Messages seem generic

The AI learns over time! Also, you can customize the persona:
1. Edit `config.json`
2. Add more specific personality traits
3. Add detailed backstory
4. Restart the companion

## Next Steps

1. **Customize the persona** - Edit `config.json` to match your needs
2. **Test messages** - Run `--message` a few times to see variety
3. **Set up scheduling** - Use `--run` for automatic messages
4. **Enable payment protection** - Add Cash App tag if needed
5. **Add voice/images** - See ADVANCED.md for setup

## Getting Help

- **Documentation**: See README.md for full documentation
- **Advanced Features**: See ADVANCED.md for advanced usage
- **Issues**: Report bugs at https://github.com/ZackBradshaw/Anti-Grammy-Scammy/issues
- **Scam Resources**: 
  - FTC: https://reportfraud.ftc.gov/
  - AARP: https://www.aarp.org/money/scams-fraud/

## Important Reminders

⚠️ **This is a protective tool**
- Ensure elderly users understand this is an AI companion
- Family members should monitor usage
- Payment protection redirects to user's own account
- This is part of scam education, not a complete solution

🔒 **Security**
- Never share your API keys
- Keep `.env` file private
- Regular check-ins with family
- Monitor all financial activity

❤️ **Purpose**
- Provide genuine companionship
- Protect against romance scams
- Maintain dignity and independence
- Support, not replace, family connections

---

**Ready to start?**

```bash
python anti_scammy.py --setup
```

Welcome to Anti-Grammy-Scammy! 💕🛡️
