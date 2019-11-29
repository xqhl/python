# 思考题
# 有这样一个句子"this is my house", 对该句子进行反转, 输出为"house my is this"
sentence = 'this is my house'
new_sentence = ''
index = len(sentence.split()) - 1
while index >= 0:
    # new_sentence = new_sentence + sentence.split()[index] + ' '
    new_sentence += sentence.split()[index] + ' '
    # index = index - 1
    index -= 1
print(new_sentence.rstrip())

sentence = 'cloud1906 is good class'
print(' '.join(sentence.split()[::-1]))

# 模拟用的验证码输入并进行比对;
import random
# print(type(chr(random.randint(65, 90))))
code = ''
for i in range(4):
    code += str(random.randint(0, 9))
    code += chr(random.randint(65, 90))
print('please input check code: {}'.format(code[0:4]))
user_input = input("please input: ")
if user_input.upper() == code[0:4]:
    print("load successfully")
else:
    print("load failed.")

# 网络搜索中的敏感词替换;
user_input = input("please input search: ")
word = ['op', '老师', '航空']
print(user_input.replace('op', '**').replace('老师', '**').replace('航空', '**'))



# 练习题:
# 1. ['ABC', 'abc', [1, 2, 3, 4, 5], [3, 4, 5], 1, 2, 3, 4, 5]将列表中的数字全都提取到
# 一个新的列表中, 并进行排序;
new_list, old_list = [], ['ABC', 'abc', [1, 2, 3, 4, 5], [3, 4, 5], 1, 2, 3, 4, 5]
for element in old_list:
    # if isinstance(element, (int, float)):
    if type(element) in [int, float]:
        new_list.append(element)
    elif not type(element) in [int, float, str]:
        for e in element:
            new_list.append(e)
new_list.sort()
print(new_list)


# 2. [23, 45, 12, 21, 13, 25, 46, 28, 9, 34]对该列表进行排序;
listA = [23, 45, 12, 21, 13, 25, 46, 28, 9, 34]
for i in range(len(listA)):
    for j in range(len(listA) - 1):
        if listA[j] > listA[j+1]:
            listA[j], listA[j+1] = listA[j+1], listA[j]
print(listA)

# 3. 列表["string", "tuple", "list", [1, 2, 3, 4, 5], [6, 7]]转换成
# ["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7];
new_list, old_list = [], ["string", "tuple", "list", [1, 2, 3, 4, 5], [6, 7]]
for element in old_list:
    if not type(element) in [int, float, str, bool]:
        for e in element:
            new_list.append(e)
    else:
        new_list.append(element)
print(new_list)


# 4. 有这样一堆球, 每次数2个最后剩下1个; 数3剩2; 数4剩3; 数5剩4; 数6剩5; 恰恰数7个恰好数完;
for i in range(7, 1000):
    if i % 2 == 1 and i % 3 == 2 and i % 4 == 3 and i % 5 == 4 and i % 6 == 5:
        if i % 7 == 0:
            print(i)


# 5. 快速生成一个含有数字1到100之间的偶数的列表;
listB = [x for x in range(1, 101) if x % 2 == 0]
listC = []
for x in range(1, 101):
    if x % 2 == 0:
        listC.append(x)


# 使用python计算10-9+8-7+6-5+4-3+2-1的结果?
n, m = 10, 0
while n > 0:
    m += n * (-1) ** n
    n -= 1
print(m)

m = 0
for n in range(1, 11):
    if n % 2 == 0:
        m += n
    else:
        m -= n
print(m)
