# 📱 Appium 自動化測試練習專案

這是一個使用 Python + Appium 撰寫的 Android App 自動化測試範例，採用 Page Object Model（POM）設計模式，主要目的是展示我在 UI 自動化測試上的基礎實作能力，做為面試展示作品。


## 🧩 使用技術

- Python
- Appium
- Appium-Python-Client
- Page Object Model (POM)
- PyCharm 開發環境


## 📂 專案結構
```
Auto_APP_Test/
├── run.py                     # 主程式入口
├── utils/
│   └── driver_setup.py        # 初始化 driver 設定
├── pages/
│   ├── home_page.py           # 首頁元件與操作封裝
│   └── phone_page.py          # 手機登入頁面元件與操作封裝
├── tests/
│   └── test_home_page.py      # 測試案例
├── Pipfile                    # 套件管理
└── Pipfile.lock               # 套件鎖定
```

## ✅ 已完成功能

- 建立基本 Appium 測試架構
- 點擊首頁的「手機登入」按鈕
- 驗證跳轉頁面是否顯示特定文字
- 加入簡單斷言（assert）做功能驗證


## 🚀 執行方式

請先安裝 [Appium Server](https://appium.io/) 並啟動，再執行：

```bash
pipenv install         # 安裝環境與相依套件
pipenv shell           # 進入虛擬環境
python run.py          # 執行測試
```


## 🔖 注意事項

- 測試手機需開啟 USB 偵錯，並連接至電腦
- appPackage 與 appActivity 記得依實際 APP 調整
- 須啟動 Appium Server 並連接裝置，方能正常執行
