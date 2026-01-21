# Advanced Usage Guide

## Table of Contents
1. [Advanced Configuration](#advanced-configuration)
2. [Image Generation Setup](#image-generation-setup)
3. [Voice Customization](#voice-customization)
4. [Scheduling Strategies](#scheduling-strategies)
5. [Security Best Practices](#security-best-practices)
6. [Integration with Other Tools](#integration-with-other-tools)

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

### SMS Integration (with Twilio)

Send messages via SMS:

```python
from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = companion.generate_message()

client.messages.create(
    body=message,
    from_='+1234567890',
    to='+0987654321'
)
```

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
