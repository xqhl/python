# 列表: 声明方法, 如何遍历, 基本操作, 变量值交换, 算法(冒泡排序, 二分查找)
# 四种数据类型: int,float,str,bool叫做python中的基石;
# 四中数据结构: 元组(tuple), 列表(list), 字典(dict), 集合(set)

# 声明list的方式
listA = [18, 3.14, 'string', True]
print(listA, type(listA))
if isinstance(listA, list):
    print("yes")

listB = [x for x in range(1, 101) if x % 2 == 0]
print(listB)

# 对列表进行遍历
for index in range(len(listA)):
    print(listA[index])
print(listA[1])

for element in listA:
    print(element)

# 列表的加法
listC = [1, 2, 3, 4, True, False]
listD = [5, 6, 7, 'string']
print(listC + listD)

# 列表的乘法
print(listC * 20)

# 列表的减法?
# listE = [1, 2, 3, 4]
# listF = 1
# print(listE - listF)

# 冒泡排序知识储备 变量值的交换
v1, v2 = 'hello', 23
v1, v2 = v2, v1
print(v1, v2)

listA = [12, 11, 14, 37, 23, 45, 67, 15, 78]
for i in range(len(listA)):
    for j in range(len(listA) - 1):
        if listA[j] < listA[j+1]:
            listA[j], listA[j+1] = listA[j+1], listA[j]
print(listA)
# i = 0
# -> j = 0 -> listA[0] > listA[0+1] -> 交换
# [11, 12, 14, 37, 23, 45, 67, 15, 78]
# -> j = 1 -> listA[1] > listA[1+1]  -> 不换
# [11, 12, 14, 37, 23, 45, 67, 15, 78]
# -> j = 2 -> listA[2] > listA[2+1]  -> 不换
# [11, 12, 14, 37, 23, 45, 67, 15, 78]
# -> j = 3 -> listA[3] > listA[3+1] -> 交换
# [11, 12, 14, 23, 37, 45, 67, 15, 78]
# -> j = 4 -> listA[4] > listA[4+1] -> 不换
# [11, 12, 14, 23, 37, 45, 67, 15, 78]
# -> j = 5 -> listA[5] > listA[5+1] -> 不换
# [11, 12, 14, 23, 37, 45, 67, 15, 78]
# -> j = 6 -> listA[6] > listA[6+1] -> 交换
# [11, 12, 14, 23, 37, 45, 15, 67, 78]
# -> j = 7 -> listA[7] > listA[7+1] -> 不换

# 二分查找
listB = [11, 12, 14, 15, 23, 37, 45, 67, 78]

number = int(input("please input number: "))
start, stop = 0, len(listB) - 1
while stop - start > 0:
    middle = (start + stop)//2
    if number < listB[middle]:
        stop = middle - 1
    elif number > listB[middle]:
        start = middle + 1
    else:
        print(listB[middle])
        break

# list的增删改查
listA = [1, 2, 3, True]

# list增加
print(listA)

listB = [4, 5, 6]
listA.extend(listB)
print(listA)

listA.insert(5, 4.5)
print(listA)

# list删除
listA.remove(True)
print(listA)
listA.remove(True)
print(listA)

listA.pop(3)
print(listA)

# listA.clear()
# print(listA)

# del listA

# list更改
listA[1] = 3.5
print(listA)

listA.append(55)
print(listA)
# list查询
n = listA.count(5)
print(n)

strA = "[2, 3.5, 4, 5, 6, 55]"
m = strA.count('5')
print(m)

print(listA.index(5, 0, len(listA)))

# 把列表进行倒序排列
listB = [1, 2, 4, 3, 5]
listB.reverse()
print(listB)

# 列表排序
listC = [12, 14, 21, 6, 3, 1, 22, 45, 31]
listC.sort()
print(listC)
