import re

s = """Hello world
你好，北京
"""

#　只能匹配ａｓｃｉｉ码字符
# regex = re.compile(r'\w+',flags = re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags = re.I)

#　.匹配换行
# regex = re.compile(r'.+',flags=re.S)

#　匹配每行开头结尾
# regex = re.compile(r'^你好',flags=re.M)

#　正则添加注释 "\w+\s+\w+"
pattern = r"""\w+  #　第一部分
\s+ #　第二部分
\w+ # 第三部分
"""
regex = re.compile(pattern,flags=re.X | re.I)

l = regex.findall(s)
print(l)
