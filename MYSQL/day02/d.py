import re

def count(data):
    dicting={}
    temp=re.findall(r'[a-z]+\'?[a-z]+',data,flags=re.I)

    for item in temp:
        if item not in dicting:
            dicting[item]=1
        else:
            dicting[item] += 1

    return dicting
s01='Hello,How\'s are you ?hello/you/You.'
print(count(s01))