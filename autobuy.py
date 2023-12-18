# 載入需要的套件
from selenium import webdriver
from time import sleep
import datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import winsound

caps = DesiredCapabilities().FIREFOX#加速
caps["pageLoadStrategy"] = "eager"#加速complete eager none


# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Firefox()
# 方法二：或是直接指定exe檔案路徑
#driver = webdriver.Firrefox("桌面\chromedriver")
#driver.close() # 關閉瀏覽器視窗


driver.implicitly_wait(5)  # 隐性等待，最长等10秒

website = int(input("1.蝦皮 2.pchome 3.momo 4.yahoo :"))
url = str(input("請輸入網址:"))
#fps = float(input("刷新速度(單位:秒)(依網站及網路調整):"))
#test = int(input("1.測試不登入 2.開搶:"))



if website==1:#蝦皮
    print("請在一分鐘內登入完成")
    driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F")
    inputElement = driver.find_element_by_name("loginKey")#登入輸入框
    inputElement.send_keys("xxxxxxx")
    inputElement = driver.find_element_by_name("password")#密碼輸入框
    inputElement.send_keys("xxxxxxxx")
    sleep(0.5)
    button = driver.find_element_by_class_name("_1ruZ5a._3Nrkgj._3kANJY._1IRuK_.hh2rFL._3_offS")#登入按鈕
    button.click()
    sleep(50)
    #蝦皮
    driver.get("https://shopee.tw/i5-3570k-cpu-1155-%E8%B6%85%E9%A0%BB-2500k-2550k-i7-2600k-2700k-3770k-%E5%8F%83%E8%80%83-i.16828298.3029543647")#更改網址以前往不同網頁
    def buy_refresh():
        while True: #不斷刷新網頁

            if EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-solid-primary.btn--l._3Kiuzg")):#當此元素存在
                button = driver.find_element_by_class_name("btn.btn-solid-primary.btn--l._3Kiuzg")#直接購買按鈕
                button.click()
                button = driver.find_element_by_class_name("product-variation")#去買單按鈕
                button.click()
                button = driver.find_element_by_class_name("shopee-button-solid.shopee-button-solid--primary")#貨到付款按鈕
                button.click()
                #button = driver.find_element_by_class_name("stardust-button.stardust-button--primary.stardust-button--large._2g81WV")#結帳按鈕
                button.click()
            else:
                time.sleep(0.01)#注意刷新間隔時間要儘量短
                driver.refresh()
    buy_refresh()#不斷執行

elif website==2:#pchome
    print("請在一分鐘內登入完成")
    driver.get("http://pcportal.pchome.com.tw/resourceApi/xpvip/login?to=PSH&amp;ref=")
    print("60s")
    time.sleep(10)
    print("50s")
    time.sleep(10)
    print("40s")
    time.sleep(10)
    print("30s")
    time.sleep(10)
    print("20s")
    time.sleep(10)
    print("10s")
    driver.get(url)
    def buy_refresh():
        while True:#不斷刷新網頁
            try:
                WebDriverWait(driver,0.2,0.01).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.site_btn.origncheckbutton.addBigCart button")))#當此元素存在
                button = driver.find_element_by_css_selector("li.site_btn.origncheckbutton.addBigCart button")#加入購物車
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("a#24hrCartContainer"))#結帳
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("li.ATM a.ui-btn"))#ATM轉帳
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("a#warning-timelimit_btn_confirm.ui-btn"))#繼續
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("div#normal_chk label"))#繼續
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("a#btnSubmmit.send"))#確定送出
                button.click()
                print('結束')
                winsound.MessageBeep(-1)
                break
            except:
                print('reload')
                driver.find_element_by_tag_name("body").send_keys("Keys.ESCAPE")
                time.sleep(0.01)#注意刷新間隔時間要儘量短
                driver.refresh()

    buy_refresh()#不斷執行
    
elif website==3:#momo
    print("請在一分鐘內登入完成")
    driver.get("https://www.momoshop.com.tw/main/Main.jsp")
    print("60s")
    time.sleep(10)
    print("50s")
    time.sleep(10)
    print("40s")
    time.sleep(10)
    print("30s")
    time.sleep(10)
    print("20s")
    time.sleep(10)
    print("10s")
    driver.get(url)
    def buy_refresh():
        while True:#不斷刷新網頁
            try:
                WebDriverWait(driver,0.2,0.01).until(EC.presence_of_element_located((By.CSS_SELECTOR, "dl.checkoutArea dt")))#當此元素存在
                button = driver.find_element_by_css_selector("dl.checkoutArea dt")#去結帳
                button.click()
                WebDriverWait(driver,0.5,0.01).until(button = driver.find_element_by_css_selector("ul.checkoutDetailsArea li.checkoutBtn"))#結帳
                button.click()
                WebDriverWait(driver,0.5,0.01).until(button = driver.find_element_by_css_selector("div.fillinBox.payment label.cashdelivery"))#貨到付款
                button.click()
                WebDriverWait(driver,1,0.01).until(button = driver.find_element_by_css_selector("div.completeArea a#orderSave"))#確認結帳
                button.click()
                print('結束')
                winsound.MessageBeep(-1)
                break
            except:
                print('reload')
                driver.find_element_by_tag_name("body").send_keys("Keys.ESCAPE")
                time.sleep(0.01)#注意刷新間隔時間要儘量短
                driver.refresh()

    buy_refresh()#不斷執行

elif website==4: #yahoo
    print("請在一分鐘內登入完成")
    driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8735289&Area=search&mdiv=403&oid=1_8&cid=index&kw=switch") 
    def buy_refresh():
        while True: #不斷刷新網頁

            if EC.element_to_be_clickable((By.CLASS_NAME,"buyNowBtn")):#當此元素存在
                button = driver.find_element_by_class_name("buyNowBtn")#直接購買按鈕
                button.click()
                print('GOOD')
            else:
                print('bad')
                time.sleep(0.01)#注意刷新間隔時間要儘量短
                driver.refresh()

    buy_refresh()#不斷執行

#YAHOO
#driver.get('https://reurl.cc/GdgaGG') # 更改網址以前往不同網頁

#sleep(20)
#driver.get('https://reurl.cc/GdgaGG') # 更改網址以前往不同網頁
#button = driver.find_element_by_class_name("SasCheckoutButton__mod___1BK9F.CheckoutBar__buyNowBtn___qgDtR.CheckoutBar__checkoutButton___jSkkJ")#立即購買
#button.click()

"""
def buy_on_time(buytime):
    while True: #不斷刷新時鐘
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id("kw").send_keys(Keys.F5)
            button = driver.find_element_by_class_name("SasCheckoutButton__mod___1BK9F.CheckoutBar__buyNowBtn___qgDtR.CheckoutBar__checkoutButton___jSkkJ")#立即購買
            button.click()
            # 点击结算按钮
            sleep(2)
            button = driver.find_element_by_class_name("submitButton")#立即購買
            button.click()
            # 提交订单
            sleep(1)
            button = driver.find_element_by_class_name("submitButton")#立即購買
            button.click()
            sleep(0.1)
            button = driver.find_element_by_class_name("DialogLightBox__ActionButton-sc-14al6ym-9.eoybDb")#立即購買
            button.click()
        time.sleep(0.01)#注意刷新間隔時間要儘量短

buy_on_time('2021-03-24 00:00:02')#指定秒殺時間，並且開始等待秒殺
"""

#button = driver.find_element_by_class_name("submitButton")#確認購買
#button.click()
#button = driver.find_element_by_class_name("InputRadioBox__RadioIcon-tjna0c-1 ikJOGV rbxIcon Cur(p)")#貨到付款按鈕
#button.click()
#button = driver.find_element_by_class_name("stardust-button.stardust-button--primary.stardust-button--large._2g81WV")#結帳按鈕
#button.click()

"""
def buy_refresh():
    while True: #不斷刷新網頁
        driver.refresh()
        if EC.element_to_be_clickable(By.XPATH, '//*[@id="buy_yes"]/a/img'):#當此元素存在
            driver.find_element_by_id('kw').send_keys(Keys.F5)
            button = driver.find_element_by_class_name('SasCheckoutButton__mod___1BK9F.CheckoutBar__buyNowBtn___qgDtR.CheckoutBar__checkoutButton___jSkkJ')#立即購買
            button.click()
            # 点击结算按钮
            sleep(2)
            button = driver.find_element_by_class_name('submitButton')#立即購買
            button.click()
            # 提交订单
            sleep(1)
            button = driver.find_element_by_class_name('submitButton')#立即購買
            button.click()
            sleep(0.1)
            button = driver.find_element_by_class_name('DialogLightBox__ActionButton-sc-14al6ym-9.eoybDb')#立即購買
            button.click()
        time.sleep(0.01)#注意刷新間隔時間要儘量短

buy_refresh()#不斷執行
"""