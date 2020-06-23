from selenium import webdriver
import time
import json,os
import requests
from retrying import retry
from bs4 import BeautifulSoup

class DouyuSpider:
    def __init__(self):
        self.start_url = "http://www.zjcampus.com/event?page=5"
        self.driver = webdriver.Chrome()
        self.content_list_detail = []

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='am-avg-sm-1 am-avg-md-1 am-avg-lg-3']//li")
        # print("li_list",li_list)
        content_list = []
        for li in li_list:
            item = {}
            itemContent = li.find_elements_by_xpath(".//div[@class='info am-gallery-overlay']//p")
            item["home_Img"] = li.find_element_by_xpath(".//div[@class='info am-gallery-overlay']//img").get_attribute("src")
            item["home_peopleNum"] = itemContent[0].find_elements_by_xpath(".//span")[0].text
            item["home_perice"] = itemContent[0].find_element_by_xpath(".//span[@class='am-text-warning']").text
            item["home_Address"] = itemContent[1].text
            item["home_WorkTime"] = itemContent[2].text
            item["home_Join"] = itemContent[3].text
            item["home_activityStatus"] = li.find_elements_by_xpath(".//div[@class='info am-gallery-overlay']//a")[1].text
            item["home_moreLink"] = li.find_elements_by_xpath(".//div[@class='info am-gallery-overlay']//a")[
                1].get_attribute('href')


            print("item",item)
            content_list.append(item)
        return content_list


    def save_content_list_json(self,pageNum,itemDict):
        # with open(path, "w", encoding='utf-8') as f:
        #  f.write(json.dumps(itemDict, ensure_ascii=False, indent=4))
        file_name = 'partJob{}页'.format(pageNum)
        item = json.dumps(itemDict,ensure_ascii=False,indent=4)
        try:
            if not os.path.exists(file_name):
                with open(file_name,"w",encoding='utf-8') as f:
                    f.write(item + ",\n")
                    # print("write success")

            else:
                 with open(file_name,"a",encoding='utf-8') as f:
                       f.write(item +",\n")
                       # print("write success")
        except Exception as e :
            print("write error==>",e)

    def get_contentDetail_list(self,content,content_list_detail):
            bs_data = BeautifulSoup(content.text, 'html.parser')
            itemOne = {}
            itemOne["Work_One"] = (bs_data.find_all('p')[1].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_Two"] = (bs_data.find_all('p')[2].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_Three"] = (bs_data.find_all('p')[3].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_Five"] = (bs_data.find_all('p')[4].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_Six"] = (bs_data.find_all('p')[5].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_Seven"] = (bs_data.find_all('p')[6].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_eight"] = (bs_data.find_all('p')[7].text).replace('\n', '').replace('\r', '').replace('\t', '')
            itemOne["Work_nine"] = (bs_data.find_all('p')[8].text).replace('\n', '').replace('\r', '').replace('\t', '')
            print("item",itemOne)
            content_list_detail.append(itemOne)
            return content_list_detail

    def save_content_list_detail_json(self,pageNum,itemDict):
        # with open(path, "w", encoding='utf-8') as f:
        #  f.write(json.dumps(itemDict, ensure_ascii=False, indent=4))
        file_name = 'partJobDetail{}页'.format(pageNum)
        item = json.dumps(itemDict,ensure_ascii=False,indent=4)
        try:
            if not os.path.exists(file_name):
                with open(file_name,"w",encoding='utf-8') as f:
                    f.write(item + ",\n")
                    # print("write success")

            else:
                 with open(file_name,"a",encoding='utf-8') as f:
                       f.write(item +",\n")
                       # print("write success")
        except Exception as e :
            print("write error==>",e)

    def run(self):
        self.driver.get(self.start_url)
        time.sleep(2)
        content_list = self.get_content_list()
        pageNum = 1
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
        content_list_detail = []
        for content in content_list:
          self.save_content_list_json(pageNum, content)
          # print(content["home_moreLink"])

          response = requests.get(content["home_moreLink"], headers=headers, timeout=3)
          self.get_contentDetail_list(response,content_list_detail)

        for content_detail in content_list_detail:
            self.save_content_list_detail_json(pageNum, content_detail)


if __name__ == '__main__':
    doubanSpider = DouyuSpider()
    doubanSpider.run()
