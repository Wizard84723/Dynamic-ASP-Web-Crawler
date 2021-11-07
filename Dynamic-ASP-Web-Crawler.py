import re
import requests
from bs4 import BeautifulSoup
import urllib
import time
import sys
path = 'output.txt'
f = open(path, 'w')
start = "https://school.tn.edu.tw/default.aspx"
r = requests.get(start, timeout=3)
r.encoding = 'UTF8'
soup = BeautifulSoup(r.text, 'lxml')
a_tags = soup.find(id='ctl00_ContentPlaceHolder1_Panel_sch').find_all('a', href=True)
for tag in a_tags:
    url = tag.get('href')
    if 'http' in url:
        f.write(url+"\n")
VIEWSTATEGENERATOR  = soup.find('input',{'id':'__VIEWSTATEGENERATOR'}).get('value')
VIEWSTATE = soup.find('input',{'id':'__VIEWSTATE'}).get('value')
EVENTVALIDATION = soup.find('input',{'id':'__EVENTVALIDATION'}).get('value')
for i in range(2,29):#29
    PAGE = "Page$"+str(i)
    data = {
            'ctl00$ContentBody$chkAll': None,
            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$GridV_schByarea",
            "__EVENTARGUMENT": PAGE,
            "__LASTFOCUS": "",
            "__VIEWSTATE":VIEWSTATE,
            "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
            "__VIEWSTATEENCRYPTED": "",
            "__EVENTVALIDATION": EVENTVALIDATION
        }
    res = requests.post(start,data=data)#.content.decode('utf8')
    res.encoding = 'UTF8'
    soup2 = BeautifulSoup(res.text, 'lxml')
    VIEWSTATEGENERATOR = soup2.find('input', {'id': '__VIEWSTATEGENERATOR'}).get('value')
    VIEWSTATE = soup2.find('input', {'id': '__VIEWSTATE'}).get('value')
    EVENTVALIDATION = soup2.find('input', {'id': '__EVENTVALIDATION'}).get('value')
    a_tags = soup2.find(id='ctl00_ContentPlaceHolder1_Panel_sch').find_all('a', href=True)
    for tag in a_tags:
        url = tag.get('href')
        if 'http' in url:
            f.write(url+"\n")
sys.exit()


# javascript:__doPostBack('ctl00$ContentPlaceHolder1$GridV_schByarea','Page$2')
