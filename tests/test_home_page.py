from pages.home_page import HomePage
from pages.phone_page import PhonePage


def test_button_click(driver):
    home = HomePage(driver)
    home.click_btn_phone()

    success = PhonePage(driver)
    result = success.get_result_text()
    assert result == "輸入手機門號"
