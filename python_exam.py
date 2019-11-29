# 1. 有这样一堆球, 每次数2个最后剩下1个; 数3剩2; 数4剩3; 数5剩4; 数6剩5; 恰恰数7个恰好数完;
n = 7
while True:
    if n % 2 == 1 and n % 3 == 2 and n % 4 == 3 and n % 5 == 4 and n % 6 == 5 and n % 7 == 0:
        print("小球的数量最小为: {}".format(n))
        break
    n += 1

# 2. 使用while循环, 反转句子"hello Tony this my sister"; 反转后为"sister my this Tony hello";
sentence = "hello Tony this my sister"
sentence_list = sentence.split()
sentence_reverse, n = "", len(sentence_list)
while n > 0:
    n -= 1
    sentence_reverse += sentence_list[n] + " "
print(sentence_reverse.strip())

sentence = "hello Tony this my sister"
print(' '.join(sentence.split()[::-1]))

# 3. 列表["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]转换成["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7];
listA, listB = [], ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
for element in listB:
    if not isinstance(element, (int, float, str, bool)):
        for e in element:
            listA.append(e)
    else:
        listA.append(element)
print(listA)

# 4. 对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]进行排序; 方式一: 要求使用for循环; 方式二: sorted函数;
listC = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
for i in range(len(listC)):
    for j in range(len(listC) - 1):
        if listC[j] > listC[j+1]:
            listC[j], listC[j+1] = listC[j+1], listC[j]
print(listC)

listC = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
listC.sort()
print(listC)

# 5. 元组("string", "world", 1, 2, 3.14, 4, 6, 9, 10), 把其中的数字提取到一个列表中;
listD, tupleA = [], ("string", "world", 1, 2, 3.14, 4, 6, 9, 10)
for element in tupleA:
    if isinstance(element, (int, float)):
        listD.append(element)
print(listD)

# 6. 提取access_log日志中所有的IP地址到字典ips中, 并根据ips中每个IP出现次数进行排序;
with open(file='access_log', mode='r') as log:
    ips = {}
    for lines in log.readlines():
        ip = lines.split()[0]
        if ip in ips.keys():
            ips[ip] += 1
        else:
            ips.setdefault(ip, 1)
    ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True)[:10])
    print(ips)

# 7. 字符串"hello7723worl45d78", 把其中的数字提取到一个元组中;
listE, string = [], "hello7723worl45d78"
for word in string:
    if word.isdigit():
        listE.append(int(word))
print(tuple(listE))

# 8. 利用函数求取10的阶乘结果;10 * 9 * 8 * 7 ... * 1
def jc(number=1):
    if number == 1:
        return number
    return number * jc(number - 1)

print(jc(10))

# 9. 书写一个函数, 实现让用户输入验证码, 并判断用户输入的验证码正确与否;
import random
def checkCode(c=4):
    cc = []
    for i in range(c):
        cc.append(str(chr(random.randint(65, 90))))
        cc.append(str(random.randint(0, 9)))
    random.shuffle(cc)
    print(cc)
    ccs = ''.join(cc[:c])
    print("checkCode is {}".format(ccs))
    return ccs

# check_code = checkCode(4)
# user_input = input("input: ")
# if check_code == user_input.upper():
#     print("ok")
# else:
#     print("false")

# 10. 书写一个装饰器, 功能为计算程序执行的时间;
import time
def program_time(func):
    def wrapper(*args, **kwargs):
        first_time = time.time()
        listA = func(*args, **kwargs)
        end_time = time.time()
        print("刚刚程序运行了: {}秒".format(end_time - first_time))
        return listA
    return wrapper

@program_time
def println(number):
    listG = []
    for i in range(number):
        listG.append(i)
    return listG

listH = println(1000)
print(listH)

# 11. 使用正则表达式, 匹配出access_log中所有的IP地址;
import re
with open(file='access_log', mode='r') as log:
    content = log.read().replace('\n', "").replace(" ", "")
    ips = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", content)
    print(ips)

# 12. 请先写出闭包的框架, 然后利用该框架来实现一个计步器的功能
def waibu(n=0):
    def neibu():
        nonlocal n
        n += 1
    return neibu

# 13. 快速生成一个含有数字1到100的列表;
listF = [x for x in range(1, 101)]
# 14. 根据输入的成绩进行打分, 学习成绩>=90分的同学用A表示;60-89分之间的用B表示;60分以下的用C表示;
# 15. 编写一个函数, 可以在文件中增加用户自定义的内容;
def writes(filepath, content="anyStr"):
    with open(file=filepath, mode='a') as files:
        files.write(content)

writes('./aaa.txt', 'hello aaa')
