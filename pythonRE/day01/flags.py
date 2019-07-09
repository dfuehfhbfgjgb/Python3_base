import re

s = """Hello world
你好，北京
"""
regex = re.compile(r'\w+')
l=regex.findall(s)
print(l) # -->['Hello', 'world', '你好', '北京']

regex = re.compile(r'\w+',flags = re.A) # 只能匹配ascii字符
l=regex.findall(s)
print(l) # -->['Hello', 'world']

regex = re.compile(r'[a-z]+', flags=re.I)  # 匹配忽略字母大小写
l = regex.findall(s)
print(l)  # -->['Hello', 'world']

regex = re.compile(r'.+',flags = re.S) # 使 . 可以匹配换行
l=regex.findall(s)
print(l) # -->['Hello world\n你好，北京\n']

regex = re.compile(r'.+')
l=regex.findall(s)
print(l) # -->['Hello world', '你好，北京']

regex = re.compile(r'.*')
l=regex.findall(s)
print(l) # -->['Hello world', '', '你好，北京', '', '']

regex = re.compile(r'World$',flags = re.M) # 使 ^ $可以匹配每一行的开头结尾位置
l=regex.findall(s)
print(l) # -->['world']

# 正则添加注释
regex = re.compile(r'World$#匹配行末尾字符',flags = re.X|re.I|re.M)
l=regex.findall(s)
print(l)