from selenium import webdriver
import time
import json,os,csv

class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        # print("li_list",li_list)
        content_list = []
        for li in li_list:
            item = {}
            item["home_img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']//img").get_attribute("src")
            item["home_Title"] = li.find_element_by_xpath(".//div[@class='DyListCover-info']/h3").get_attribute("title")
            item["home_TitleType"] = li.find_element_by_xpath(".//div[@class='DyListCover-info']/span").text
            # item["home_TitleOne"] = li.find_element_by_xpath(".//div[@class='DyListCover-info']/h3").text
            DyListCoverHotNum = li.find_elements_by_xpath(".//div[@class='DyListCover-info']")[1]
            item["home_hotNum"] = DyListCoverHotNum.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
            item["home_userName"] = DyListCoverHotNum.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
            # item["home_wrapLabel"] = li.find_element_by_xpath(".//span[@class='HeaderCell-label-wrap']").text
            # print("item",item)
            content_list.append(item)
            #获取下一页的元素
            next_url = self.driver.find_element_by_xpath("//li[@class=' dy-Pagination-next']")
                # if len(next_url)>0 else None
            # print("next_url",next_url)
        return content_list,next_url


    def save_content_list_json(self,pageNum,itemDict):
        # with open(path, "w", encoding='utf-8') as f:
        #  f.write(json.dumps(itemDict, ensure_ascii=False, indent=4))
        file_name = 'douyuAll{}页'.format(pageNum)
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
        content_list,next_url = self.get_content_list()
        pageNum = 1
        for content in content_list:
          self.save_content_list_json(pageNum, content)

        while pageNum <3:
            print(pageNum)
            next_url.click()
            pageNum = pageNum+1
            time.sleep(2)
            content_list, next_url = self.get_content_list()
            for content in content_list:
                self.save_content_list_json(pageNum, content)

if __name__ == '__main__':
    doubanSpider = DouyuSpider()
    doubanSpider.run()
