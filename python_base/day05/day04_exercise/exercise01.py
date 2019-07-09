# 在控制台中循环录入字符串，输入ｑ时退出．
# 　　然后显示一个新的字符串．

# # str_result = ""
# list_result = []
# while True:
#     str_input = input("请输入：")
#     if str_input =="q":
#         break
#     # str_result = str_result + str_input
#     # （１）使用列表拼接
#     list_result.append(str_input)
#
# #(2)　使用join合并
# str_result = "".join(list_result)
# print(str_result)
#
#
# # 字符串　－－＞　列表
# list01 = list("abc")
# list01 = "a-b-c".split("-")
# print(list01)


string='asfd-tvxhsbf'
list02='asfdt-vxh-sbf'.split(" ")
print(list02)

list03=['d','gfhdg','sads']
str01="".join(list03)
print(str01)


# 统计列表中各元素在列表中出现了几次
list_targe=[1,4,7,5,1,9,8]
dict01={}
for item in list_targe:
    if item not in dict01:
        dict01[item]=1
    else:
        dict01[item]+=1

print(dict01)






