from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import urllib.parse
import requests
import bs4

def webSearching(keyword, site_name, max_page, win_addaress):
    int(max_page)
    now = datetime.today().strftime("%Y%m%d")
    now_over = datetime.today().strftime("%H%M%S")
    page = int(1)
    url_keyword = urllib.parse.quote(keyword)
    url_n = 'https://search.naver.com/search.naver?query='+url_keyword+'&where=news&ie=utf8&sm=nws_hty'
    url_d = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q={}'
    # naver
    if(site_name == 'NAVER'):
        while page < max_page:
            html_n = urlopen(url_n)
            soup = BeautifulSoup(html_n, "html.parser")
            title_list_n = []
            link_list_n = []
            title = soup.findAll('a', {'class':'_sp_each_title'})
            for n in title:
                title_list_n.append(n.text.strip())
                link_list_n.append(n.get('href'))
            page=page+1
        data_n = pd.DataFrame(title_list_n, link_list_n)
        fileName = keyword+' 네이버 검색결과('+str(now)+')'+now_over+'.csv'
        data_n.to_csv(win_addaress+'/'+fileName, encoding='utf-8-sig')

    # daum
    if(site_name == 'DAUM'):
        while page < max_page:
            real_url = url_d.format(keyword)
            news = requests.get(real_url)
            news_bs = bs4.BeautifulSoup(news.content, 'html.parser')
            title_list_d = []
            link_list_d = []
            title = news_bs.findAll('a', {'class':'f_link_b'})
            for d in title:
                title_list_d.append(d.text.strip())
                link_list_d.append(d.get('href'))
            page=page+1
        data_d = pd.DataFrame(title_list_d, link_list_d)
        fileName = keyword+' 다음 검색결과('+str(now)+')'+now_over+'.csv'
        data_d.to_csv(win_addaress+'/'+fileName, encoding='utf-8-sig')
