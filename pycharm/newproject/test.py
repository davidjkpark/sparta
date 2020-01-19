import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

for i in (soup.select("#old_content > table > tbody > tr")) :
    # print(i.find("div", class_="tit5"))
    # print(i)
    # print(i.select_one("td.title > div > a"))
    if i.select_one("td.title > div > a") is not None :
        print(i.select_one("td.title > div > a").text)
