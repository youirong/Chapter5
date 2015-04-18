'''
Created on 2015年4月14日

@author: Rong
'''

# james = [100]
# 
# james_file = open("james.txt")
# james = james_file.readline
# for each_time in open("james.txt"):

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
# print(james)

juf = open('julie.txt')
data = juf.readline()
julie = data.strip().split(',')

mikey = open('mikey.txt').readline().strip().split(',')
# print(mikey)

sarah = open('sarah.txt').readline().strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)








