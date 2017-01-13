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
    pattern = re.compile('<div.*?"author clearfix".*?'+'<h2>(.*?)</h2>.*?'+
                         '<a.*?'+'<div.*?"content".*?'+'<span>(.*?)</span>.*?'+
                         '<div(.*?)"stats".*?'+'<span.*?"stats-vote".*?'+
                         '<i.*?>(.*?)</i>'
                         ,re.S)
    items=re.findall(pattern,content)
    removeBr=re.compile('<br/>')
    for item in items:
        if not 'img' in item[2]:            
            print '___________________________________________________________________________________________'
            print item[0],':'
            print re.sub(removeBr,'\n    ','    '+item[1])
            print item[3]

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
