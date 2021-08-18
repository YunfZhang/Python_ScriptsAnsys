import threading
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import socket

#设置超时时间
socket.setdefaulttimeout(10) 

def getHTMLData(strURL):
    try:
        data = urllib.request.urlopen(strURL).read()
        return data
    except:
        print('i get the error')
        data = urllib.request.urlopen(strURL).read()
        return data

def getDataOnMatch(data, name, att, match):
    soup = BeautifulSoup(data,"html.parser")
    result = soup.find_all(name, att)
    if match !="":
        re_pat = re.compile(match)
        list = re_pat.findall(str(result))
        return list 
    return result

#保存小说信息
class ListBookInfo:
    def __init__(self):
        self.lock = threading.Lock()
        self.nLsBookCnt = 0
        self.lsBookInfo = []
      
    def AddBookInfo(self, strBookName, strBookURL):
        self.lock.acquire()
        obj = []
        obj.append(strBookName)
        obj.append(strBookURL)
        self.lsBookInfo.append(obj)
        self.nLsBookCnt += 1
        self.lock.release()
        
    def GetHeadBookInfo(self):
        self.lock.acquire()
        if self.nLsBookCnt > 0:
            bookInfo = self.lsBookInfo[0]
            del self.lsBookInfo[0]
            self.nLsBookCnt -= 1
            self.lock.release()
            return bookInfo
        else:
            self.lock.release()
            return 0
        
    def GetSize(self):
        self.lock.acquire()
        nSize = self.nLsBookCnt
        self.lock.release()
        return nSize
        
    def ClearLsBook(self):
        self.lock.acquire()
        self.lsBookInfo.clear()
        self.nLsBookCnt = 0
        self.lock.release()

#保存小说名、小说章节信息（章节名、章节URL）        
class BookPageInfo:
    def __init__(self):
        self.lock = threading.Lock()
        self.nBookPageCnt = 0
        self.lsBookPageInfo = []
      
    def AddBookPageInfo(self, strBookName, lsBookPageURL):
        self.lock.acquire()
        obj = []
        obj.append(strBookName)
        obj.append(lsBookPageURL)
        self.lsBookPageInfo.append(obj)
        self.nBookPageCnt += 1
        self.lock.release()
        
    def GetHeadBookPageInfo(self):
        self.lock.acquire()
        if self.nBookPageCnt > 0:
            bookInfo = self.lsBookPageInfo[0]
            del self.lsBookPageInfo[0]
            self.nBookPageCnt -= 1
            self.lock.release()
            return bookInfo
        else:
            self.lock.release()
            return 0
    
    def GetSize(self):
        self.lock.acquire()
        nSize = self.nBookPageCnt
        self.lock.release()
        return nSize
        
    def ClearLsBookPage(self):
        self.lock.acquire()
        self.lsBookPageInfo.clear()
        self.nBookPageCnt = 0
        self.lock.release()
        
def getArticleType(data):
    soup = BeautifulSoup(data)
    data_ul = soup.find_all("ul", "channel-nav-list")
    print(data_ul)
    re_pat = re.compile('\<a href=\"(.*?)\"\>(.*)\<\/a\>') 
    list = re_pat.findall(str(data_ul))
    print(list)
    for i in list:
        print("%s-->%s" % (i[1], i[0]))
    return list

def getArticle(strURL):
    data = getHTMLData(strURL)
    print(data)
    ll = getDataOnMatch(data, "ul", "seeWell cf", "\<li\>(.*?)href=\"(.*?)\"(.*?)\<\/li\>")
    list = []
    for i in ll:
        obj = []
        listReData = getDataOnMatch(getHTMLData(i[1]),"section","main b-detail", "(.*?)href=\"(.*?)\"(.*?)")
        obj.append(listReData[0][1])
        lf = re.findall("(.*?)alt=\"(.*?)\"(.*?)", i[2])    
        obj.append(lf[0][1])
        list.append(obj)
    return list

def getArticlePageContent(strURL):
    data = getHTMLData(strURL)
    InfoList = getDataOnMatch(data, "div", "clearfix dirconone", "\<li\>(.*?)href=\"(.*?)\" title=\"(.*?)\"(.*?)\<\/li\>")
    pageInfoList = []
    for i  in InfoList:
        obj = []
        obj.append(strURL + '/' + i[1])
        obj.append(i[2])
        pageInfoList.append(obj)
    return pageInfoList

def getArticleContent(strURL):
    try:
        data = getHTMLData(strURL)
        ll = getDataOnMatch(data, "div", "mainContenr", "")
        return ll
    except:
        print('i get the error')
        data = getHTMLData(strURL)
        ll = getDataOnMatch(data, "div", "mainContenr", "")
        return ll

class CleverBookSys:
    
    def __init__(self):
        self.bExit = 0
        self.eventBook = threading.Event()
        self.eventPage = threading.Event()
        self.lsBookInfo = ListBookInfo()
        self.lsBookPageInfo = BookPageInfo()
        self.thrParseBook = ThreadForParseAllBook(self, "ThreadForParseAllBook")
        self.thrParseBookPage = ThreadForParseBookPage(self, "ThreadForParseBookPage")
        nCount = 0
        self.thrDownLoad = []
        #开十个线程用于下载，视网速而定
        while nCount < 10:         
            thread = ThreadForDownloadTxt(self,"ThreadForDownloadTxt",nCount)
            thread.start()
            self.thrDownLoad.append(thread)
            nCount += 1
        self.thrParseBook.start()
        self.thrParseBookPage.start()
        
#用与抓取整个网站的小说名及URL（没写完、大概写了一些）
class ThreadForParseAllBook(threading.Thread):
    
    def __init__(self, parent, strThrName):
        threading.Thread.__init__(self) 
        self.parent = parent
        self.strThrName = strThrName
        #这里只针对这个网站的解析
        self.lsArticle = getArticleType(getHTMLData("http://www.quanshuwang.com/"))
        
    def run(self):
        print("Thread %s is Start!!!" % (self.strThrName))
        for art in self.lsArticle:
            bookInfoList = getArticle(art[0])
            #【0】：小说路径，[1]：小说名
            for bookInfo in bookInfoList:
                self.parent.lsBookInfo.AddBookInfo(bookInfo[1], bookInfo[0])
            self.parent.eventBook.set()
            
#用于抓取单本小说的所以章节名及URL                
class ThreadForParseBookPage(threading.Thread):
    
    def __init__(self, parent, strThrName):
        threading.Thread.__init__(self) 
        self.parent = parent
        self.strThrName = strThrName
        
    def run(self):
        print("Thread %s is Start!!!" % (self.strThrName))
        while self.parent.bExit == 0:
            nSize = self.parent.lsBookInfo.GetSize() 
            print("ThreadForParseBookPage-->%d" % nSize)
            if (nSize > 0):
                bookInfo = self.parent.lsBookInfo.GetHeadBookInfo()
                print("ThreadForParseBookPage->%s" % bookInfo)
                PageInfo = getArticlePageContent(bookInfo[1])
                print("ThreadForParseBookPage2->%s" % PageInfo)
                self.parent.lsBookPageInfo.AddBookPageInfo(bookInfo[0], PageInfo)
                self.parent.eventPage.set()
            else:
                print("self.parent.eventBook.wait()")
                self.parent.eventBook.wait()
                if(nSize <= 0):
                    self.parent.eventBook.clear()
                print("self.parent.eventBook.run()")
                
#用于抓取单小说的所有章节内容并生成TXT文档保存                
class ThreadForDownloadTxt(threading.Thread):
    
    def __init__(self, parent, strThrName, nThrNO):
        threading.Thread.__init__(self) 
        self.parent = parent
        self.strThrName = strThrName
        self.nThrNO = nThrNO
        
    def run(self):
        print("Thread %s%d is Start!!!" % (self.strThrName,self.nThrNO))
        while self.parent.bExit == 0:
            nSize = self.parent.lsBookPageInfo.GetSize()
            print("ThreadForDownloadTxt-->%d" % nSize)
            if (nSize > 0):
                bookPageInfoList = self.parent.lsBookPageInfo.GetHeadBookPageInfo()
                print("ThreadForDownloadTxt%d-->%s" % (self.nThrNO,bookPageInfoList))
                fileName = 'D:\\txt\\' + bookPageInfoList[0] + '.txt'
                file_object = open(fileName, 'w',encoding='utf-8')
                for pageInfo in bookPageInfoList[1]:
                        print("ThreadForDownloadTxt%d-->%s" % (self.nThrNO,pageInfo))
                        content = getArticleContent(pageInfo[0])
                        print(content)
                        file_object.write(pageInfo[1])
                        file_object.write(str(content))
                        file_object.flush()
                file_object.close()
            else:
                print("self.parent.eventPage.wait()")
                self.parent.eventPage.wait()
                if(nSize <= 0):
                    self.parent.eventPage.clear()
                print("self.parent.eventPage.run()")

cleverBook =  CleverBookSys()