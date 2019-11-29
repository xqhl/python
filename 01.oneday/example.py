# 思考题:
#   有这样一个阶梯;
#   每走2层最后剩下一层;每走3层剩下2层;每走4层剩下3层;
#   每走5层最后剩下4层;每走6层剩下5层;每次走7层恰好走完;
#   请问阶梯最短有多少层?
# for i in range(7, 1000):
#     if i % 2 == 1 and i % 3 == 2 and i % 4 == 3 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
#         print(i)

i = 0
while True:
    i += 7
    if i % 2 == 1 and i % 3 == 2 and i % 4 == 3 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(i)
        break

import sys
# 练习题:
# 1. 写一个程序判断用户输入的是不是数字, 如果是那么是否是奇数?
user_input = input("please input: ")    # a123
if user_input.isdigit():                # False
    if int(user_input) % 2 == 1:
        print("yes")
    else:
        print("not")
elif "." in user_input:                 # False
    for i in range(32, 46):            # for ->
        if chr(i) in user_input:        # False -> else
            print("error: word in user_input")
            sys.exit()
    else:
        if chr(47) in user_input:
            sys.exit()
    for j in range(58, 128):
        if chr(j) in user_input:        # False -> else
            print("error: word in user_input")
            break
    else:
        print(float(user_input))


# 2. 写一个程序来计算用户输入数字的立方
user_input = input("please input: ")    # a123
if user_input.isdigit():                # False
    print(int(user_input) ** 3)
elif "." in user_input:                 # False
    for i in range(32, 46):            # for ->
        if chr(i) in user_input:        # False -> else
            print("error: word in user_input")
            sys.exit()
    else:
        if chr(47) in user_input:
            sys.exit()
    for j in range(58, 128):
        if chr(j) in user_input:        # False -> else
            print("error: word in user_input")
            break
    else:
        print("result: {:.2f}".format(float(user_input) ** 3))
else:
    print("invalid word")

# 3. 写一个程序来计算人民币转化为欧元
rate = 7.7816
user_input = input("please input: ")    # a123
if user_input.isdigit():                # False
    print(int(user_input) / rate)
elif "." in user_input:                 # False
    for i in range(32, 46):            # for ->
        if chr(i) in user_input:        # False -> else
            print("error: word in user_input")
            sys.exit()
    else:
        if chr(47) in user_input:
            sys.exit()
    for j in range(58, 128):
        if chr(j) in user_input:        # False -> else
            print("error: word in user_input")
            break
    else:
        print("result: {:.2f}".format(float(user_input) / rate))
else:
    print("invalid word")

# 4. 根据输入的成绩进行打分, 学习成绩>=90分的同学用A表示;60-89分之间的用B表示;60分以下的用C表示;
# 5. 写一个程序判断用户输入的内容是否为空, 若为空则直接提示用户重新输入, 若不为空则打印用户输入
while True:
    user_input = input("please input: ")
    if "" == user_input:
        continue
    else:
        print(user_input)
        break

