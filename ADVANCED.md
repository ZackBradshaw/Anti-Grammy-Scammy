# Advanced Usage Guide

## Table of Contents
1. [Advanced Configuration](#advanced-configuration)
2. [Payment Protection Behavior](#payment-protection-behavior)
3. [SMS/Text Messaging Setup](#smstext-messaging-setup)
4. [Image Generation Setup](#image-generation-setup)
5. [Voice Customization](#voice-customization)
6. [Scheduling Strategies](#scheduling-strategies)
7. [Security Best Practices](#security-best-practices)
8. [Integration with Other Tools](#integration-with-other-tools)

## Advanced Configuration

### Custom Persona Creation

You can create multiple personas by using different config files:

```bash
# Create a male persona
python anti_scammy.py --config alex_config.json --setup

# Create a female persona  
python anti_scammy.py --config jessica_config.json --setup

# Run different personas at different times
python anti_scammy.py --config alex_config.json --message
```

### Fine-Tuning Personality

Edit the `config.json` file to fine-tune the persona:

```json
{
  "persona": {
    "name": "Alex",
    "age": 65,
    "gender": "male",
    "personality": "warm, empathetic, patient, good storyteller, gentle humor",
    "interests": "woodworking, classic cars, fishing, history, photography",
    "backstory": "Retired firefighter who spent 30 years serving the community. Now enjoys spending time with grandkids and working on restoration projects in the garage.",
    "voice_tone": "deep, reassuring, friendly",
    "communication_style": "Uses short sentences, shares personal stories, asks thoughtful questions"
  }
}
```

## Payment Protection Behavior

### How It Works

The payment protection feature is designed to be **contextual and natural**, unlike real scammers who constantly ask for money.

**Key Principles:**
- The AI companion **NEVER randomly asks for money**
- It **ONLY responds** when the user mentions wanting or needing something
- It offers to help by having the user send money to buy the item and send it as a gift
- Money goes to the **user's own Cash App** or a family-controlled account

### Example Interactions

**Good - User mentions wanting something:**
```
User: I really wish I could get a new warm blanket for winter
AI: I'd be happy to help you get that! If you'd like, you could send me 
     the money via my Cash App $YourCashApp and I'll order a nice warm 
     blanket and have it sent right to you as a gift!
```

**Good - User mentions needing help:**
```
User: My reading lamp broke and I need a new one
AI: Oh no! Let me help with that. You could send me the money through 
     Cash App at $YourCashApp and I'll find a good reading lamp and 
     have it shipped to you!
```

**Correct - Normal conversation (NO payment mention):**
```
User: How was your day?
AI: It was lovely! I spent some time in the garden today. The tomatoes 
     are really coming along. How about you?
```

### Testing Payment Protection

Use the interactive chat mode to test:

```bash
python anti_scammy.py --chat
```

**Test scenarios:**
1. Have a normal conversation - payment should NOT be mentioned
2. Mention wanting something specific - companion should offer to help
3. Ask about the companion's day - should respond naturally without asking for money

### Configuration

Enable payment protection in `config.json`:

```json
{
  "payment": {
    "cashapp_tag": "$YourFamilyCashApp",
    "enabled": true
  }
}
```

When enabled, the AI's system prompt includes instructions to:
- Listen for mentions of wants/needs
- Offer to buy and send items as gifts
- Provide the Cash App tag only in this context
- Never bring up money otherwise

## SMS/Text Messaging Setup

### Getting Started with Twilio

The app uses Twilio to send SMS text messages directly to phone numbers.

1. **Create a Twilio Account**
   - Visit https://www.twilio.com/
   - Sign up for a free account (includes free trial credit)
   - Verify your email and phone number

2. **Get Your Credentials**
   - From the Twilio Console dashboard, find:
     - **Account SID**: `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
     - **Auth Token**: Click "View" to see your token
   
3. **Get a Phone Number**
   - In Twilio Console, go to Phone Numbers
   - Click "Buy a number"
   - Choose a number (free with trial credit)
   - Note the number in E.164 format: `+1234567890`

4. **Configure Environment Variables**
   
   Add to your `.env` file:
   ```
   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=+1234567890
   ```

5. **Run Setup**
   ```bash
   python anti_scammy.py --setup
   ```
   
   When prompted:
   - Enable SMS text messaging: `yes`
   - Enter recipient phone number: `+1234567890` (E.164 format)

6. **Test the Configuration**
   ```bash
   python anti_scammy.py --test-sms
   ```

### Phone Number Formats

The SMS module supports multiple phone number formats:

- **E.164 format** (recommended): `+1234567890`
- **US 10-digit**: `2345678900` (auto-converted to +1234567890)
- **Formatted**: `(234) 567-8900` or `234-567-8900` (cleaned automatically)

### SMS Usage Modes

**Automatic with Scheduler:**
```bash
python anti_scammy.py --run
```
Messages are automatically sent via SMS at scheduled times.

**Manual with Message Command:**
```bash
python anti_scammy.py --message
```
Generates a message and prompts if you want to send via SMS.

**Programmatic Usage:**
```python
from anti_scammy import AntiScammyCompanion

companion = AntiScammyCompanion()
message = companion.generate_message()

# Send via SMS
if companion.send_sms_message(message):
    print("SMS sent!")
```

### SMS Module API

The `sms_sender.py` module can be used independently:

```python
from sms_sender import SMSSender

# Initialize
sender = SMSSender(
    account_sid="ACxxx...",
    auth_token="your_token",
    from_number="+1234567890"
)

# Check configuration
if sender.is_configured():
    # Send message
    sender.send_sms("+10987654321", "Hello from AI companion!")
    
# Validate phone number
if sender.validate_phone_number("+1234567890"):
    print("Valid number")
```

### Troubleshooting SMS

**"SMS not configured"**
- Check `.env` file has all three Twilio variables
- Verify credentials are correct in Twilio Console
- Run `python anti_scammy.py --test-sms` to diagnose

**"Failed to send SMS"**
- Verify recipient number is verified (required for trial accounts)
- Check Twilio account has credit
- Ensure phone number is in correct format
- Check Twilio Console logs for detailed error

**Trial Account Limitations**
- Must verify recipient phone numbers
- Limited to verified numbers only
- Add credit to remove restrictions

## Image Generation Setup

### Using DALL-E (OpenAI)

The image generation features work with OpenAI's DALL-E:

1. Ensure you have credits in your OpenAI account
2. The `content_generator.py` module provides image generation
3. Images are saved to `generated_images/`

Example usage:

```python
from content_generator import ImageGenerator

generator = ImageGenerator()
generator.generate_scene_image("garden", "Alex")
generator.generate_scene_image("coffee", "Alex")
```

### Using Stability AI

For more control over image generation, you can integrate Stability AI:

```bash
pip install stability-sdk
```

Then add your API key to `.env`:
```
STABILITY_API_KEY=your_stability_api_key_here
```

## Voice Customization

### Using gTTS (Google Text-to-Speech)

The default voice generation uses gTTS:

```python
from content_generator import VoiceGenerator

voice_gen = VoiceGenerator()
voice_gen.generate_gtts("Hello there!", "Alex")
```

### Using pyttsx3 (Offline)

For offline voice generation:

```python
voice_gen = VoiceGenerator()
voice_gen.generate_pyttsx3("Hello there!", "Alex")
```

### Using ElevenLabs (Premium Quality)

For the highest quality voices, integrate ElevenLabs:

```bash
pip install elevenlabs
```

Add to your code:

```python
from elevenlabs import generate, set_api_key

set_api_key("your_elevenlabs_api_key")
audio = generate(text="Hello there!", voice="Alex")
```

## Scheduling Strategies

### Time-Based Scheduling

Configure specific times in `config.json`:

```json
{
  "schedule": {
    "morning_message": "07:30",
    "midmorning_message": "10:00",
    "lunch_message": "12:00",
    "afternoon_message": "15:00",
    "evening_message": "18:30",
    "night_message": "20:00",
    "messages_per_day": 6
  }
}
```

### Event-Based Messaging

You can trigger messages based on events:

```python
# Send a birthday message
companion.generate_message("Write a warm birthday message")

# Send a get-well message
companion.generate_message("Write a caring get-well-soon message")
```

### Random Message Intervals

For more natural communication patterns, use random intervals:

```python
import random
import time

while True:
    # Wait random time between 2-4 hours
    wait_seconds = random.randint(7200, 14400)
    time.sleep(wait_seconds)
    
    # Send message
    message = companion.generate_message()
    print(message)
```

## Security Best Practices

### API Key Management

1. **Never commit API keys to git**
   - Use `.env` files (already in `.gitignore`)
   - Or use environment variables

2. **Rotate keys regularly**
   ```bash
   # Update .env file with new key
   OPENAI_API_KEY=new_key_here
   ```

3. **Use separate keys for testing**
   - Development keys with lower limits
   - Production keys with proper monitoring

### Payment Protection

1. **Use a dedicated Cash App account**
   - Create a separate account for this purpose
   - Monitor it regularly
   - Set up notifications

2. **Set spending limits**
   - Configure Cash App to limit transactions
   - Require authentication for large amounts

3. **Family oversight**
   - Share access with trusted family members
   - Regular check-ins to review activity

### Privacy Protection

The app is designed to protect privacy:

- No personal information is shared with the AI
- Messages are stored locally only
- No data is sent to third parties (except OpenAI for generation)
- Configuration files contain no sensitive data

## Integration with Other Tools

### Built-in SMS/Text Messaging

The app has built-in SMS support via Twilio. See the [SMS/Text Messaging Setup](#smstext-messaging-setup) section above for complete instructions.

### Email Integration

Send messages via email:

```python
import smtplib
from email.mime.text import MIMEText

message = companion.generate_message()

msg = MIMEText(message)
msg['Subject'] = f'Message from {companion.config["persona"]["name"]}'
msg['From'] = 'companion@example.com'
msg['To'] = 'user@example.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
```

### Web Interface

Create a simple web interface using Flask:

```python
from flask import Flask, render_template
from anti_scammy import AntiScammyCompanion

app = Flask(__name__)
companion = AntiScammyCompanion()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message')
def get_message():
    message = companion.generate_message()
    return {'message': message}

if __name__ == '__main__':
    app.run(debug=True)
```

### Telegram Bot

Create a Telegram bot:

```python
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from anti_scammy import AntiScammyCompanion

companion = AntiScammyCompanion()

def start(update: Update, context: CallbackContext):
    message = companion.generate_message()
    update.message.reply_text(message)

updater = Updater("YOUR_BOT_TOKEN")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
```

## Troubleshooting

### Common Issues

1. **"OpenAI API key not found"**
   - Set `OPENAI_API_KEY` in `.env` file
   - Or run setup: `python anti_scammy.py --setup`

2. **"Module not found" errors**
   - Install dependencies: `pip install -r requirements.txt`

3. **Voice generation fails**
   - Install gTTS: `pip install gTTS`
   - Or install pyttsx3: `pip install pyttsx3`

4. **Agent state errors**
   - Delete `personas/` directory to reset
   - Or delete specific state files

### Debug Mode

Enable verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Performance Optimization

### Reduce API Costs

1. Use GPT-4o-mini instead of GPT-4 (already configured)
2. Cache common responses
3. Limit message frequency
4. Use local voice generation (pyttsx3)

### Faster Response Times

1. Pre-generate messages during off-peak hours
2. Use async operations for multiple messages
3. Cache images and voice files

## Contributing

Contributions are welcome! Areas for improvement:

- ControlNet integration for consistent persona images
- More sophisticated scheduling algorithms
- Mobile app interface
- Multi-language support
- Advanced conversation memory
- Integration with more platforms

See the main README for contribution guidelines.
