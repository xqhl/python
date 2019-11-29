# 匿名函数: lambda variable: expresion
# 匿名函数在python编程中起到简洁易读的作用, 当实现某个单一功能的时候可以使用匿名函数;
# 不是所有功能都可以用匿名函数实现; 高级的功能有def自定义函数去实现;

# 匿名函数的定义: 特点: 没有名字
nick = lambda a, b: a + b
result = nick(12, 13)
print(result)

# def add(a, b):
#     return a + b


# 使用匿名函数提取指定位置的数据
# ips = {'1.1.1.1': 40, '2.2.2.2': 67}
# number = lambda dictType, index: dictType.iterms()[index][1]
# number = lambda dictType, key: dictType[key]

with open(file='../03.threeday/access_log', mode='r') as file:
    ip = lambda line: line.split()[0]
    ips = {}
    for lines in file.readlines():
        if ip(lines) in ips.keys():
            ips[ip(lines)] += 1
        else:
            ips.setdefault(ip(lines), 1)
    print(ips)
    # top100 = filter(lambda x: x >= 100, ips.values())
    # print(tuple(top100))
    ipSort = sorted(ips.items(), key=lambda x: x[1], reverse=True)
    print(ipSort)
    ipFilter = filter(lambda x: x[1] > 100, ipSort)
    print(tuple(ipFilter))


# 高阶函数: map(); filter(); reduce(); sorted();
# 高阶函数特性: 在高阶函数的()中可以传递自定义函数或匿名函数进去,在传入一个可迭代对象;
# 高阶函数就会将可迭代对象中的元素,逐个的传入到函数中, 让函数去处理, 并存入到容器中, 最后返回容器;
# map()函数: 对可迭代对象中的每个元素进行操作
tupleA = (1, 2, 3, 4, 5)
sq = lambda x: x ** 2
result = map(sq, tupleA)
print(tuple(result))

result = map(lambda x: x ** 2, (2, 4, 6, 8))
print(list(result))

# filter()函数: 过滤可迭代对象中符合条件的元素
def odd(x):
    if x % 2 == 0:
        return x

edd = lambda x: x % 2 == 0


tupleB = (1, 2, 3, 4, 5, 6)
result = filter(lambda x: x % 2 == 0, tupleB)
print(tuple(result))

# reduce()函数: 对可迭代对象中的元素进行相加或相乘等相互作用的功能
tupleA = (1, 2, 3, 4, 5)

from functools import reduce
result = reduce(lambda x, y: x * y, tupleA)
print(result)

# sorted()函数: 可以修改可迭代对象中的排序,或根据指定的key进行排序


