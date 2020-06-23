import requests
import json



headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}
post_url = 'https://fanyi.baidu.com/basetrans'
post_data = {
'query': '格式化',
'from': 'zh',
'to': 'en',
'token': '78b4dee422542070df64d51b2f3ab074',
'sign': '115896.337801'
}

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())
# dict_ret = json.loads(r.content.decode())


response = requests.get('http://www.baidu.com')
print('cookies',response.cookies)
print('cookies 字典',requests.utils.dict_from_cookiejar(response.cookies))
print('url解码',requests.utils.unquote('https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh&decrypt_suc=1#zh/en/%E4%BF%AE%E6%94%B9'))
print('url编码',requests.utils.quote('https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh&decrypt_suc=1#zh/en/修改'))
# 提示这个链接不是私密链接 不安全 verify=False(进行忽略 可以直接访问 提示警告 不会报错)
requests.get('https://wwww.baidu.com',verify=False)
# 设置请求超时时间
responseTimeout = requests.get(post_url,timeout=10)


