import execjs
with open("fanyi.js", "r", encoding="utf-8") as f:
	js = execjs.compile(f.read())
sign = js.call("e", "我")
print("sign",sign)