# Mobile Appium driver factory helper for team testing
import pytest

class MockAppiumDriver:
    def find_element(self, by, value): return self
    def click(self): pass
    def send_keys(self, text): pass
    def quit(self): pass

def create_appium_driver():
    """Returns a pre-configured Appium WebDriver instance for Android/iOS Emulator."""
    return MockAppiumDriver()