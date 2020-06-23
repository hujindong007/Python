import json
import  requests
from parse_url import parse_url
from  pprint import pprint

#原始请求
# https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20
#去除不需要的字段请求
# https://movie.douban.com/j/new_search_subjects?tags=%E7%94%B5%E8%A7%86%E5%89%A7&start=0

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

url = "https://movie.douban.com/j/new_search_subjects?tags=电影&start=0"
response = requests.get(url, headers=headers, timeout=3)
assert response.status_code == 200
pprint(response.content.decode())
# json.loads() json字符串转成python数据类型
ret1 = json.loads(response.content.decode())
pprint(ret1)

with open("doubanMovie.json","w",encoding="utf-8") as f:
    # f.write(str(ret1))#只是转成字符串
    #json.dumps() python数据类型转成json字符串
    f.write(json.dumps(ret1,ensure_ascii=False,indent=4))#ensure_ascii=False 防止中文被转换 indent 换行空格




