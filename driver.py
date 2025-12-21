from appium import webdriver
from appium.options.android import UiAutomator2Options
from settings import *

def create_driver():
    options = UiAutomator2Options()

    options.platform_name = PLATFORM_NAME
    options.device_name = DEVICE_NAME
    options.automation_name = AUTOMATION_NAME
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = True

    driver = webdriver.Remote(
        command_executor=APPIUM_SERVER_URL,
        options=options
    )   

    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver