from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_phone = "com.more.laozi:id/preload_btn_phone"
        self.btn_recommend = "com.more.laozi:id/preload_iv_recommend"
        self.btn_account = "com.more.laozi:id/preload_btn_account"
        self.btn_free = "com.more.laozi:id/preload_btn_free"
        self.btn_line = "com.more.laozi:id/preload_btn_line"
        self.btn_fb = "com.more.laozi:id/preload_btn_fb"
        self.btn_google = "com.more.laozi:id/preload_btn_google"
        self.btn_apple = "com.more.laozi:id/preload_btn_apple"

    def wait_for_element_and_click(self, element_id, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((AppiumBy.ID, element_id)))
        element.click()

    def click_btn_phone(self):
        self.wait_for_element_and_click(self.btn_phone)

    def click_btn_recommend(self):
        self.wait_for_element_and_click(self.btn_recommend)

    def click_btn_account(self):
        self.wait_for_element_and_click(self.btn_account)

    def click_btn_free(self):
        self.wait_for_element_and_click(self.btn_free)

    def click_btn_line(self):
        self.wait_for_element_and_click(self.btn_line)

    def click_btn_fb(self):
        self.wait_for_element_and_click(self.btn_fb)

    def click_btn_google(self):
        self.wait_for_element_and_click(self.btn_google)

    def click_btn_apple(self):
        self.wait_for_element_and_click(self.btn_apple)
