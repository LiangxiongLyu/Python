import urllib
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
loginUrl="/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action"
postData=urllib.urlencode({
    'username':'U201310604',
    'password':'qqww651767201',
    'code':'code',
    'lt':'LT-NeusoftAlwaysValidTicket',
    'execution':'e1s1',
    '_eventId':'submit'
    })
headers={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'POST':'/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action HTTP/1.1',
    'Host':'pass.hust.edu.cn',
    'Connection':'keep-alive',
    'Content-Length': '603',
    'Cache-Control':'max-age=0',
    'Origin':'https://pass.hust.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'JSESSIONID=BpuYBG2kOJbvwoeWkeWXUHinjJpJsJYMaJIJRkOTDDoBjao_aAYc!1123674794'
    }
print 1
request=urllib2.Request(loginUrl,postData,headers)
responce=opener.open(request)
print responce.read().decode('utf-8')
