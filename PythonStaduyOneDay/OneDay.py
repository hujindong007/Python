import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
# p = {'wd':'传智播客'}
# url_temp = 'https://www.baidu.com/s'
# r = requests.get(url_temp,headers=headers,params=p)
# print(r.status_code)
# print(r.request.url)


class TiebaSpider:
    def __init__(self,tieba_name): # init初始化
        self.tieba_name = tieba_name # 为了传值
        self.url_temp = 'https://tieba.baidu.com/f?kw='+tieba_name+'&ie=utf-8&pn={}'
        self.headers ={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    def get_url_list(self):
        # url_list = []
        # for i in range(5):
        #     url_list.append(self.url_temp.format(i*50))
        # # print('url_list:',url_list)
        # return url_list
       #这一句和上面四句一样 列表生成式
        return [self.url_temp.format(i*50) for i in range(5)]

    def parse_url(self,url):
        # print('url',url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_num):
        file_path = '{}-第{}页.html'.format(self.tieba_name,page_num)
        with open(file_path,'w',encoding='utf-8') as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        # print('url_list',url_list)
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url)+1 #页码数
            self.save_html(html_str,page_num)

if __name__  == '__main__':
    tieba_num = input('输入贴吧的名字:')
    tieba_spider = TiebaSpider(tieba_num)
    tieba_spider.run()


