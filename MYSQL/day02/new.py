# print(list(range(10,1,-1)))
# print(list(range(6))[::2])
# print(3 in [1,2,3,4])

# print(sorted([111,2,33],key=lambda x:len(str(x))))
# x=[1,2,3,4,5]
# # print(x.pop())
# print(x.pop(-1))

# print([i for i in range(10)])

# x=5
# y=6
# print(x if x>y else y)
# print(isinstance('abc',str))

# print(int("0x12",base=16))
# print([chr(x) for x in range(97,123)])

def count_word(string):
    data=string.lower()
    dicting={}
    start=i=0
    while True:
        if 97<=ord(data[i])<=122:
            i+=1
        else:
            temp=data[start:i]
            while True:
                i += 1
                if 97<=ord(data[i])<=122:
                    break


            start=i
            i+=1
            if temp not in dicting:
                dicting[temp]=1
            else:
                dicting[temp] += 1

        if i==len(data):
            return dicting
string='Hello World,How are you?  \
       https//:www.baidu.com,,,are'


print(count_word(string))