import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
headers={'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<a.*?'+'<div.*?"content".*?'+'<span>(.*?)</span>.*?'+
                         '<div.*?"stats".*?'+'<span.*?"stats-vote".*?'+
                         '<i.*?>(.*?)</i>'
                         ,re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
