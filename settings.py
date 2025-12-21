from dotenv import load_dotenv
import os

##driver setting
APPIUM_SERVER_URL = "http://localhost:4723"

PLATFORM_NAME = "Android"
AUTOMATION_NAME = "UiAutomator2"
DEVICE_NAME = "emulator-5554"

APP_PACKAGE = "net.bucketplace"
APP_ACTIVITY = "se.ohou.screen.splash.SplashActivity"

IMPLICIT_WAIT = 5

##test setting
load_dotenv()
TEST_EMAIL = os.getenv("EMAIL")
TEST_PASSWORD = os.getenv("PASSWORD")