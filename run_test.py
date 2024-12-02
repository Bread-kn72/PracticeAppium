from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


def setup_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "adb-R9YTB03PNMP-RjSBb0._adb-tls-connect._tcp",
        "automationName": "UiAutomator2",
        "appPackage" : "net.monki.tableorder.staging",
        "appActivity" : "net.monki.tableorder",
        "noReset" : False
    }
    print("Initializing Appium driver...")
    driver = webdriver.Remote("http://localhost:4800", capabilities)
    return driver
    

if __name__ == "__main__":
    driver = setup_driver()  # Appium 드라이버 초기화
    try:
        driver.find_element(by=By.XPATH,)
    finally:
        print("Closing Appium driver...")
        driver.quit()  # 테스트 후 드라이버 종료