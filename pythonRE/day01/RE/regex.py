import re

s = "Levi:1994,Sunny:1993"
pattern = r"(\w+):(\d+)"

#　ｒｅ模块调用
# l = re.findall(pattern,s)
# print(l)

#　compile对象调用
# regex = re.compile(pattern)
# l = regex.findall(s,0,12)
# print(l)

#　切割字符串
# s = "hello world how are  you  L-boby"
# l = re.split(r'\W+',s)
# print(l)

# 替换字符串
s = "时间: 2019/10/12"
ns = re.subn(r'\d+','00',s)
print(ns)














