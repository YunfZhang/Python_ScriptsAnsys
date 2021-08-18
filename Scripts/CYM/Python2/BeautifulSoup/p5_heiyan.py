
from urllib import request,parse
from bs4 import BeautifulSoup
import time
import os
import random

SLEEPTIME = random.randrange(3,9)


def search_book(bookname):
    url = 'http://www.heiyan.org/plus/search.php?kwtype=0&searchtype=&q=' + parse.quote(bookname)
    response = request.urlopen(url)
    content = response.read().decode('gb2312')
    # content = response.read().decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    menu = []
    key = 0
    for item in soup.find_all('div', attrs={"class": "so new"}):
        href = "http://www.heiyan.org" + item.find('h2').find('a').get('href')
        name = item.find('h2').find('a').string
        # author = item.find('div', attrs={"class": "infos"}).find('span').get_text()
        menu.append({'name':name,'href':href})
        author = item.find('div', attrs={"class": "infos"}).find('span').find('a').string
        print(f"{key}: {name} -> {author}")
        key += 1
    if(menu):
        select_key = -1
        while(select_key >= key or select_key < 0):
            if len(menu) == 1:
                select_key = 0
            else:
                select_key = int(input('请输入你要下载的小说序号：'))
        return menu[int(select_key)]
    return []

def get_novel_menu(url):
    response = request.urlopen(url)
    content = response.read().decode('gb2312', "ignore")
    with open ('a.html', 'wb') as fmenu:
        fmenu.write(content.encode('gb2312'))
    soup = BeautifulSoup(content, 'html.parser')
    list = []
    for dd in soup.find('div',class_="book_list").find('ul').find_all('li'):
        title = dd.find('a').string
        href = url + dd.find('a').get('href')
        list.append({'title':title,'href':href})
    return list

def get_novel_content(title,url):
    # headers = {
        # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    # }
    # proxy_list = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
    # proxy_ip = random.choice(proxy_list)
    # proxies = {'http': proxy_ip}
    # px = request.ProxyHandler(proxies)
    # opener = request.build_opener(px)
    
    # response = request.urlopen(request.Request(url,headers=headers))
    # response = opener.open(request.Request(url,headers=headers))
    # content = response.read().decode('gb2312')
    # soup = BeautifulSoup(content, 'html.parser')
    # text = soup.find('div',id="contentbox").get_text()
    # return title + "\r\n" + text
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    # url = "http://www.heiyan.org/daojun/3735220.html"
    response = request.urlopen(request.Request(url,headers=headers))
    content = response.read().decode('gb2312')
    with open("content.txt", "wb") as f:
        f.write(content.encode('gb2312'))
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.find('div',class_="contentbox").get_text()
    return title + "\r\n" + text
    
    

info = [] #type: ignore
while(info == []):
    bookname = input('请输入你要查找的小说名：')
    info = search_book(bookname)
menu_lists = get_novel_menu(info['href']) #type: ignore
if(menu_lists == []):
    print('该小说没有可供下载的目录')
    exit(0)
for list in menu_lists:
    if not os.path.isdir(bookname):
        os.mkdir(bookname) 
    
    txt_name = list['title'].replace("?","_").replace("/","_").replace(":","_").replace("|","_").replace("*","_")
    if os.path.isfile(f'{bookname}/{txt_name}.txt'):
        # print('章节：' + list['title'] + '=======>>>>>已存在！！！')
        pass
    else:
        print('正在下载：' + list['title'])
        content = get_novel_content(list['title'],list['href'])
        # f = open('novel.txt', 'a')
        f = open(f'{bookname}/{txt_name}.txt', 'w')
        f.write(content)
        f.close()
        time.sleep(SLEEPTIME)


