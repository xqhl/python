# string字符串: 声明, 基本操作, 索引切片, 自带方法, 实战面试题一例
string = "this's my house"

# 索引切片
# t    h    i    s    '    s        m   y       h    o    u    s   e
# 0    1    2    3    4    5    6   7   8   9   10   11   12   13  14
# -15  -14  -13  -12  -11  -10  -9  -8  -7  -6  -5   -4   -3   -2  -1
print(string[7])  # 字符串名字[索引号]
for index in range(len(string)):
    print(string[index])
# print(len(string))

for element in string:
    print(element)

# 利用索引切片出this单词
print(string[0:4])
print(string[0:15:2])     # 步长:step
print(string[0:15])
print(string[:])
print(string)
print(string[:4])
print(string[4:])
print(string[-8:9])

# 字符串中自带的几种方法
string = "This's My House"

# 把字符串转换为大写形式
new_string = string.upper()
print(new_string)
# 把字符串转换为小写形式
old_string = string.lower()
print(old_string)
# 把字符串中特定的字符进行替换
string_replace = string.replace('T', 't')
print(string_replace)
string_china = '这是我的家'
string_replace = string_china.replace('这', '那')
print(string_replace)
# 删除首尾空格或特定字符
string = '  this is my house ttt'
print(len(string))
string = string.strip('t')
print(string)
print(len(string))

string = string.lstrip()
print(string)
string = string.rstrip('t')
print(string)

# 字符串的截取
string = "192.168.161.100 2018/12/31 +0080 15:30:42 /index.php HTTP/1.1 404 ..."
string_split = string.split()
print(string_split[0])

# 字符串的拼接操作
string = 'wow'  # w^o^W
print(string.join('^^^'))
print('^'.join(string))

# 字符串中字符的统计
string = 'www.baidu.com'
print(string.count('w'))
print(string.index('a', 1, len(string)))

# 判断一个字符串是否包含在对应的字符串中?
if 'www' in string:
    print('yes')
else:
    print('no')

# 字符串格式化打印
name, score = 'tom', 90
# print("tom's grade is 90")
# print(name, "'s grade is", score)
print("{}'s grade is {}".format(name, score))
print("圆周率保留小数点后四位: {:.4f}".format(3.1415926))
# print("%s's grade is %d" % (name, score))

# 字符串的测试方法
number = input("please input number: ")
if number.isdigit():
    print("yes")
else:
    print("no")

word = input("please input word: ")
if word.isalpha():
    print("yes")
else:
    print("no")

space = input('please input: ')
if space.isspace():
    print("yes")
else:
    print("no")


# 判断一个变量是否是某个类型
string = 'hello world'
if type(string) == str:
    print(string.upper())

if isinstance(string, str):
    print(string.upper())
