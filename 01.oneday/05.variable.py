# usage: variable
# date: 2019/11/18
# filepath: cloud1908/01.oneday/05.variable.py

# shell variable
# var="hello world"

# 单变量赋值
var01 = "hello world"
print(var01, type(var01))
if type(var01) == str:
    print("True")
else:
    print("False")

if isinstance(var01, str):
    print("True")
else:
    print("False")

# 多变量赋值
# shell中多个变量在同一行赋值?
# var01="hello";var02="world"
var01, var02 = "hello", "world"

# 链式赋值
var03 = var04 = var05 = 18
if isinstance(var03, int):
    print("True")
else:
    print("False")


# 键盘读值
# read -p "please input: " var
# var06 = input("please input: ")
# print("var06's type: ", var06, type(var06))

# 表达式赋值
# shell: a=2;b=3
# echo "$a+$b" | bc
var07 = var03 + var04
print(var07)

# 变量的值交换
n01, n02 = "hello", "world"
print(n01, n02)

n01, n02 = n02, n01
print(n01, n02)

# 变量类型的转化
var08 = input("please input: ")
# print(var08.isdigit())
if var08.isdigit():
    var08 = int(var08)
    print(var08, type(var08))
else:
    print(var08, " not a number.")

# # str -> int
# number = '123456'
# color = '蓝'
# new_number = int(number)
# print(new_number, type(new_number))
#
# # int -> str
# old_number = 12
# print(old_number, type(old_number))
# new_number = str(old_number)
# print(new_number, type(new_number))
#
# # int -> bool
# aa = 1
# print(aa, type(aa))
# new_aa = bool(aa)
# print(new_aa, type(new_aa))
#
# # 只要是非零数字转化成bool类型都是True
# print(bool(0))
# print(bool(2))
# print(bool(3))
# print(bool(-56))
#
# # int -> float; str -> float
# number = 12.74
# print(int(number))
#
# string = "34.56"
# print(float(string))
