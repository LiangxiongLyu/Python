# -*- coding: cp936 -*-
##format.py
import os
import shutil
import filecmp
path=os.getcwd()
def listdir(level,path):
    'list all dirctories in order'
    for i in os.listdir(path):
        subpath=os.path.join(path,i)
        print '|'*(level+1)+i
        if os.path.isdir(subpath):
            listdir(level+1,subpath)

def modname(name,path,size=False):
    filemap={}
    filelist=[]
    i=0
    if size==True:
        for file in os.listdir(path):
            filename=os.path.join(path,file)
            filesize=os.path.getsize(filename)
            filemap.setdefault(filename,filesize)
        filelist=sorted(filemap.items(),key=lambda d:d[1],reverse=False)
        #print filelist
    else:
        for file in os.listdir(path):
            filename=os.path.join(path,file)
            filesize=os.path.getsize(filename)
            filelist.append((filename,filesize))
        #print filelist
    for index,it in enumerate(filelist):
        oldname=it[0]
        if os.path.isfile(oldname):
            newname=os.path.join(path,(str(name)+'_'+str(index+1)+os.path.splitext(oldname)[1]))
            #print newname
            os.rename(oldname,newname)  

## in fact, there is a bug, where the newname may be the same with other file in this folder                


def merge(path,):
    filemap={}
    filelist=[]
    i=0
    removefilelist=[]
    for file in os.listdir(path):
        filename=os.path.join(path,file)
        filesize=os.path.getsize(filename)
        filemap.setdefault(filename,filesize)
    filelist=sorted(filemap.items(),key=lambda d:d[1],reverse=False)
    while i<len(filelist)-1:
        if filecmp.cmp(filelist[i][0],filelist[i+1][0]):
            print 'find file %s' % filelist[i+1][0]
            print filelist[i][0],filelist[i+1][0]
            removefilelist.append(filelist[i+1][0])
            filelist.remove(filelist[i+1])
        else:
            i+=1
    w=raw_input('Are you sure to del these files?')
    if w=='y':
        for rmfile in removefilelist:
            print 'deling file %s' % rmfile
            os.remove(rmfile)
    else:
        pass
    
    
            
