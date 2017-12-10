#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import lxml
import json
import thread

url_store = {
        "mouse" : "http://prod.danawa.com/list/?cate=112787",
        "monitor" : "http://prod.danawa.com/list/?cate=112757",
        "ODD" : "http://prod.danawa.com/list/?cate=112772",
        "RAM" : "http://prod.danawa.com/list/?cate=112752",
        "CPU" : "http://prod.danawa.com/list/?cate=112747",
        "SSD" : "http://prod.danawa.com/list/?cate=112760",
        "HDD" : "http://prod.danawa.com/list/?cate=112763",
        "GPU" : "http://prod.danawa.com/list/?cate=112753",
        "keyboard" : "http://prod.danawa.com/list/?cate=112782",
        "mainboard" : "http://prod.danawa.com/list/?cate=112751"
}

class Crawler():
    def __init__(self):
        self.url_store = url_store
        self.browser = webdriver.PhantomJS('./phantomjs')
        #self.browser = webdriver.Chrome('./chromedriver')

    def getInfo(self, url, minPrice, maxPrice, memo):
        self.browser.get(url)

        browser.find_element_by_name("priceRangeMinPrice").send_keys(minPrice)
        browser.find_element_by_name("priceRangeMaxPrice").send_keys(maxPrice)
        browser.find_element_by_class_name("btn_search").click()
        #sleep before pressing enter
        a = input("Press Enter\n")
        print(a)

    def getInfoByText(self, url, minPrice, maxPrice, memo):
        ret_json = {
                "product": [],
                "price" : []
        }
        self.browser.ignoreSynchronization = True
        self.browser.get(url)
        #print(url)
        self.browser.ignoreSynchronization = False
        #print(browser.page_source)
        self.browser.find_element_by_name("priceRangeMinPrice").send_keys(minPrice)
        self.browser.find_element_by_name("priceRangeMaxPrice").send_keys(maxPrice)
        self.browser.find_element_by_class_name("btn_search").click()
        self.browser.implicitly_wait(1)
        print("finish loading the page...\n")
        product_list = self.browser.find_elements_by_name("productName")
        
        p_name = ""
        p_price = 0
        for n, product in enumerate(product_list):
            p_name = product.text
            break
        #price_list = browser.find_elements_by_class_name("prod_pricelist")
        #for n, price in enumerate(price_list): 
        #    p_price = price.text
        #    break
            #ret_json["price"].append(int(price.text))
        #print( p_name + " " + p_price)
        print(p_name)
        return p_name
    def getInfoByTextMT(self, url, minPrice, maxPrice, memo):
        #TODO: make getInfoByText with multithread
        #thread.start_new_thread(self.getInfoByText, (self.url_store["CPU"], 0, 100000, "cpu", ) )
        self.getInfoByText(url_store["mouse"], 15000, 100000, "call the cpu")
            #thread.start_new_thread(getInfoByText, (self.url_store["mouse"], 0, 100000, "cpu", ) )
            #thread.start_new_thread(getInfoByText, (self.url_store["keyboard"], 0, 100000, "cpu", ) )
            #thread.start_new_thread(getInfoByText, (self.url_store["RAM"], 0, 100000, "cpu", ) )
            #thread.start_new_thread(getInfoByText, (self.url_store["GPU"], 0, 100000, "cpu", ) )

if __name__ == "__main__":
    url_store = url_store
    user = Crawler()
    user.getInfoByText(url_store["mouse"], 15000, 100000, "call the cpu")
    user.getInfoByText(url_store["keyboard"], 15000, 100000, "call the cpu")
    user.getInfoByText(url_store["mainboard"], 15000, 100000, "call the cpu")
    #user.getInfo(url_store["CPU"], 300000, 450000, "call the cpu")
    #user.getInfoByTextMT(url_store["CPU"], 300000, 450000, "call the cpu")

"""
## id, pw
browser.find_element_by_name('userid').send_keys(input("ID: "))
browser.find_element_by_name('password').send_keys(input("PW: "))
browser.find_element_by_name("btn_login").submit()
## enter the ccp course
subject = input("subject : ")
ccp_url = browser.find_element_by_partial_link_text(subject).get_attribute('href')
browser.get(ccp_url)
## click 공지사항
browser.find_element_by_partial_link_text('공지사항').click()
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
notices = soup.select("strong > ")

## crawl the list on the board.
today = date.today().isoformat()
today = "2017-03-01"
title_of_list = ""
contents = ""
index_of_title=1
for index, n in enumerate(notices):
    if index % 6 == 2: # title
        title_of_list = n.text.strip()
    elif index % 6 == 4 and today == n.text.strip():  # date
        contents += title_of_list+"\n"
        title_of_list = title_of_list + " " + today
        print(str(index_of_title)+". "+title_of_list)
        index_of_title+=1
        title_of_list = ""
print("="*50)

##print the contents that are updated on today.
for index, n in enumerate(iter(contents.splitlines())):
    browser.find_element_by_partial_link_text(n).click()
    print(str(index+1)+". ")
    print(browser.find_element_by_class_name('text_to_html').text)
    print("\n\n"+"-"*50)
    browser.back()

# 네이버 사이트 로그인
driver = webdriver.Chrome('./chromedriver')
#approach to the url
driver.get('https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fwww.naver.com')

#input the information
driver.find_element_by_name('id').send_keys(input("ID: "))
driver.find_element_by_name('pw').send_keys(input("PW: "))

#click the login button
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
#go to the naver music site
driver.implicitly_wait(10)
driver.get('http://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h')
driver.implicitly_wait(5)


#driver.find_element_by_xpath('//tr[@class="_tracklist_move _track_dsc list1 on"][1]/td[@class="buy"]/a[1]').click()
#driver.set_script_timeout(3)
#driver.find_element_by_xpath('//tr[@class="_tracklist_move _track_dsc list1 on"][1]/td[@class="buy"]/div[@class="_buy_layer buy_layer"]/ul/li[1]/a/strong').click()
driver.find_element_by_link_text('MP3구매').click()
"""
