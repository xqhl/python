# dict字典: {key01: values, key02: values, ...}

# 字典的定义
dictA = {"key01": 3.14, "key02": 14}
dictB = dict([("key01", 3.14), ("key02", 14)])
print(dictA)
print(dictB)

# 字典的特点: 值不唯一且键唯一; 项
print({"key01": 3.14, "key02": 3.14})

# 字典的遍历
print(dictA.items())
for kv in dictA.items():
    print(kv)

for keys in dictA.keys():
    print(keys)

for values in dictA.values():
    print(values)

# 字典有没有索引? 没有 -> 但是可以把key当做索引;
listA = [1, 2, 3, 4, 5]
dictA = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5}
print(listA[2], dictA["2"])


# 字典方法: 增删改查
dictA = {"tom": 92}
# 增加
dictA['jerry'] = 90
print(dictA)

dictA.update([('hale', 60), ('natasha', 34)])
print(dictA)

dictA.setdefault('beta', None)
print(dictA)

# 删除
dictA.pop('jerry')
print(dictA)

dictA.popitem()
print(dictA)

# 更改
dictA['tom'] = 60
print(dictA)

dictA.update([('hale', 92), ('natasha', 78)])
print(dictA)


# 查询
natasha_grade = dictA.get('natasha')
print(natasha_grade)

# 快速生成字典
tupleA = ("tom", "hale", "natasha", "beta", "nezha")
dictB = {}.fromkeys(tupleA)
print(dictB)


# ips = {'192.168.123.10': 34, '12.34.56.78': 12, '90.12.34.56': 19}
# 对上方的字典进行排序 -> 根据值进行排序;


