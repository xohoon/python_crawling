from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://search.naver.com/search.naver?&where=news&query=%EC%9E%A5%EC%95%A0%EC%9D%B8%20%EC%B7%A8%EC%97%85&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=59&start=1&refresh_start=0")
soup = BeautifulSoup(html, "html.parser")
title = soup.findAll("a", {"class":"_sp_each_url _sp_each_title"})
title_list = []
for link in title:
    title_list.append(link.text.strip())
data = pd.DataFrame(title_list)
data.head()
data.to_csv('test05.csv', encoding='utf-8-sig')
