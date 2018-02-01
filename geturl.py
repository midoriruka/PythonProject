# -*- coding: UTF-8 -*-
# author : sijt

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html=requests.get('https://chenqingyun.github.io/')
    html.encoding='utf-8'
    soup = BeautifulSoup(str(html.text),'html.parser')
    if len(soup.select('.post-body')) > 0:
    	txt = soup.select('.post-body')[0].text
    	with open('G:\python\PythonProject\chenqingyun.txt','w') as f:
    		f.write(txt)
    	print('获取数据成功')
