# python 3.6
# 糗事百科爬取段子

import urllib
import urllib.request
# import regular expression module
import re
# target url
page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
# headers in the form of a dictionary
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
              ' AppleWebKit/537.36 (KHTML, like Gecko)' +
              ' Chrome/55.0.2883.87 Safari/537.36')
headers = {'User-Agent': user_agent}
# handle exception
try:
    # a Request instance
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # compile a re to match the result
    pattern = re.compile('<div.*?"author clearfix".*?' + '<h2>(.*?)</h2>.*?' +
                         '<a.*?' + '<div.*?"content".*?' +
                         '<span>(.*?)</span>.*?' +
                         '<div(.*?)"stats".*?' + '<span.*?"stats-vote".*?' +
                         '<i.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    removeBr = re.compile('<br/>')
    for item in items:
        # delete the jokes with images
        if 'img' not in item[2]:
            print('_________________________________________________' +
                  '__________________________________________')
            print(item[0], ':')
            print(re.sub(removeBr, '\n    ', '    ' + item[1]))
            print(item[3])
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)