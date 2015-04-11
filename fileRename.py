'''
Created on Apr 11, 2015
In this file, I renamed each picture downloaded by url
@author: Rong
'''


#coding=UTF-8
#userinput = input('Enter the name of a file')

#When processing Chinese file, it needs to change the codes.

import codecs
import urllib.request
import os
'''
import http.client

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
'''

nameArr = [0 for x in range(0, 216)]
nameCount = 0

for name in codecs.open("picName.txt","r","UTF-8"):
    nameArr[nameCount] = name
    nameCount = nameCount + 1
    #print (name)
    

path = "/Users/Rong/Documents/pic/"   
os.chdir(path)
os.getcwd()

count = 0

for url in open("urlList.txt"):
    
    print(count) 
    print (url)
    #filename = str(count) + '.png'
    filename = nameArr[count] + '.png'
    conn = urllib.request.urlopen(url)   
    f = open(filename,'wb')
    count = count + 1
    f.write(conn.read())  
    print('Picture Saved!')   
 
f.close()

#if I write as conn.read(), there occurs the problem of imcompleteread.
#but if I write as conn.readline(), the pic file doesn't work.:(
#So i need to get "\n" from the readline(), but how?





