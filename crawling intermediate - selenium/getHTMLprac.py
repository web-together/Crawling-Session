from selenium import webdriver
import time
from bs4 import BeautifulSoup

executable_path = 'C:\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions() 
#options.add_argument('--headless') #headless 모드 (창 띄우지 않고 웹 브라우저 실행 시키기) 
driver = webdriver.Chrome(executable_path=executable_path, options=options)

url = 'https://www.acmicpc.net/problem/tags'
driver.get(url)
time.sleep(3) # 웹 페이지 로드를 보장하기 위해 3초 쉬기
text = driver.page_source
#print(text)

soup = BeautifulSoup(text, 'html.parser')

for li in soup.select('.table-responsive tbody tr a[href*=problem]'):
    print(li.text)

#driver.quit()