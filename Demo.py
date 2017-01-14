import urllib
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
loginUrl="https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action"
postData=urllib.urlencode({
    'username':'56ff07f249594f8e7ec6f9101ff4a2fc2287f81293dd5e400c23cb19805136d35f46598bf8f1b13932b62f1f4ed25e1bb65ad5fd663a56c4312becbb69a0da32d37314b3097ef5d15944997f4bb0d98a7b34607939f694e54e7169d23b997fce95d625bec5414eb263c09d0a79c58ddd6628552952e2f7ef53ec037d66ff8222',
    'password':'1fb8cd2ca5b1ceb208d3d52210dcb3d3ae990c35ad3dce7da43ce51f0b50c7be011e87d510db09fd6fd640d58ed7022838014716a821dc828d27bc190cdea2c6f84d165b551dd3bb6b732e17f7af6781dce6d210d2b2e2711a6c4eca086919313d9e52edbd11ef041e22f2e182f3779b8eb2785f825b4d269634c3af85bec800',
    'code':'code',
    'lt':'LT-NeusoftAlwaysValidTicket',
    'execution':'e1s1',
    '_eventId':'submit'
    })
# print postData,type(postData)
headers={
    'POST':'/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action HTTP/1.1',
    'Host':'pass.hust.edu.cn',
    'Connection':'keep-alive',
    'Content-Length': '603',
    'Cache-Control':'max-age=0',
    'Origin':'https://pass.hust.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'https://pass.hust.edu.cn/cas/login?service=http%3A%2F%2Fhubs.hust.edu.cn%2Fhustpass.action',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'JSESSIONID=BpuYBG2kOJbvwoeWkeWXUHinjJpJsJYMaJIJRkOTDDoBjao_aAYc!1123674794'
    }

request=urllib2.Request(loginUrl,postData,headers)
responce=opener.open(request)
print responce.read()


# "10001","","89b7ad1090fe776044d393a097e52f99fc3f97690c90215ecb01f1b3dfc4d8b0226a4b16f51a884e0c1545180eb40365dbec848cc0df52f515512e2317bf9d82b6f4c9cafcc94082fd86c97e77a4d3aa44cba54f8d94f5757ce3cc82c3adf31082738cfe531b4b4675f35a0c8401745dbed15c92d0747c6349915378fff22b9b"
