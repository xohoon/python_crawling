from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import urllib.parse
import requests
import bs4

keyword = '고용부담금'
url_keyword = urllib.parse.quote(keyword)
page=1
url_n = 'https://search.naver.com/search.naver?query='+url_keyword+'&where=news&ie=utf8&sm=nws_hty'
# url_d = 'https://news.daum.net/'
# url_d = 'https://search.daum.net/search?w=news&sort=recency&q='+url_keyword+'&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period='


# for i in range(1, page+1):
#     # url_d = 'https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period='
#     # url_d = 'https://search.daum.net/search?w=news&sort=recency&q={}&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p={}&rc=1&at=more&sd=&ed=&period='
#     real_url = url_d.format(keyword, i)
#     news = requests.get(real_url)
#     news_bs = bs4.BeautifulSoup(news.content, 'html.parser')
#     newsList = news_bs.findAll('a', {'class':'f_link_b'})
#     title_list = []
#     link_list = []
#     for d in newsList:
#         title_list.append(d.text.strip())
#         link_list.append(d.get('href'))
# print(title_list)
# print('123123121')
# print(link_list)


html = urlopen(url_n)
soup = BeautifulSoup(html, "html.parser")
title = soup.findAll('a', {'class':'_sp_each_title'})

title_list = []
link_list = []
for d in title:
    title_list.append(d.text.strip())
    link_list.append(d.get('href'))
data_n = pd.DataFrame(link_list, title_list)
print(data_n)

# # 실시간 이슈 검색어만 추출
# searchword_list = []
# for elem in elem_list:
#     searchword_list.append(elem.get_text())
  
# # 결과 확인
# for searchword in searchword_list:
#     print(searchword)




# for link in title:
#     title_list.append(link.text.strip())
#     link_list.append(link.get('href'))
    
#     print(link_list)
#     print(title_list)
    



# def webSearching(keyword, site_name, max_page):
#     int(max_page)
#     now = datetime.today().strftime("%Y%m%d")
#     # now = datetime.today().strftime("%Y%m%d%H%M%S")
#     page = int(1)
#     url_keyword = urllib.parse.quote(keyword)
#     naver_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+url_keyword
#     daum_url = 'ttps://search.daum.net/search?w=tot&DA=23A&rtmaxcoll=NNS&q='+url_keyword
#     while page < max_page:
#         html = urlopen(naver_url)
#         soup = BeautifulSoup(html, "html.parser")
#         title_list_n = []
#         link_list_n = []
#         title_n = soup.findAll('a', {'class':'_sp_each_url _sp_each_title'})
#         for link in title_n:
#             title_list_n.append(link.text.strip())
#             link_list_n.append(link.get('href'))

#         html = urlopen(daum_url)
#         title_list_d = []
#         link_list_d = []
#         title_d = soup.findAll('a', {'class':'f_link_b'})
#         for link in title_d:
#             title_list_d.append(link.text.strip())
#             link_list_d.append(link.get('href'))
#         page=page+1
    

#     data = pd.DataFrame(title_list_n, link_list_n)
#     fileName = keyword+' 네이버 검색결과'+str(now)+'test03.csv'
#     data.to_csv(fileName, encoding='utf-8-sig')
    
#     data_d = pd.DataFrame(title_list_d, link_list_d)
#     fileName = keyword+' 다음 검색결과'+str(now)+'text01.csv'
#     data.to_csv(fileName, encoding='utf-8-sig')