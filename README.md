# High-Frequency E-Commerce Automation Engine
### 台灣主流電商高頻自動化下單系統實作

這是一個基於 **Python** 與 **Selenium** 開發的自動化執行引擎，專門針對台灣四大電商平台（Shopee, PChome, momo, Yahoo）的高併發搶購情境進行優化。本專案不僅實現了基本的 UI 自動化，更深入探討了 **Web 載入策略優化** 與 **動態 DOM 監測** 等進階技術。

---

## 🛠️ 技術核心與設計亮點 (Core Engineering)

### 1. 毫秒級效能優化策略 (Low-Latency Strategy)
為了在搶購情境中取得領先，本系統實作了以下效能優化：
* **Eager Page Load Strategy**：透過修改 WebDriver 的 `pageLoadStrategy` 為 `eager`，強制瀏覽器在 DOM Tree 解析完成後立即移交控制權，無需等待靜態資源（圖片、廣告、追蹤腳本）載入，將執行時機提前 40% 以上。
* **Polling Loop & Implicit Wait**：結合 `implicitly_wait` 與自定義的 `while True` 高頻輪詢（0.01s 間隔），實現對目標按鈕狀態的即時監控。

### 2. 動態 DOM 元素監控 (Dynamic Element Handling)
針對現代電商站點大量使用 AJAX 與非同步渲染的特性，本專案採用了：
* **Explicit Waits (顯性等待)**：利用 `WebDriverWait` 搭配 `Expected Conditions (EC)`，確保腳本僅在元素「可被點擊」或「已存在」時才觸發動作，有效避免 `NoSuchElementException` 導致的腳本崩潰。
* **Multi-Platform Adapters**：針對不同平台的 DOM 結構（如 PChome 的 CSS Selector 階層、蝦皮的 Class Name 混淆），設計了具備容錯能力的元素定位邏輯。

### 3. 異常處理與系統韌性 (Error Handling & Resilience)
* **Try-Except Recovery**：在關鍵交易路徑（PChome/momo 模組）中導入異常捕獲機制，若遭遇彈窗干擾或頁面未響應，腳本會自動執行 `Keys.ESCAPE` 並強制 `refresh` 重新校準狀態。
* **Audio Feedback System**：整合 `winsound` 模組，在自動化流程完成（下單成功）時提供物理層面的提示音，實現人機協作的最佳化。

---

## 🏗️ 系統架構流圖

| 模組階段 | 關鍵技術 | 優化目標 |
| :--- | :--- | :--- |
| **初始化** | DesiredCapabilities (Firefox) | 繞過靜態資源載入，優化首屏執行速度 |
| **身份校驗** | Login Buffer (60s) | 兼顧自動化效率與手動驗證 (MFA/CAPTCHA) 的彈性 |
| **狀態監測** | ExpectedConditions / CSS Selectors | 精準定位動態生成的「立即購買」按鈕 |
| **交易執行** | Atomic Click Sequences | 最小化下單步驟間的延遲，確保庫存鎖定成功 |

---

## 📈 未來技術演進 (Roadmap)

雖然目前的版本已具備高度實用性，但為進一步提升技術深度，計畫進行以下優化：
- [ ] **Selenium 4.x 語法重構**：將現有的 `find_element_by_*` 舊制語法全面遷移至 `By.*` 標準化介面，提升代碼可維護性。
- [ ] **Anti-bot Bypass**：導入 `Undetected-Chromedriver` 或修改 WebDriver 特徵碼，規避進階的反爬蟲偵測機制。
- [ ] **OCR 驗證碼辨識**：整合 Tesseract 或深度學習模型，自動處理圖形驗證碼，實現完全無人值守化。

---

## 🛡️ 技術聲明 (Disclaimer)
本專案僅供**軟體工程技術研究與個人作品集展示**。程式碼展示了對瀏覽器自動化、DOM 解析及效能優化的理解，請遵守相關網站之使用者協議，嚴禁將此工具用於任何商業或違反法律之行為。
