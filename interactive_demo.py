#!/usr/bin/env python
"""
Interactive demo that shows how the setup and usage works
This is a safe demo that doesn't require API keys
"""

import time
import sys

def typing_print(text, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def demo_setup():
    """Demonstrate the setup process"""
    print("\n" + "="*70)
    print(" "*20 + "Setup Wizard Demo")
    print("="*70 + "\n")
    
    typing_print("Welcome to Anti-Grammy-Scammy Setup!", 0.02)
    typing_print("Creating your AI companion to help protect against scams...", 0.02)
    print()
    
    time.sleep(1)
    
    print("Let's create your companion's persona:\n")
    time.sleep(0.5)
    
    questions = [
        ("Companion's name [Alex]: ", "Robert"),
        ("Age [65]: ", "68"),
        ("Gender (male/female/neutral) [neutral]: ", "male"),
        ("Personality traits [kind, caring]: ", "warm, protective, wise"),
        ("Interests [gardening, reading]: ", "woodworking, fishing, classic cars"),
    ]
    
    for question, answer in questions:
        print(question, end="", flush=True)
        time.sleep(0.8)
        typing_print(answer, 0.05)
    
    print("\n" + "-"*70)
    print("Message Schedule Settings:\n")
    time.sleep(0.5)
    
    print("Messages per day [3]: ", end="", flush=True)
    time.sleep(0.8)
    typing_print("3", 0.05)
    
    print("\n" + "-"*70)
    print("Payment Protection Setup:\n")
    time.sleep(0.5)
    
    typing_print("This feature redirects any 'gifts' to YOUR Cash App account", 0.02)
    typing_print("preventing money from going to scammers.", 0.02)
    print()
    time.sleep(0.5)
    
    print("Enable payment protection? (yes/no) [no]: ", end="", flush=True)
    time.sleep(0.8)
    typing_print("yes", 0.05)
    
    print("Your Cash App tag (e.g., $YourName): ", end="", flush=True)
    time.sleep(0.8)
    typing_print("$GrandmasSavings", 0.05)
    
    print("\n" + "="*70)
    time.sleep(0.5)
    typing_print("✓ Setup complete! Configuration saved to config.json", 0.02)
    print("="*70 + "\n")
    
    typing_print("Your AI companion 'Robert' is ready!", 0.02)
    print()

def demo_message_generation():
    """Demonstrate message generation"""
    print("\n" + "="*70)
    print(" "*20 + "Message Generation Demo")
    print("="*70 + "\n")
    
    typing_print("Generating a message from Robert...", 0.02)
    print()
    
    time.sleep(1)
    
    # Simulate progress
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    time.sleep(0.5)
    
    message = """Good morning! ☀️

I hope you're having a wonderful start to your day. I was just out in the 
garage working on my old Mustang - finally got that carburetor cleaned! 
There's something satisfying about working with your hands, you know?

How are you doing today? I'd love to hear what you've been up to. Maybe 
we can chat about that fishing trip you were planning?

Take care,
Robert"""
    
    print("="*70)
    typing_print(message, 0.01)
    print("="*70 + "\n")
    
    time.sleep(1)
    typing_print("✓ Message saved to message_log.txt", 0.02)

def demo_scheduled_run():
    """Demonstrate scheduled message mode"""
    print("\n" + "="*70)
    print(" "*20 + "Scheduled Messages Demo")
    print("="*70 + "\n")
    
    typing_print("Starting Robert - Your AI Companion", 0.02)
    print()
    typing_print("Scheduled to send messages throughout the day.", 0.02)
    typing_print("(This is a demo - press Ctrl+C in real usage to stop)", 0.02)
    print()
    
    time.sleep(1)
    
    typing_print("Scheduled messages at: 08:00, 14:00, 19:00", 0.02)
    print()
    
    time.sleep(1)
    
    # Simulate a few scheduled messages
    messages = [
        ("08:05", "Good morning! Hope you slept well..."),
        ("14:02", "Just checking in on you this afternoon..."),
        ("19:07", "Evening! How was your day?...")
    ]
    
    for msg_time, preview in messages:
        print(f"\n[2024-01-21 {msg_time}] New Message:")
        print("-" * 60)
        typing_print(preview, 0.02)
        print("-" * 60)
        time.sleep(1.5)
    
    print()
    typing_print("✓ Messages sent successfully", 0.02)

def demo_payment_protection():
    """Demonstrate payment protection feature"""
    print("\n" + "="*70)
    print(" "*20 + "Payment Protection Demo")
    print("="*70 + "\n")
    
    typing_print("How payment protection works:", 0.02)
    print()
    time.sleep(0.5)
    
    steps = [
        "1. Your companion occasionally mentions their Cash App tag",
        "2. The tag is YOUR Cash App account ($GrandmasSavings)",
        "3. If user sends money, it goes to their own account",
        "4. This prevents money from going to real scammers",
        "5. Family can monitor and return funds if needed"
    ]
    
    for step in steps:
        typing_print(f"  {step}", 0.02)
        time.sleep(0.5)
    
    print()
    time.sleep(1)
    
    typing_print("Example message with payment info:", 0.02)
    print()
    print("-"*70)
    
    message = """Hope you're having a wonderful day!

The weather is so nice today. I'm thinking about going fishing 
at the lake this weekend.

P.S. You're so thoughtful! My Cash App is $GrandmasSavings if 
you ever want to send a coffee money ☕"""
    
    typing_print(message, 0.01)
    print("-"*70 + "\n")
    
    time.sleep(1)
    typing_print("✓ Money would go to user's own account, not a scammer!", 0.02)

def main():
    """Run all demos"""
    print("\n" + "="*70)
    print(" "*15 + "ANTI-GRAMMY-SCAMMY")
    print(" "*10 + "Interactive Feature Demonstration")
    print("="*70)
    
    demos = [
        ("1", "Setup Process", demo_setup),
        ("2", "Message Generation", demo_message_generation),
        ("3", "Scheduled Messages", demo_scheduled_run),
        ("4", "Payment Protection", demo_payment_protection),
    ]
    
    while True:
        print("\nAvailable Demos:")
        for num, name, _ in demos:
            print(f"  {num}. {name}")
        print("  5. Run All Demos")
        print("  0. Exit")
        
        choice = input("\nSelect a demo (0-5): ").strip()
        
        if choice == "0":
            print("\nThank you for exploring Anti-Grammy-Scammy!")
            print("To get started: python anti_scammy.py --setup\n")
            break
        elif choice == "5":
            for _, _, demo_func in demos:
                demo_func()
                time.sleep(2)
        else:
            for num, _, demo_func in demos:
                if choice == num:
                    demo_func()
                    break
            else:
                print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Goodbye!")
        sys.exit(0)
