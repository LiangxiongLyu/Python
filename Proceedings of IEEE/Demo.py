import re
import urllib
import urllib.request
import os
mainDomain = 'http://ieeexplore.ieee.org/'
try:
    if not os.path.exists(os.path.join(os.getcwd(), 'Demo.txt')):
        mainDomain = 'http://ieeexplore.ieee.org/'
        f = open('Demo.txt', 'w')
        url = (mainDomain +
               'xpl/tocresult.jsp?filter%3DAND%28p_IS_Number%3A31448%29&' +
               'rowsPerPage=50&pageNumber=1&resultAction=REFINE&' +
               'resultAction=ROWS_PER_PAGE&isnumber=31448#')
        print(url)
        print('Go to Site...')
        print('Fetching Content...')
        responce = urllib.request.urlopen(url)
        content = responce.read().decode('gbk')
        f.write(content)
    else:
        f = open('Demo.txt', 'r')
        content = f.read()
        # print(content)
        pattern = re.compile(
            '(Publication Year: \d+?), (Page\(s\)):\s*(\w+)\s*-*\s*(\w*)' +
            '.*?<a aria-label="Download or View the PDF:.*?href="(.*?)"',
            re.S)
        m = re.findall(pattern, content)


except urllib.URLError as e:
    print(e.reason)
finally:
    f.close()


try:
    pattern = re.compile('<embed.*?src="(.*?)"', re.S)
    for item in m:
        url = mainDomain + item[4]
        print(url)
        # responce = urllib.request.urlopen(url)
        # content = responce.read().decode('gbk')
        # print(content)
        # print(re.search(pattern, content).group())
except urllib.error.URLError as e:
    print(e.reason)
