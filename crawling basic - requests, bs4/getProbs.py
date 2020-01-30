import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.acmicpc.net/problem/tags').text

print(response)

# request.get(응답받고싶은url)					>> 응답 객체
# request.get(응답받고싶은url).ok				>> 써도 되는지 안되는지
# request.get(응답받고싶은url).status_code	    >> 응답 상태코드
# request.get(응답받고싶은url).content		    >> 응답받은 날것의 데이터들
# request.get(응답받고싶은url).text			    >> 응답받은 문자형식의 데이터들

soup = BeautifulSoup(response, 'html.parser')

tags = soup.select('.table-responsive tbody tr a[href*=problem]')

for x in tags:
    print(x.text)
