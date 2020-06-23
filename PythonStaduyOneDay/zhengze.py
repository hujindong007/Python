import re



a = ''' <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />'''
b = 'chuan1zhi2'
print(re.sub('\d','_',b))
# 这个匹配三个是因为html中文件有隐藏的\n，导致的换行
print('不是从头开始查找，查找所有',re.findall("<.+>",a))
# re.S 匹配非空白字符  .+ 是一种贪婪模式，会匹配尽可能多的  所以会匹配成一个
print('不是从头开始查找，查找所有，遇\\n不会停止',re.findall("<.+>",a,re.S))
# .+? 非贪婪模式 ？取 0或者1次，会匹配三个
print('查询？',re.findall("<.+?>",a))
# re.compile 提前进行编译 把要匹配 设置好
p = re.compile(".")
print('p',p.findall("\n"))
p1 = re.compile(".",re.S)
print('p1',p1.findall("\n"))

p2 = re.compile("\d")
print('p2sub',p2.sub('_',b))
print('p2findall',p2.findall(b))

# r 转义字符
p3 = 'a\nb'
print(len(p3))
print(p3[1])#输出的是换行
p4 = r'a\nb'
print(len(p4))
print(p4[1])
# 转义字符 findall 匹配 \\要相同
print(r"a\nb" == "a\\nb")
print('转义字符匹配',re.findall(r"a\nb","a\\nb"))
print('转义字符匹配',re.findall(r"a\\nb","a\\nb"))




