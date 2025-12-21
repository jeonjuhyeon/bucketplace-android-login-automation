from settings import *

def kill_app(driver):
    try:
        driver.terminate_app(APP_PACKAGE)
    except Exception:
        pass

def run_app(driver):
    try:
        driver.activate_app(APP_PACKAGE)
    except Exception:
        pass
