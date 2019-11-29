# 循环语句的基本用法: for,while基本框架, +=符号的使用及意义
# 爱因斯坦阶梯问题, range的用法及生成规律;

# 打印1~20所有的数字(整型)
# n = 0
# while n < 20:
#     n = n + 1
#     print(n)

# n = 1
# while n <= 20:
#     print(n)
#     n = n + 1

# for i in range(1, 21):
#     print(i)


# 求出1-100之间所有的偶数
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
# 求出1-100之间既能被2整除又能被3整除的数字
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
# 如何书写一个死循环?;
# while True:
#     pass

# break及continue与if判断加入到循环体中后可以实现循环的终止和中断;
for i in range(100):
    print(i) # - 23
    if i == 23:
        break


while True:
    variable = input("please input your word: ")
    if variable == "bavdu":
        break

for i in range(1, 101):
    for j in range(1, 101):
        if j % 2 == 0:
            continue
        print(j)
    print("i = ", i)
