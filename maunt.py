import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/group/topic/15792897/'

r = requests.get(url).text
soup = BeautifulSoup(r,'lxml')
textlist = soup.select('div#link-report div.topic-content p')
print(textlist)

with open('maunt.txt','w',encoding='utf-8') as f:
    txt = textlist[0].text
    txt = re.sub(r'\<br\>',r'\n',txt,flags=re.M)
    f.write(txt)