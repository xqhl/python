# string type:
string = 'hello world'

# 获取string变量的类型
print("string variable's type: {}".format(type(string)))

# 获取string的长度: 单个字符的个数即长度
print("string's len: {}".format(len(string)))

# 获取string中特定字符,或特定范围的字符
# h e l l o   w o r l d     ->  string
# 0 1 2 3 4 5 6 7 8 9 10
# -len(string) -len(string) + 1
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print("string's o: {}".format(string[4]))
# 字符串的遍历: 把字符串中每一个字符进行打印; 意义: 可以单独的处理每一个字符
for index in range(len(string)):
    print(string[index])
# 支持索引的数据结构统称为可迭代对象; 可迭代对象的特点为: 可直接使用for进行遍历而不需要使用索引
for word in string:
    print(word)

# 切片: 起始标号到终止标号之间的内容; 意义: 获取业务所需要的信息; 特点: 切片为左闭右开区间
print(string[6:11])
print("o->d: {}".format(string[4:]))
print("h->w: {}".format(string[:7]))
print("h->l->o->w->r: {}".format(string[:9:2]))     # 步长:每个字符之间距离(单位:单个字符)
# 输出首尾字符
print("string's first word: {}".format(string[0]))
print("string's last word: {}".format(string[len(string) - 1]))
print("string's last word: {}".format(string[-1]))


# 字符串中自带的方法:
# join()拼接 // replace()替换 // split()切片 // upper()lower()大小写转换
# strip()删除首尾特定字符 // isdigit()判断是否为纯整数 // isalpha()判断是否为纯字母[Aa-Zz]
# count()统计字符串中特点字符的个数 // index()寻找字符串中特定字符的索引号
string = "This's my House "

# 字符串大小写转换
print("set string's word to upper: {}".format(string.upper()))
print("set string's word to lower: {}".format(string.lower()))

# 替换字符串中某一个字符; str type不可变;
new_string = string.replace("o", "0")
print("string replace to new_string: {}".format(new_string))

# 删除首尾的空格及特定字符
new_string = string.strip()
print("string strip to new_string: {}".format(new_string))
print("string rstrip/lstrip to new_string: {}".format(string.lstrip()))
print("string's T remove: {}".format(string.lstrip("T")))

# 判断字符串中的内容 -> 这几种方法都会返回布尔值 -> 可应用于if判断
# isdigit()判断纯数字; isalpha()判断纯字母; isidentifier()判断是否含有特殊字符;
# islower()判断纯小写; isupper()判断纯大写;

# split切片: 按照规定的字符对文本进行分割; awk -F" " 'NR==2{ print $1 }' /etc/passwd
string = 'hello world kitty class cloud'
print("string's space split: {}".format(string.split()))

# join连接: 把规定字符添加至对象中
string = "hello"    # -> To display: h e l l o
print("To display: h e l l o: {}".format(' '.join(string)))
# new_string = "" + h + " "
# new_string = new_string + e + " "
# new_string = new_string + l + " "

new_string = ''
for i in string:
    new_string += i + " "
print(new_string.rstrip())

# count()统计字符串中特点字符的个数
string = "hello"
print("l's number: {}".format(string.count("l")))

# index()寻找字符串中特定字符的索引号
string = "hello hello"
print("l's index: {}".format(string.index("l", 4, len(string) - 1)))
print("l's index: {}".format(string.find("l", 4, len(string) - 1)))

# 输出倒序的字符串
# hello -> olleh
string = "hello"
print("olleh: {}".format(string[::-1]))
