from appium import webdriver
from test_cases.TKR_Login import 

def setup_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "adb-R9YTB03PNMP-RjSBb0._adb-tls-connect._tcp",
        "automationName": "UiAutomator2"
    }
    print("Initializing Appium driver...")
    driver = webdriver.Remote("http://localhost:4800", capabilities)
    return driver

def run_tests(driver):
   

if __name__ == "__main__":
    driver = setup_driver()  # Appium 드라이버 초기화
    try:
        run_tests(driver)  # 테스트 실행
    finally:
        print("Closing Appium driver...")
        driver.quit()  # 테스트 후 드라이버 종료