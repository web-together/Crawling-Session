from selenium import webdriver
import time
from bs4 import BeautifulSoup
from idpw import lion_id, lion_pw

executable_path = 'C:\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(executable_path=executable_path, options=options)

url = 'https://class.likelion.org/accounts/login/?next=/board/notices/'
driver.get(url)
time.sleep(3) # 웹 페이지 로드를 보장하기 위해 3초 쉬기

# 값 보내기
driver.find_element_by_name('username').send_keys(lion_id)
driver.find_element_by_name('password').send_keys(lion_pw)

# 버튼 누르기
driver.find_element_by_class_name('LoginButton').click()
#driver.quit()