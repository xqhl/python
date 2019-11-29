# list struct:
# 在python中四个数据基石: 元组/列表/字典/集合

# 列表的声明和方法调用
# string = "hello world"
listA = ["string", 14, 3.14, True, ["hello", 1, 3.14, False]]

# 列表的的长度
print("listA's len: {}".format(len(listA)))
# 对于列表的遍历
for i in range(len(listA)):
    print(listA[i])

for j in listA:
    print(j)

# 对于列表如何去利用索引打印特定值
print(listA[2])
# 列表的切片
print(listA[1:3])
# 列表中的负号索引
print("first index: {}".format(listA[0]))
print("last index: {}".format(listA[-1]))
# 列表的反序输出   -> 列表是一个有序的集合(序列)
print("revers list: {}".format(listA[::-1]))


# 列表中的方法: 增删改查
listB = [1, 2, 3]

# 增加元素:
listB.append(14)    # 追加: 在列表的末尾进行增加元素
print("listB elements: {}".format(listB))

listB.insert(2, "insert")   # 在指定位置插入元素: 确定两元素,插入时使用右边元素索引号,即可插入到两元素之间;
print("listB elements: {}".format(listB))

listC = ["123", "456", "789"]
listB.extend(listC)         # 在指定列表中扩充另外一个列表中的元素;
print("listB elements: {}".format(listB))

# 删除元素
# listB.pop(2)    # 指定索引删除元素
# print("listB elements: {}".format(listB))
#
# listB.remove('456')   # 指定元素名称进行删除
# print("listB elements: {}".format(listB))

# listB.clear()     # 清空了;列表中所有的元素
# print("listB elements: {}".format(listB))
#
# del listB         # 从内存中删除列表的空间
# print("listB elements: {}".format(listB))

# 更改元素
listB[-3] = 123     # 利用索引号对其代表的位置进行重新赋值
print("listB elements: {}".format(listB))

listB.reverse()     # 让列表倒序显示
print("listB elements: {}".format(listB))

listD = [12, 3, 23, 56, 78, 94, 26]
listD.sort(reverse=True)    # 对数字列表进行排序
print("listD elements: {}".format(listD))

# 查询元素
listE = [1, 2, 3, 4, True, False, 'string']

print("listE element number: {}".format(listE.count(0)))    # 统计特定元素的个数
print("listE element index: {}".format(listE.index('string')))  # 查询特定元素的索引

listF = listB.copy()
print(listB)
print(listF)

listG = listB
print(listB)
print(listG)


# 冒泡排序: 其实质就是两个for循环
listH = [12, 3, 23, 56, 78, 94, 26]
for i in range(len(listH)):
    for j in range(len(listH) - 1):
        if listH[j] > listH[j+1]:
            listH[j], listH[j+1] = listH[j+1], listH[j]
print(listH)

# i = 0;
# -> j = 0 -->> if listH[0] > listH[0+1] --->>> 12 > 3 - True: [3, 12, 23, 56, 78, 94, 26]
# -> j = 1 -->> if listH[1] > listH[1+1] --->>> 12 > 23 - False
# ...
# -> j = 5 -->> if listH[5] > listH[5+1] --->>> 94 > 26 - True: [3, 12, 23, 56, 78, 26, 94]

# i = 1;


# 二分查找: 从已经排好顺序的列表中去查找;
search = int(input("please input: "))

listI = [3, 12, 23, 26, 56, 78, 94]
findex, lindex = 0, len(listI) - 1
while lindex - findex >= 0:
    middle = (findex + lindex) // 2
    if listI[middle] == search:
        print(middle)
        break
    elif listI[middle] < search:
        findex = middle + 1
    elif listI[middle] > search:
        lindex = middle - 1

