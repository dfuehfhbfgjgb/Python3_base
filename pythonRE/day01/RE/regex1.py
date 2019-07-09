import re

s = "2019年,建国70周年"
pattern = r"\d+"

#　返回包含匹配结果的迭代器
it = re.finditer(pattern,s)

# print(dir(next(it)))

# for i in it:
#     print(i.group())


#　完全匹配
# m = re.fullmatch(r'[0-9a-zA-Z]+',"hello1973")
# print(m.group())

#　匹配开始位置
# m = re.match(r'[A-Z]\w*',"Hello World")
# print(m.group())

#　匹配第一处
m = re.search(r'\S+',"    好嗨 呦")
print(m.group())



