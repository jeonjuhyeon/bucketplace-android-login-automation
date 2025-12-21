from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from settings import *

class SeleniumElement :

    def check(driver, by, value):
        try:
            assert driver.find_element(by, value).is_displayed(), f"{value} is not displayed"
        except NoSuchElementException as e :
            raise AssertionError(f"{value} not found") from e
        
    def click(driver, by, value):
        try:
            driver.find_element(by, value).click()
        except NoSuchElementException as e :
            raise AssertionError(f"{value} not found") from e
        
    def click_by_text(driver, text):
        elements = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")

        for element in elements:
            if element.text.strip() == text:
                element.click()
                return
        raise AssertionError(f"Text not found: {text}")
        
    def close_popup_if_exists(driver, by, value):
        elements = driver.find_elements(by, value)
        if elements:
            driver.back()

    def input_text(driver, by, value, text):
        try:
            driver.find_element(by, value).click()
            driver.find_element(by, value).clear()
            driver.find_element(by, value).send_keys(text)
        except NoSuchElementException as e :
            raise AssertionError(f"{value} not found") from e
        
    def input_text_by_hint(driver, by, value, hint_text, text):
        elements = driver.find_elements(by, value)
        for element in elements :
            if element.get_attribute("hint") == hint_text:
                element.click()
                try:
                    element.clear()
                except Exception:
                    pass
                element.send_keys(text)
                return
        raise AssertionError(f"{hint_text} not found")
        
    def check_text(driver, by, value, expected):
        elements = driver.find_elements(by, value)
        if not elements:
            raise AssertionError(f"{value} not found")
        
        for el in elements :
            text = el.text.strip()
            if text == expected : 
                return
            
        raise AssertionError(
        f"{value} text mismatch "
        f"(expected='{expected}', text={[el.text.strip() for el in elements]})"
    )

    def check_message(driver, expected_text, timeout=5):
        try :
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().textContains("{expected_text}")'
                ))
            )
        except TimeoutException:
            raise AssertionError(f"Message not found: '{expected_text}'")

    def scroll_to_text_and_click(driver, text):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

        elements = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
        for element in elements:
            if element.text.strip() == text:
                parent = element.find_element(By.XPATH, "..")
                if parent.get_attribute("clickable") == "true":
                    parent.click()
                else:
                    element.click()
                    
                return

        raise AssertionError(f"'{text}' not found")
  
    def logout(driver):
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().text("로그아웃"))'
        )
        # NOTE:
        # '로그아웃' 버튼은 고유 resource-id/accessibility-id가 없어 XPath 사용
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='로그아웃']/..").click()

        # raise AssertionError("'로그아웃' not found")
