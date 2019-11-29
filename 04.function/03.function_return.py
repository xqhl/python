# 函数返回值

string = 'hello world'
string = string.replace('o', '0')
print(string)

# 具备返回值的函数
def add(a=0, b=0):
    c = a + b
    return c

def odd(c=1, d=1):
    e = c * d
    return e

# result_add = add(2, 3)
# result_odd = odd(c=result_add, d=6)
# print(result_odd)
result = odd(c=add(2, 3), d=6)
print(result)

# yield生成器
with open(file='../03.threeday/access_log', mode='r') as log:
    print(log.readline())
    print(log.readline())

def ysd():
    for i in range(100):
        yield i
# @容器@ -> @1@ -> @1, 2@

def ysds():
    listA = []
    for i in range(100):
        listA.append(i)
    return listA

result = ysd()
print(result.__sizeof__())
# for i in result:
#     print(i)

result = ysds()
print(result.__sizeof__())
# for i in result:
#     print(i)
