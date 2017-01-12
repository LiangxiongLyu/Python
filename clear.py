#clear.py
#clear the trabish files
import os
import shutil

def listDir(path,level=0):
    'list all dirctories in order'
    for i in os.listdir(path):
        subpath=os.path.join(path,i)
        print '*'*(level+1)+i
        if os.path.isdir(subpath):
            listdir(level+1,subpath)

video=['.mp4','.wmv','.rmvb','.avi','.mov','.mpg','.mpeg','.dat','.rm','.asf']
photo=['.gif','.jpg','.png','.bmp','.jpeg','.tiff','.pcd','.svg']
others=['.py','.ass','.rar','zip','txt']
filefilter=video+photo+others
path=os.getcwd ()

def clear(filefilter,path):
    'Clear files according to the filefilter'
    print 'Clearing Files!'
    for i in os.walk(path):
        for f in i[2]:               #for each file under the path 
            for ff in filefilter:
                if ff in os.path.splitext(f)[1].lower():
                    break
            else:                    #for file without strs in filefilter in its name
                absf=os.path.join(i[0],f)
                print 'remove file %s' % absf
                os.remove(absf)
    print 'Cleared!'




def clearEmptyDir(abspath):
    if not os.path.isabs (abspath):
        print 'Need absolute path'
        return 0
    count=0
    for i in os.walk(abspath):
        if i[1] or i[2]:
            continue
        else:
            print 'removing empty dir %s' % i[0]
            shutil.rmtree(i[0])
            count+=1
    if count:
        clearEmptyDir(abspath)
        
        



