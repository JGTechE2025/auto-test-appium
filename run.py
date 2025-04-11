from utils.driver_setup import init_driver
from tests.test_home_page import test_button_click

driver = init_driver()
try:
    test_button_click(driver)
    print("✅ 測試成功")
except AssertionError:
    print("❌ 測試失敗：結果不符")
except Exception as e:
    print(f"⚠️ 測試出現其他錯誤：{e}")
finally:
    driver.quit()

