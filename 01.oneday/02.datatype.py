# usage: 基本数据类型
# date: 2019/11/18
# filepath: cloud1908/01.oneday/02.datatype.py

# python中基本的数据类型: 整型(int); 浮点型(float); 字符串类型(str); 布尔值类型(bool)

# 整型数据: int; 定义: 整数或负整数都为int类型; 判断一个数据类型使用type()
print(1 + 2)
print(2 - 1)

# 显示数据类型使用type()
print(type(23))
print(type(0))

# 浮点类型: float; 定义: 小数点的数字就是浮点数;
print(type(4.445))

# 字符串: str; 定义: 由单引或双引或三引 引起来的字符叫做字符串
print('hello world')
print("hello world")
print("hello\nworld")
print("""hello
world""")

print(type('hello world'))

# 布尔值: bool; 定义: 只含有True/False的变量或值都为bool类型
print(True)
print(False)
print(type(True))

# 运算符: + - * /
print("hello" + " " + "world")  # 字符串的低阶拼接手段
print("hello" * 20)             # 使字符串重复输出

# 取余和取整
print(5 % 2)
print(5 // 2)

# 取平方
print(5 ** 2)


