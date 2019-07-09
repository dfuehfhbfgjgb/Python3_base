import re

s="Levi:1994,Sunny:1993"
pattern=r"\w+:\d+"
pattern1=r"(\w+):(\d+)"
pattern2=r"(\w+):\d+"
# re模块调用

l=re.findall(pattern,s)
print(l) #--->['Levi:1994', 'Sunny:1993']
l=re.findall(pattern1,s)
print(l) # -->[('Levi', '1994'), ('Sunny', '1993')]

# compile调用
regex=re.compile(pattern)
l=regex.findall(s)
print(l) #--->['Levi:1994', 'Sunny:1993']

regex=re.compile(pattern)
l=regex.findall(s,0,12) #截取字符串s的一部分进行正则匹配
print(l) #--->['Levi:1994']

s="hello world how are  you  L-boby"
l=re.split(r'[^\w]+',s)
print(l) # ['hello', 'world', 'how', 'are', 'you', 'L', 'boby']

"""
    功能: 使用一个字符串替换正则表达式匹配到的内容
参数: pattern 正则表达式
replace 替换的字符串
string 目标字符串
max 最多替换几处,默认替换全部
flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串
"""
s="时间：2019/10/12"
s01=s[::-1]
# result=re.sub(r'/','-',s,)
result1=re.sub(r'/','-',s01,1)
s02=result1[::-1]
print(s02)

"""
    re.finditer(pattern,string,flags = 0)
功能: 根据正则表达式匹配目标字符串内容
参数: pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
返回值: 匹配结果的迭代器
"""

s="hello world how are you"

iter01=re.finditer(r'\w+',s)
for item in iter01:
    print(item)