import requests
import json
from retrying import retry

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

# @retry(stop_max_attempt_number=3)#这个方法可以在请求错误 连续请求多次
# def _parse_url(url,method,data):
#     print('错误请求几次')
#     if method == 'POST':
#         response = requests.post(url,data=data,headers=headers,timeout = 3)
#     else:
#         response = requests.get(url,headers = headers,timeout = 3)
#     assert  response.status_code == 200
#     return  response.content.decode()
#
# def parse_url(url,method='GET',data=None):
#     try:
#         html_str = _parse_url(url,method,data)
#     except:
#         html_str = None
#
#
# if __name__ == '__main__':
#     url = 'www.baidu.com/'
#     print('输入url得到的请求消息',parse_url(url))

@retry(stop_max_attempt_number=3)#这个方法可以在请求错误 连续请求多次
def _parse_url(url):
    print('错误请求几次')
    response = requests.get(url,headers = headers,timeout = 3)
    assert  response.status_code == 200
    print('输入url得到的请求消息', response.status_code)

    return json.loads(response.content.decode())

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None

    return html_str


# if __name__ == '__main__':
#     url = 'www.baidu.com/'
#     print('输入url得到的请求消息',parse_url(url))