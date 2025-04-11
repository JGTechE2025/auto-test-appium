from appium import webdriver
from appium.options.android import UiAutomator2Options


def init_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "J3AXB7629768BEA"
    options.app_package = "com.more.laozi"
    options.app_activity = "sgt.o8app.ui.LaunchActivity"
    options.platform_version = "9"
    options.auto_grant_permissions = True
    options.no_reset = False
    options.full_reset = False

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub",
        options=options
    )

    driver.implicitly_wait(10)
    return driver
