
from urllib import request,parse
from bs4 import BeautifulSoup
import time
import os
import random

SLEEPTIME = random.randrange(3,9)


def search_book(bookname):
    url = 'http://www.biquge5200.com/modules/article/search.php?searchkey=' + parse.quote(bookname)
    response = request.urlopen(url)
    content = response.read().decode('gbk')
    # content = response.read().decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    menu = []
    key = 0
    for row in soup.find('table').find_all('tr'):
        td1 = row.select('td:nth-of-type(1)')
        td3 = row.select('td:nth-of-type(3)')
        if(td1 and td3):
            name    = td1[0].find('a').string
            href    = td1[0].find('a').get('href')
            author  = td3[0].string
            menu.append({'name':name,'href':href})
            print(str(key) + ' 书名：' + name + ' >> 作者：' + author)
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
    content = response.read().decode('gbk', "ignore")
    # content = response.read().decode('ISO-8859-1')
    with open ('a.html', 'wb') as fmenu:
        fmenu.write(content.encode('gbk'))
    soup = BeautifulSoup(content, 'html.parser')
    list = []
    for dd in soup.find('div',id="list").find('dt').find_next('dt').find_all_next('dd'):
        title = dd.find('a').string
        href = dd.find('a').get('href')
        list.append({'title':title,'href':href})
    return list

def get_novel_content(title,url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    proxy_list = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    px = request.ProxyHandler(proxies)
    opener = request.build_opener(px)
    
    # response = request.urlopen(request.Request(url,headers=headers))
    response = opener.open(request.Request(url,headers=headers))
    content = response.read().decode('gbk')
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.find('div',id="content").get_text()
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


