# Python的函数闭包

# 正常的函数定义: 求a+b的结果
def add(a=0, b=0):
    return a + b

# 调用函数
result = add(12, 34)
print(result)

# 进阶: 函数的别名
adds = add
result = adds(12, 34)
print(result)

# 进阶: 函数的嵌套
def waibu():
    def neibu():
        return "hello world"
    return neibu()

result = waibu()
# result = neibu()
print(result)

# 进阶: 闭包
def waibu():
    def neibu():
        return "hello world"
    return neibu

result = waibu()
# result = neibu
a = result()
print(a)

# 在函数嵌套的过程中, 在全局范围内是无法调用内部函数的, 只能在外部函数的函数体中调用内部函数;
# 但是如果想要调用内部函数的功能时, 采用外部函数返回内部函数名字的方式, 来调用内部函数;

# 使用闭包来实现计步器的功能
# 0-> 0+1 -> 1+1 -> 到公司了(3000) -> 3000+1(中午去吃饭) -> ...
def jbq(n):
    def add():
        nonlocal n
        n += 1
        return n
    return add

# 实现计步
zl = jbq(0)     # -> zl = add
zl()    # add()
zl()
zl()
zl()
step = zl()
print(step)



