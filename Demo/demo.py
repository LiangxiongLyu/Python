import requests
req=requests.get("http://www.baidu.com")
print(type(req))
print(req.status_code)
print(req.encoding)
print(req.cookies)