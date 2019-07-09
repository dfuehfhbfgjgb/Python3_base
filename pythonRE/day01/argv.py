import sys
import re

port = sys.argv[1]

f=open('1.txt')

while True:
    data=''
    for line in f:
        if line != '\n': # 不是空行
            data+=line
        else:
            break
    # print(">>>",data)
    if not data:
        print("Not Found the %s"%port)
        break

    # 匹配目标字符串data开始位置
    key_word=re.match(r'\S+',data).group() # 匹配非空字符串
    print(key_word)
    if port == key_word:
        pattern=r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        # pattern=r'(\d{1,3}\.){3}\d{1,3}/\d+|Unknow'
        try:
            # 匹配目标字符串data中第一个符合内容的字符串
            address = re.search(pattern,data).group()
            print(address)
        except:
            print("No address")
        break


# 作业：
# 1. 正则表达式使用
# 2. 复习聊天室，ftp文件服务，httpserver 2.0
# 3. 学习markdown的书写格式