import random


# 随机输出0-1之间的任意一个浮点数
print(random.random())

# 随机输出0-9之间的任意一个浮点数
print("0-9: {:.2f}".format(random.uniform(0, 9)))

# 随机输出任意范围内的整数
print("int: {}".format(random.randint(0, 9)))

# 在给定的列表中随机的输出一个元素
data = ["hello", "world", "tom", 1, 2, 3, 4, 78, 3.14, 4.445]
print("element: {}".format(random.choice(data)))

# 把给定的列表打乱顺序
data = ["1", "2", 3, 4, 3.14, 18, 78, 25, 4.445]
random.shuffle(data)
print(data)
# [78, '2', 18, 4, 3, 3.14, 4.445, 25, '1']
# [4.445, 78, 3, 25, 3.14, 18, '2', '1', 4]


# 随机产生8位密码;
psd = ''
password = [chr(p) for p in range(33, 127)]
for c in range(8):
    random.shuffle(password)
    psd += password[c]
print("随机密码为: {}".format(psd))
# PGKCAlHx
# r8)$YelN
# 7i`Bk\V}
