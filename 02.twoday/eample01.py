# # 思考题
# # 有这样一个句子"this is my house", 对该句子进行反转, 输出为"house my is this"
# s = "this is my house"
# s_list = s.split()
# s_list.reverse()
# s_reverse = ""
# for i in s_list:
#     s_reverse += i + " "
# print(s_reverse.strip())
#
# print(' '.join(s.split()[::-1]))
#
# # 模拟用户的验证码输入并进行比对;
# import random
#
# code = ""
# for i in range(4):
#     number = random.randint(0, 9)
#     word = chr(random.randint(65, 92))
#     code += str(number) + word
# print("check code: {}".format(code[:4]))
# user_input = input("input: ")
# if code[:4] == user_input.upper():
#     print("true")
# else:
#     print("false")
#
#
# # 网络搜索中的敏感词替换;
# search = input("search: ")
# new_search = search.replace("游戏", 'eooro')
# error_list = ['eooro', 'fatal', 'aaa']
# for e in error_list:
#     if e in new_search:
#         print("未找到您搜索的页面")
#         break
# else:
#     print("您搜索的内容是...")
#
# # 练习题:
# # 1. ['ABC', 'abc', [1, 2, 3, 4, 5], [3, 4, 5], 1, 2, 3, 4, 5]将列表中的数字全都提取到
# # 一个新的列表中, 并进行排序;
# listA, listB = [], ['ABC', 'abc', [1, 2, 3, 4, 5], [3, 4, 5], 1, 2, 3, 4, 5]
# for element in listB:
#     if isinstance(element, list):
#         for i in element:
#             if isinstance(i, int) or isinstance(i, float):
#                 listA.append(i)
#     elif isinstance(element, int) or isinstance(element, float):
#         listA.append(element)
# listA.sort()
# print(listA)
#
# # 2. [23, 45, 12, 21, 13, 25, 46, 28, 9, 34]对该列表进行排序;
# listC = [23, 45, 12, 21, 13, 25, 46, 28, 9, 34]
# for i in range(len(listC)):
#     for j in range(len(listC) - 1):
#         if listC[j] > listC[j+1]:
#             listC[j], listC[j+1] = listC[j+1], listC[j]
# print(listC)

# 3. 列表["string", "tuple", "list", [1, 2, 3, 4, 5], 12, [6, 7]]转换成
# ["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7];
index, listD = 0, ["string", "tuple", "list", [1, 2, 3, 4, 5], [6, 7]]
for element in listD:
    if not type(element) in [int, float, str, bool]:
        for i in element:
            listD.append(i)
        index = listD.index(element)
print(listD)
print(index)
listD.pop(index-1)
listD.pop(index-1)
print(listD)

# 4. 有这样一堆球, 每次数2个最后剩下1个; 数3剩2; 数4剩3; 数5剩4; 数6剩5; 恰恰数7个恰好数完;

# 5. 快速生成一个含有数字1到100之间的偶数的列表;
listE = []
for i in range(1, 101):
    if i % 2 == 0:
        listE.append(i)
print(listE)

listF = [i for i in range(1, 101) if i % 2 == 0]
print(listF)

# 6. 使用python计算10-9+8-7+6-5+4-3+2-1的结果?
# 10-9+8-7+6-5+4-3+2-1 -> 0-1+2-3+4-5+6-7+8-9+10
s = 0
for i in range(11):
    if i % 2 == 0:
        s += i
    else:
        s -= i
print(s)



