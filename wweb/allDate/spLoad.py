#搜尋物品，頁數
from selenium import webdriver #自動瀏覽器
from selenium.webdriver.chrome.options import Options   #防止跳窗
import time
from bs4 import BeautifulSoup

from ..models import ssp 

def sp_(name,page):
    options = Options()
    options.add_argument("--disable-notificatoins")   
    chrome = webdriver.Chrome('./driverpath',chrome_options=options)   
    Page=1  #翻頁
    page = int(page)    #外部帶入
    
    for i in range(page):
        name = name
        chrome.get("https://shopee.tw/search?keyword={}&page={}".format(name,Page))
        Page += 1
        count = 500
        for i in range(4):#捲動次數
            chrome.execute_script("window.scrollTo(0,{})".format(count))
            time.sleep(2)
            count += 300
        data = BeautifulSoup(chrome.page_source,"html.parser")
        content = data.find_all(class_='VTjd7p whIxGK')

        for i in content:
            sname = i.find('img').get('alt')
            #print(name)        
            png = i.find('img').get('src')
            #print(png)
            price = i.find(class_ = 'vioxXd rVLWG6')
            pic = price.find('span',class_='ZEgDH9').text
            #print(pic)
            #print()
            if(sname != None and png != None and pic != None):
                Ssp = ssp.objects.create(sname=sname,spic=pic,spng=png)
                Ssp.save()

    context = ssp.objects.all()
    return context