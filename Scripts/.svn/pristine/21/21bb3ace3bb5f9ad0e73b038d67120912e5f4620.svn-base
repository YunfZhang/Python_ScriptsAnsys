import requests
import re


from bs4 import BeautifulSoup
#以上作为基本引用


##https://blog.csdn.net/dyboy2017
##https://github.com/dyboy2017/novel_spider


def getContent(content_url,i):
    i=i+1
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res = requests.get(content_url,headers = header,timeout = 10)
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('.jieqi_title')[0].text.lstrip('章 节目录 ')
    content = soup.select('#content')[0].text.lstrip('style5();').rstrip('style6();')
    both = title + content
    next_url = soup.select('.next')[0]['href']
    print(both,file = f)
    print(i)
    return getContent(next_url,i)


#MAIN
f = open("dldl2.txt", 'w+',encoding='utf-8')
i=0
getContent('http://www.quanshuwang.com/book/44/44683/15379609.html',i)
f.close()
print('ok!')