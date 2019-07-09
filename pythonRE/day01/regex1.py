import re

# 匹配结果的迭代器
s="2019年，建国70周年"
p=r"((\D)\w)"

it=re.finditer(p,s)

for i in it:
    print(i.group())

# 完全匹配

m=re.fullmatch(r'\w+',"helllo1973")
print(m.group())

# 匹配开始位置
m=re.match(r'[A-Z]\w*',"Ao hello World")
print(m.group())

# 匹配目标字符串第一个符合表达式的内容
m=re.search(r'\S',"    好了\n\n嗨")
print(m.group())

# # 匹配出汉字
# s="2019年，建国70周年"
# result=re.findall(r'(\D)\w',s)
# print(result)