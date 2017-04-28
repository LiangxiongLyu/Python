import os
import re
path=os.getcwd()
abspath=os.path.join(path,"t.txt")
pattern=re.compile("( )([,.])")
def fun(m):
    return m.group(2)
try:
    f=open(abspath,"r+")
    string=f.read()
    string2=re.sub(pattern,fun,string)
    print(string2)
    f.close()
except IOError as e:
    print(e)
    f.close()



