from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhonePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_phone_title = "com.more.laozi:id/register_tv_input_phone_title"

    def get_result_text(self):
        # 等待元素可見
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((AppiumBy.ID, self.input_phone_title)))
        return element.text
