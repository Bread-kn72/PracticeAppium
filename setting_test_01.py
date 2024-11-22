import unittest, time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='adb-R9YTB03PNMP-RjSBb0._adb-tls-connect._tcp',
    appPackage='com.android.settings',
    appActivity='.Settings'
)

appium_server_url = 'http://localhost:4800'

class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_find_settings(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="기기 간 연결"]')
        el.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()