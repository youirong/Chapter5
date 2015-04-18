'''
Created on 2015年4月14日， April 18

Chapter5 HF python

@author: Rong

sort()
sorted()   w/ reverse for descending order
list comprehension
集合 set() to delete repetitive numbers

'''

# james = [100]
# 
# james_file = open("james.txt")
# james = james_file.readline
# for each_time in open("james.txt"):
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

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

# print(james)
# print(julie)
# print(mikey)
# print(sarah)
# 
# james.sort()
# print(james)
# 
# jamesNew = sorted(james)
# print(jamesNew)

# print('-------')

# print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))

# jamesC = []
# for each_item in james:
#     jamesC.append(sanitize(each_item))
#     
# print(sorted(jamesC))
# 
# julieC = []
# for each_item in julie:
#     julieC.append(sanitize(each_item))
# 
# print(sorted(julieC))
# 
# mikeyC = []
# for each_item in mikey:
#     mikeyC.append(sanitize(each_item))
# 
# print(sorted(mikeyC)) #without reverse value, it is ascending order
# 
# sarahC = []
# for each_item in sarah:
#     sarahC.append(sanitize(each_item))
# 
# print(sorted(sarahC,reverse = True))  # "reverse = True" is for descending order.
#     
# 
# sarahC = [sanitize(each_item) for each_item in sarah] #list comprehension
# print(sorted(sarahC))

print(sorted([sanitize(t) for t in james]))

# print(sorted([sanitize(t) for t in julie]))
# print(sorted([sanitize(t) for t in mikey]))
# print(sorted([sanitize(t) for t in sarah], reverse = True))


james = sorted([sanitize(t) for t in james])
j = []
for each_item in james:
    if each_item not in j:
        j.append(each_item)

print(j[0], j[1], j[2])
print(j[0:3])

julie = sorted([sanitize(t) for t in julie])
ju = []
for each in julie:
    if each not in ju:
        ju.append(each)
        
print(ju[0:3])

mikey = sorted([sanitize(t) for t in mikey])
m = []
for each in mikey:
    if each not in m:
        m.append(each)

print(m[0:3])

sarah = sorted([sanitize(t) for t in sarah])
#print(sarah)
newS = set(sarah)
#print(newS)
print(sorted(newS)[0:3])
print(sorted(set(sanitize(t) for t in sarah))[0:3])
# s = []
# for each in newS:
#     s.append(each)
# print(sorted(s)[0:3])

# s = []
# for each in sarah:
#     if each not in s:
#         s.append(each)
#     
# print(s[0:3])

def openFile(inputFile):
    in_file = open(inputFile)
    data = in_file.readline()
    new_file = data.strip().split(',')
    return new_file

jj = openFile('james.txt')
print(jj)





