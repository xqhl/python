# set集合

# 集合的定义: 集合就是把字典中所有的key提取出来放在{}中, 所形成的数据结构 -> 特点: 元素唯一
setA = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4}
listA = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
print(setA)
print(listA)

# 对列表中重复元素去重的操作
new_listA = set(listA)
print(new_listA)

# 集合的基本操作
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

# 交集和并集
setC = setA & setB  # 两个集合之间交集
print(setC)

setD = setA | setB  # 两个集合之间并集
print(setD)

# 集合的顺序: 集合是无序的; 列表和元组是有序序列; 字符串也是有序的;
setE = {3, 2, 4, "string", 7, 5, 8}
listA = [3, 2, 4, "string", 7, 5, 8]
print("集合的顺序: {}".format(setE))
print("列表的顺序: {}".format(listA))

# 集合中的方法
setF = {1, 2, 3}

# 增加
setF.update((7, 8))
print("setF: {}".format(setF))

setF.add(4)
print("setF: {}".format(setF))

# 删除
setF.pop()
print("setF: {}".format(setF))

setF.remove(3)
print("setF: {}".format(setF))

# 查询: 集合不支持索引
# print(setF[2])
for i in setF:
    print(i)

# 查询案例
if 3 in setF:
    print(True)
else:
    print(False)
