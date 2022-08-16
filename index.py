import re
import json
s_file=open('exclude-words.txt', "r", encoding='utf-8')
s_content = s_file.read()
read=s_content.split('\n')

s_dis={}
for i in read:
    if i in s_dis:
        s_dis[i] = s_dis[i]+1
    else:
        s_dis[i] = 1


# page1

file = open('Page1.txt', "r", encoding='utf-8')
content = file.read()
read1= re.split(r'[ ,\n ./:;]',content)

dis={}
for i in read1:
    if i in dis:
        dis[i] = dis[i]+1
    else:
        dis[i] = 1


for j in s_dis:
    if j in dis:
        dis.pop(j)

# page2
file2 = open('Page2.txt', "r", encoding='utf-8')
content2 = file2.read()
read2 = re.split(r'[ ,\n ./:;]',content2)

dis2={}
for i in read2:
    if i in dis2:
        dis2[i] = dis2[i]+1
    else:
        dis2[i] = 1

for j in s_dis:
    if j in dis2:
       dis2.pop(j)

# page3
file3 = open('Page3.txt', "r", encoding='utf-8')
content3 = file3.read()
read3 = re.split(r'[ ,\n ./:;]',content)

dis3={}
for i in read3:
    if i in dis3:
        dis3[i] = dis3[i]+1
    else:
        dis3[i] = 1

for j in s_dis:
    if j in dis3:
       dis3.pop(j)



# All data
result={}
for i in dis:
    if i in result:
        result[i] = result[i]+1
    else:
        result[i] = 1
for i in dis2:
    if i in result:
        result[i] = result[i]+1
    else:
        result[i] = 1
for i in dis3:
    if i in result:
        result[i] = result[i]+1
    else:
        result[i] = 1
# final result calculate
final={}
for i in result:
    list1=[]
    if i in dis:
        list1.append("1")
    if i in dis2:
        list1.append("2")
    if i in dis3:
        list1.append("3")
    final[i] = list1

# sending data from dictionary to new file

with open("final.txt", 'w') as f:
    for key, value in final.items():
        f.write('%s:%s\n' % (key, value))