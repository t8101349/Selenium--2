from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import sys

#定義編碼
sys.stdout.reconfigure(encoding='utf-8')
 
#啟用選項,禁用通知
options = Options()
options.add_argument("--disable-notifications")
 
#打開瀏覽器
chrome = webdriver.Chrome(options=options)
url="https://www.facebook.com/"
chrome.get(url)
 

#定位元素
#email = chrome.find_element(By.ID,"email")
#password = chrome.find_element(By.ID,"pass")

#登入帳號
#email.send_keys('example@gmail.com') / email.send_keys(config.email)
#password.send_keys('*****')  /  password.send_keys(config.password)
#password.submit()


#使用cookies避開登陸動作(add_cookie)
cookie = 'your_cookie=your_cookie ; your_cookie=your_cookie'   #填入cookie
def get_cookies_list(cookie):
    cookie_list = []
    for i in cookie.split(';'):
        name, value = i.strip().split('=', 1)
        i_dict = {'name': name,'value':value}
        cookie_list.append(i_dict)
    return cookie_list

cookie_list = get_cookies_list(cookie)

for c in cookie_list:
    chrome.add_cookie(c)


#等待加載後前往粉絲專頁
time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

#關閉聊天室窗
try:
    chat_close_btn = chrome.find_element(By.CSS_SELECTOR, 'div[aria-label="關閉聊天"]')
    chat_close_btn.click()
except:
    pass

#操作JavaScript向下滾動頁面,等待加載
for x in range(1, 6):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    
#用BeautifulSoup解析動態延遲加載網頁
soup = BeautifulSoup(chrome.page_source, 'html.parser')

#爬取資料
titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve'})
 
for title in titles:
 
    post = title.find('span', {'dir': 'auto'})
 
    if post:
        print(post.getText())

chrome.quit()