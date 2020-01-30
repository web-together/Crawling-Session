from selenium import webdriver
import time
from bs4 import BeautifulSoup
from idpw import naver_id, naver_pw

executable_path = 'C:\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(executable_path=executable_path, options=options)

url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)
time.sleep(3) # 웹 페이지 로드를 보장하기 위해 3초 쉬기

# 값 보내기
driver.find_element_by_name('id').send_keys(naver_id)
driver.find_element_by_name('pw').send_keys(naver_pw)

# 버튼 누르기
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
#driver.quit()