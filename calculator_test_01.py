from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Samsung_Galaxy_Tab_S7_FE API TiramisuPrivacySandbox",
    "appPackage": "com.android.calculator2",
    "appActivity": ".Calculator",
    "automationName": "UiAutomator2"
}

# Appium 서버에 연결
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

try:
    # 2 버튼 클릭
    button_2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")')
    button_2.click()

    # + 버튼 클릭
    plus_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("plus")')
    plus_button.click()

    # 3 버튼 클릭
    button_3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")')
    button_3.click()

    # = 버튼 클릭
    equals_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("equals")')
    equals_button.click()

    # 결과 가져오기
    result = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.calculator2:id/result")')
    print(f"결과값: {result.text}")  # 결과 출력

finally:
    # 세션 종료
    driver.quit()