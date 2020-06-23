import json
import requests
from parse_url import parse_url


# https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=综艺&start=0
class doubanName:
    def __init__(self,tagName):
        self.tagName = tagName
        self.url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=' + tagName + '&start={}'
        # self.url = 'https://movie.douban.com/j/new_search_subjects?range=0,10&tags=' + tagName + '&start={}'
        # self.url = 'https://movie.douban.com/j/new_search_subjects?tags='+tagName+'&start={}'#没有评分 会缺失
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}


    def get_list_url(self):
        return [self.url.format(i*20) for i in range(5)]

    def save_json(self,pythonJson,pageNum):
        file_name = '{}排行榜第{}页'.format(self.tagName,pageNum)
        with open(file_name,'w',encoding='utf-8') as f :
            f.write(json.dumps(pythonJson,ensure_ascii=False,indent=4))
            self.readPythonJson(file_name)

    def run(self):
        url_list = self.get_list_url()

        for url in url_list:
         print('请求url',url)
         pythonJson = parse_url(url)
         print('请求pythonJson', pythonJson)
         pageNum = url_list.index(url)+1
         self.save_json(pythonJson,pageNum)

    def readPythonJson(self,file_name):
        with open(file_name,'r',encoding='utf-8') as f :
            print('读取电影数据',json.load(f))
            # print('读取电影类型',type(json.load(f)))

if __name__ == '__main__':
    inputDoubanName = input('输入要查询排行榜类型（例如 电影 电视剧）')
    doubanName = doubanName(inputDoubanName)
    # doubanName = doubanName('电影')
    doubanName.run()



