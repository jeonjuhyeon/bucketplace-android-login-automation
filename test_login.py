from selenium.webdriver.common.by import By

from driver import *
from settings import *
from actions.element import *
from actions.app_action import *

class Login :
    def Login_001():
        print("Login_001 : 로그인 진입 페이지 노출 확인")
        driver = create_driver()
        try:
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/logo")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/guideImage")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/kakaoLoginButton")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/naverLoginButton")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/facebookLoginButton")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/appleLoginButton")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/emailSignUpText")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/customerServiceTex")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/anonymousOrderCheck")
            print("Login_001 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_001 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()
    
    def Login_002():
        print("Login_002 : 이메일로 로그인 페이지 진입 확인")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/title")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/emailField")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/inputField", "이메일")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/inputField", "비밀번호")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/passwordFindingButton")
            print("Login_002 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_002 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()

    def Login_003():
        print("Login_003 : 이메일 로그인 > 이메일 미입력 시 로그인 불가 확인")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")

            print("Login_003 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_003 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()

    def Login_004():
        print("Login_004 : 이메일 로그인 > 비밀번호 미입력 시 로그인 불가 확인")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "이메일", TEST_EMAIL)
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")
            print("Login_004 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_004 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()

    def Login_005():
        print("Login_005 : 이메일 로그인 > 잘못된 비밀번호 입력 시 로그인 실패 스낵바 노출 확인")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "이메일", TEST_EMAIL)
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "비밀번호", "failpassword")
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.check_message(driver, "10번 실패하면")

            print("Login_005 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_005 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()

    def Login_007():
        print("Login_007 : 이메일 로그인 > 정상 정보 입력 시 로그인 확인")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "이메일", TEST_EMAIL)
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "비밀번호", TEST_PASSWORD)
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.close_popup_if_exists(driver,By.ID, "net.bucketplace:id/com_braze_inappmessage_html_webview")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/bottomNavigation")
            SeleniumElement.click_by_text(driver, "마이페이지")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/bottomNavigation")
            SeleniumElement.check_text(driver,By.CLASS_NAME, "android.widget.TextView", "자동화qa_001")
            SeleniumElement.click(driver,AppiumBy.ACCESSIBILITY_ID,"Gear icon")
            SeleniumElement.check_text(driver,By.CLASS_NAME, "android.widget.TextView", "설정")
            SeleniumElement.logout(driver)

            print("Login_007 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_007 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()

    def Login_008():
        print("Login_008 : 로그인 상태에서 앱 실힝 시")
        driver = create_driver()
        try:
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/emailLogInText")
            SeleniumElement.check_text(driver,By.ID, "net.bucketplace:id/title", "이메일 로그인")
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "이메일", TEST_EMAIL)
            SeleniumElement.input_text_by_hint(driver, By.ID, "net.bucketplace:id/inputField", "비밀번호", TEST_PASSWORD)
            SeleniumElement.click(driver,By.ID, "net.bucketplace:id/loginButton")
            SeleniumElement.close_popup_if_exists(driver,By.ID, "net.bucketplace:id/com_braze_inappmessage_html_webview")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/bottomNavigation")
            kill_app(driver)
            run_app(driver)
            SeleniumElement.close_popup_if_exists(driver,By.ID, "net.bucketplace:id/com_braze_inappmessage_html_webview")
            SeleniumElement.check(driver,By.ID, "net.bucketplace:id/bottomNavigation")

            print("Login_008 : PASS")
            return True
        
        except AssertionError as e:
            print(f"Login_008 : FAIL - {e}")
            return False
        
        finally:
            kill_app(driver)
            driver.quit()