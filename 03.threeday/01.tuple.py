# tuple元组:

# 元组的定义
tupleA = (1, 2, 3, "string", True, 4.445)
listA = [1, 2, 3, "string", True, 4.445]

# 大小的不同点
print(tupleA.__sizeof__())
print(listA.__sizeof__())

# 元组的遍历;切片;
for i in tupleA:
    print(i)

for j in range(len(tupleA)):
    print(tupleA[j])

print("tupleA third: {}".format(tupleA[0:3]))
print("tupleA's reverse: {}".format(tupleA[::-1]))
print("tupleA's odd number's index: {}".format(tupleA[-1]))
print("odd index and orr index: {}".format(tupleA[0:-1]))

# 元组不支持修改; -> 就是不支持增删改
# tupleA[3] = "hello world"
# print(tupleA)

tupleB = (1, 15, 27)
print(tupleA)
tupleC = tupleA + tupleB
print(tupleC)

# 元组解包
a, b, c = tupleB
print(a, b, c)

a, _, c = tupleB
print(a, c)

# 元组中自带的方法
tupleD = (1, 2, 3, True, False, "string", "string")
number = tupleD.count("string")
print(number)
index = tupleD.index("string", 0, 6)
print(index)
