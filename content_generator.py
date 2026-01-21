"""
Advanced image generation module for Anti-Grammy-Scammy

This module provides image generation capabilities using:
- OpenAI DALL-E for general images
- Stability AI for more control
- ControlNet for pose-consistent persona images
"""

import os
from typing import Optional
from datetime import datetime
from pathlib import Path


class ImageGenerator:
    """Handle image generation for the AI companion"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.output_dir = Path("generated_images")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_dalle_image(self, prompt: str, persona_name: str) -> Optional[str]:
        """Generate image using DALL-E"""
        try:
            import openai
            openai.api_key = self.api_key
            
            # Enhance prompt with persona context
            enhanced_prompt = f"A warm, friendly photo suitable for a companion message: {prompt}"
            
            response = openai.Image.create(
                prompt=enhanced_prompt,
                n=1,
                size="512x512"
            )
            
            image_url = response['data'][0]['url']
            
            # Download and save image
            import requests
            from PIL import Image
            from io import BytesIO
            
            img_data = requests.get(image_url).content
            img = Image.open(BytesIO(img_data))
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = self.output_dir / f"{persona_name}_{timestamp}.png"
            img.save(filename)
            
            print(f"Image saved: {filename}")
            return str(filename)
            
        except ImportError:
            print("OpenAI package not properly configured for image generation")
            return None
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
    
    def generate_scene_image(self, scene_description: str, persona_name: str) -> Optional[str]:
        """Generate a scene image (garden, sunset, coffee, etc.)"""
        scene_prompts = {
            "garden": "Beautiful flourishing garden with colorful flowers and vegetables",
            "sunset": "Peaceful sunset over a quiet neighborhood",
            "coffee": "Warm cup of coffee on a wooden table with morning light",
            "book": "Cozy reading nook with comfortable chair and open book",
            "cooking": "Homemade meal being prepared in a bright kitchen",
            "nature": "Serene nature scene with trees and wildlife"
        }
        
        prompt = scene_prompts.get(scene_description, scene_description)
        return self.generate_dalle_image(prompt, persona_name)
    
    def generate_selfie_style_image(self, persona_description: str, persona_name: str) -> Optional[str]:
        """Generate a persona 'selfie' style image"""
        # Note: This would ideally use ControlNet for consistency
        prompt = f"A warm, friendly selfie-style portrait photo: {persona_description}"
        return self.generate_dalle_image(prompt, persona_name)


class VoiceGenerator:
    """Enhanced voice generation capabilities"""
    
    def __init__(self):
        self.output_dir = Path("generated_voices")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_gtts(self, text: str, persona_name: str, lang: str = 'en') -> Optional[str]:
        """Generate voice using Google Text-to-Speech"""
        try:
            from gtts import gTTS
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = self.output_dir / f"{persona_name}_{timestamp}.mp3"
            
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(str(filename))
            
            print(f"Voice message saved: {filename}")
            return str(filename)
            
        except ImportError:
            print("gTTS not installed. Run: pip install gTTS")
            return None
        except Exception as e:
            print(f"Error generating voice: {e}")
            return None
    
    def generate_pyttsx3(self, text: str, persona_name: str) -> Optional[str]:
        """Generate voice using pyttsx3 (offline)"""
        try:
            import pyttsx3
            
            engine = pyttsx3.init()
            
            # Adjust voice properties for warmer tone
            voices = engine.getProperty('voices')
            # Try to set a more pleasant voice
            if len(voices) > 1:
                engine.setProperty('voice', voices[1].id)  # Often female voice
            
            engine.setProperty('rate', 150)  # Slower, more gentle pace
            engine.setProperty('volume', 0.9)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = self.output_dir / f"{persona_name}_{timestamp}.wav"
            
            engine.save_to_file(text, str(filename))
            engine.runAndWait()
            
            print(f"Voice message saved: {filename}")
            return str(filename)
            
        except ImportError:
            print("pyttsx3 not installed. Run: pip install pyttsx3")
            return None
        except Exception as e:
            print(f"Error generating voice: {e}")
            return None


def demo_image_generation():
    """Demo function for image generation"""
    print("Image Generation Demo")
    print("="*60)
    
    generator = ImageGenerator()
    
    # Test scene generation
    scenes = ["garden", "coffee", "sunset"]
    for scene in scenes:
        print(f"\nGenerating {scene} image...")
        result = generator.generate_scene_image(scene, "Alex")
        if result:
            print(f"✓ Success: {result}")
        else:
            print("✗ Failed")


def demo_voice_generation():
    """Demo function for voice generation"""
    print("\nVoice Generation Demo")
    print("="*60)
    
    generator = VoiceGenerator()
    
    test_message = "Good morning! I hope you're having a wonderful day today."
    
    print("\nGenerating voice with gTTS...")
    result = generator.generate_gtts(test_message, "Alex")
    if result:
        print(f"✓ Success: {result}")
    else:
        print("✗ Failed")


if __name__ == "__main__":
    print("Anti-Grammy-Scammy: Advanced Content Generation")
    print("="*60)
    print("\nThis module provides advanced image and voice generation.")
    print("\nAvailable demos:")
    print("1. Image generation (requires OpenAI API key)")
    print("2. Voice generation (requires gTTS or pyttsx3)")
    print("\nTo use in main app, these functions are integrated automatically.")
