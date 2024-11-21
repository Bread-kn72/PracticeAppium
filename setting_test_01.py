import unittest, time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung_Galaxy_Tab_S7_FE API 34',
    appPackage='com.android.settings',
    appActivity='.Settings'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_settings(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Apps"]')
        el.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()