# 函数参数: param
# 在函数中传入多个参数:
def cj(a, b, c):
    print(a * b * c)

cj(1, 2, 3)

# 设定函数参数的默认值
def cjs(a=1, b=1, c=1):
    print("a: {}".format(a))
    print("b: {}".format(b))
    print("c: {}".format(c))
    print(a * b * c)

cjs(1)
# 传入指定的参数值
# cjs(a=1, b=3, 4)
cjs(1, b=3, c=1)

# 不定长度的参数
# print(1, 2, 3, 4, 5)
def println(*args):
    result = ''
    for i in args:
        result += str(i) + " "
    print(result.strip())

println(1, 2, 3, 4, 5, 6, 7)

# 函数参数的作用域
variable = 4444

def dnf():
    global variable
    variable = 13
    print(variable)

dnf()
print(variable)

