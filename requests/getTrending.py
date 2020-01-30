import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.daum.net/').text

soup = BeautifulSoup(res,'html.parser')

for li in soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li'):
    rank = li.select_one('span').text
    search_word = li.select_one('span[class="txt_issue"]').text
    print(rank,search_word)

