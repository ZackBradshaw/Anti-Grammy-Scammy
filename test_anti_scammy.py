#!/usr/bin/env python
"""
Basic tests for Anti-Grammy-Scammy

These tests verify the core functionality without requiring API keys.
"""

import os
import sys
import json
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anti_scammy import AntiScammyCompanion


def test_config_creation():
    """Test that default configuration is created properly"""
    print("Testing configuration creation...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.json")
        
        # Set a test API key to avoid warnings
        os.environ['OPENAI_API_KEY'] = 'test-key'
        
        companion = AntiScammyCompanion(config_path=config_path)
        
        # Check that config was created
        assert os.path.exists(config_path), "Config file not created"
        
        # Check config structure
        assert "persona" in companion.config
        assert "schedule" in companion.config
        assert "content_settings" in companion.config
        assert "payment" in companion.config
        
        # Check persona fields
        persona = companion.config["persona"]
        assert "name" in persona
        assert "age" in persona
        assert "personality" in persona
        
        print("✓ Configuration creation test passed")


def test_config_save_load():
    """Test saving and loading configuration"""
    print("Testing configuration save/load...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.json")
        
        os.environ['OPENAI_API_KEY'] = 'test-key'
        
        # Create and modify config
        companion = AntiScammyCompanion(config_path=config_path)
        companion.config["persona"]["name"] = "TestName"
        companion.config["payment"]["cashapp_tag"] = "$TestTag"
        companion.save_config()
        
        # Load config again
        companion2 = AntiScammyCompanion(config_path=config_path)
        
        # Verify changes persisted
        assert companion2.config["persona"]["name"] == "TestName"
        assert companion2.config["payment"]["cashapp_tag"] == "$TestTag"
        
        print("✓ Configuration save/load test passed")


def test_directories_created():
    """Test that necessary directories are created"""
    print("Testing directory creation...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.json")
        
        os.environ['OPENAI_API_KEY'] = 'test-key'
        
        # Change to temp directory
        original_dir = os.getcwd()
        os.chdir(tmpdir)
        
        try:
            companion = AntiScammyCompanion(config_path=config_path)
            
            # Check directories exist
            assert os.path.exists("generated_images"), "generated_images directory not created"
            assert os.path.exists("generated_voices"), "generated_voices directory not created"
            assert os.path.exists("personas"), "personas directory not created"
            
            print("✓ Directory creation test passed")
        finally:
            os.chdir(original_dir)


def test_agent_creation():
    """Test that Swarms agent is created properly"""
    print("Testing agent creation...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.json")
        
        os.environ['OPENAI_API_KEY'] = 'test-key'
        
        companion = AntiScammyCompanion(config_path=config_path)
        
        # Check agent was created
        assert companion.agent is not None, "Agent not created"
        assert hasattr(companion.agent, 'agent_name'), "Agent missing agent_name"
        
        print("✓ Agent creation test passed")


def test_payment_info_addition():
    """Test that payment info is added correctly"""
    print("Testing payment info addition...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        config_path = os.path.join(tmpdir, "test_config.json")
        
        os.environ['OPENAI_API_KEY'] = 'test-key'
        
        companion = AntiScammyCompanion(config_path=config_path)
        
        # Enable payment
        companion.config["payment"]["enabled"] = True
        companion.config["payment"]["cashapp_tag"] = "$TestTag"
        
        # Test adding payment info
        test_message = "Hello there!"
        
        # This may or may not add payment info due to randomness
        # Just verify it doesn't crash
        result = companion.send_message_with_payment_info(test_message)
        assert isinstance(result, str), "Result should be a string"
        
        print("✓ Payment info addition test passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print(" "*20 + "Running Anti-Grammy-Scammy Tests")
    print("="*70 + "\n")
    
    tests = [
        test_config_creation,
        test_config_save_load,
        test_directories_created,
        test_agent_creation,
        test_payment_info_addition,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"Tests passed: {passed}/{len(tests)}")
    if failed == 0:
        print("All tests passed! ✓")
    else:
        print(f"Tests failed: {failed}")
    print("="*70 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
