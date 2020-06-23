import requests
import json

# post_url = 'http://www.renren.com'

class Xiushi:
    def __init__(self):
        # self.url = 'https://www.qiushibaike.com/text/page/{}/'
        self.url = 'https://www.qiushibaike.com/text/page/3/'
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

    def run(self):
        response = requests.get(self.url,headers=self.headers,timeout=3)
        print('输出网页内容',response.content.decode())


if __name__ == '__main__':
    xiushi = Xiushi()
    xiushi.run()