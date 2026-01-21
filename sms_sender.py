"""
SMS/Text Message sending module for Anti-Grammy-Scammy

This module handles sending text messages to phone numbers using Twilio.
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class SMSSender:
    """Handle SMS sending via Twilio"""
    
    def __init__(self, account_sid: Optional[str] = None, auth_token: Optional[str] = None, 
                 from_number: Optional[str] = None):
        """
        Initialize SMS sender
        
        Args:
            account_sid: Twilio account SID (or from TWILIO_ACCOUNT_SID env var)
            auth_token: Twilio auth token (or from TWILIO_AUTH_TOKEN env var)
            from_number: Twilio phone number to send from (or from TWILIO_PHONE_NUMBER env var)
        """
        self.account_sid = account_sid or os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = auth_token or os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = from_number or os.getenv("TWILIO_PHONE_NUMBER")
        
        self.client = None
        if self.account_sid and self.auth_token:
            try:
                from twilio.rest import Client
                self.client = Client(self.account_sid, self.auth_token)
            except ImportError:
                print("Warning: Twilio not installed. Run: pip install twilio")
            except Exception as e:
                print(f"Warning: Could not initialize Twilio client: {e}")
    
    def is_configured(self) -> bool:
        """Check if SMS sending is properly configured"""
        return (self.client is not None and 
                self.from_number is not None and 
                len(self.from_number) > 0)
    
    def send_sms(self, to_number: str, message: str) -> bool:
        """
        Send an SMS message
        
        Args:
            to_number: Phone number to send to (E.164 format, e.g., +1234567890)
            message: Message text to send
            
        Returns:
            True if message sent successfully, False otherwise
        """
        if not self.is_configured():
            print("SMS not configured. Please set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER")
            return False
        
        if not to_number:
            print("No phone number specified")
            return False
        
        # Ensure phone number is in E.164 format
        if not to_number.startswith('+'):
            print(f"Warning: Phone number should be in E.164 format (e.g., +1234567890), got: {to_number}")
            # Try to add +1 for US numbers if it looks like a 10-digit number
            if len(to_number.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')) == 10:
                to_number = '+1' + to_number.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
                print(f"Auto-formatted to: {to_number}")
        
        try:
            message_obj = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            print(f"SMS sent successfully! Message SID: {message_obj.sid}")
            return True
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return False
    
    def validate_phone_number(self, phone_number: str) -> bool:
        """
        Validate a phone number format
        
        Args:
            phone_number: Phone number to validate
            
        Returns:
            True if valid format, False otherwise
        """
        # Remove common formatting characters
        clean_number = phone_number.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
        
        # Check if it starts with + (E.164 format)
        if clean_number.startswith('+'):
            # Should have country code + number (typically 11-15 digits)
            return len(clean_number) >= 11 and len(clean_number) <= 16 and clean_number[1:].isdigit()
        
        # Check if it's a 10-digit US number
        if len(clean_number) == 10 and clean_number.isdigit():
            return True
        
        return False


def send_test_message():
    """Send a test SMS message"""
    sender = SMSSender()
    
    if not sender.is_configured():
        print("\nSMS not configured. To use SMS features:")
        print("1. Sign up for Twilio at https://www.twilio.com/")
        print("2. Get your Account SID, Auth Token, and phone number")
        print("3. Add to .env file:")
        print("   TWILIO_ACCOUNT_SID=your_account_sid")
        print("   TWILIO_AUTH_TOKEN=your_auth_token")
        print("   TWILIO_PHONE_NUMBER=+1234567890")
        return
    
    print("SMS is configured!")
    print(f"From number: {sender.from_number}")
    
    # Prompt for test
    to_number = input("\nEnter phone number to send test message (E.164 format, e.g., +1234567890): ").strip()
    
    if not sender.validate_phone_number(to_number):
        print("Invalid phone number format")
        return
    
    test_message = "Hello! This is a test message from Anti-Grammy-Scammy. Your AI companion is ready to send messages!"
    
    print(f"\nSending test message to {to_number}...")
    success = sender.send_sms(to_number, test_message)
    
    if success:
        print("\n✓ Test message sent successfully!")
    else:
        print("\n✗ Failed to send test message")


if __name__ == "__main__":
    send_test_message()
