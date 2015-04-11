'''
Created on 2015年4月9日

@author: Rong
'''

'''
#to download a single picture in a url 

import urllib.request  
path = "/Users/Rong/Documents/pic"  
url = "http://pp.myapp.com/ma_icon/0/icon_10401156_20513627_1423729826/96"  
name ="/Users/Rong/Documents/pic/1.jpg"  
#When savinga file, remember to match the type
#保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片  
conn = urllib.request.urlopen(url)  
f = open(name,'wb')  
f.write(conn.read())  
f.close()  
print('Pic Saved!')   
'''


# read txt file line after line
'''
for line in open("list.txt"):
    print (line)
'''

#To download pictures contained in the url and rename it from 1 to the last. 
#the list of url is written in the list.txt (place it in "/Users/Rong/Documents/pic/")
#save it in the file folder - /Users/Rong/Documents/pic/
#a bug that I met: when there is "NULL" in the list.txt, program interrupts always, but at different time.

import urllib.request  
import os

path = "/Users/Rong/Documents/pic/"  
os.chdir(path)
os.getcwd()
count = 1

for url in open("urlList.txt"):
    print(count) 
    print (url)
    filename = str(count) + '.png'
    #filename = str(name) + '.jpg' 
    conn = urllib.request.urlopen(url)   
    f = open(filename,'wb')
    count = count + 1
    f.write(conn.read())  
    #f.close()  
    print('Picture Saved!')   
 
f.close()
    







