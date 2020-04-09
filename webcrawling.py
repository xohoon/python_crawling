from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import urllib.parse

# html = urlopen("https://search.naver.com/search.naver?&where=news&query=%EC%9E%A5%EC%95%A0%EC%9D%B8%20%EC%B7%A8%EC%97%85&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=59&start=1&refresh_start=0")
# soup = BeautifulSoup(html, "html.parser")
# title = soup.findAll("a", {"class":"_sp_each_url _sp_each_title"})
# title_list = []
# for link in title:
#     title_list.append(link.text.strip())
# data = pd.DataFrame(title_list)
# data.head()
# data.to_csv('test05.csv', encoding='utf-8-sig')


def webSearching(keyword, site_name, max_page):
    int(max_page)
    now = datetime.today().strftime("%Y%m%d")
    # now = datetime.today().strftime("%Y%m%d%H%M%S")
    page = int(1)
    url_keyword = urllib.parse.quote(keyword)
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+url_keyword
    # https://search.naver.com/search.naver?query=%EC%9E%A5%EC%95%A0%EC%9D%B8+%EC%B7%A8%EC%97%85&where=news&ie=utf8&sm=nws_hty
    # https://search.daum.net/search?w=tot&DA=23A&rtmaxcoll=NNS&q=%EC%9E%A5%EC%95%A0%EC%9D%B8+%EC%B7%A8%EC%97%85
    while page < max_page:
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        title_list = []
        link_list = []
        title = soup.findAll('a', {'class':'_sp_each_url _sp_each_title'})
        for link in title:
            title_list.append(link.text.strip())
            link_list.append(link.get('href'))
        page=page+1
    

    data = pd.DataFrame(title_list, link_list)
    fileName = keyword+' '+site_name+'검색결과'+str(now)+'test03.csv'
    print(str(now))
    print(fileName)
    data.to_csv(fileName, encoding='utf-8-sig')