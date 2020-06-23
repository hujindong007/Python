from selenium import webdriver
import time
import json,os

class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.wz169.com/category/xianbao/page/8/"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//main[@id='main']//article")
        # print("li_list",li_list)
        content_list = []
        for li in li_list:
            item = {}
            item["home_Img"] = li.find_element_by_xpath(".//figure[@class='thumbnail']//img").get_attribute("src")
            item["home_Title"] = li.find_element_by_xpath(".//header[@class='entry-header']//a").text
            item["home_Content"] = li.find_element_by_xpath(".//div[@class='archive-content']").text
            item["home_Time"] = li.find_element_by_xpath(".//span[@class='date']").text
            item["home_LookNum"] = li.find_element_by_xpath(".//span[@class='views']").text
            item["home_moreLink"] = li.find_element_by_xpath(".//span[@class='entry-more']/a").get_attribute("href")

            print("item",item)
            content_list.append(item)
        return content_list


    def save_content_list_json(self,pageNum,itemDict):
        # with open(path, "w", encoding='utf-8') as f:
        #  f.write(json.dumps(itemDict, ensure_ascii=False, indent=4))
        file_name = 'Money{}页'.format(pageNum)
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
        for content in content_list:
          self.save_content_list_json(pageNum, content)


if __name__ == '__main__':
    doubanSpider = DouyuSpider()
    doubanSpider.run()
