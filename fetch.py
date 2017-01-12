#fetch.py
import os
path=os.getcwd()
print 'Now in %s' % path
filefilter=['.mp4','.rmvb','.avi','.3gp','.flv']
def fetch(filefilter,path):
    newpath=os.path.join(path,'fetch')
    if 'fetch' in os.listdir(path):
        w=raw_input('There is a dir named \'fetch\' in the path you give, do you want to continue?(y for yes and n for no)')
        if w=='n':
            return
        elif w=='y':
            pass
    else:
        os.mkdir(newpath)
    for i in os.walk(path):
        if i[0]!=newpath:
            for f in i[2]:
                for ff in filefilter:
                    if ff==os.path.splitext(f)[1].lower():
                        fnewpath=os.path.join(newpath,f)
                        fpath=os.path.join(i[0],f)
                        print 'fetching file %s' % fpath
                        os.rename(fpath,fnewpath)
                        break


    
