# usage: if condition
# date: 2019/11/18
# filepath: cloud1908/01.oneday/03.ifcondition.py


# shell if:
# if [[ 1 -gt 2 ]];then
#   echo "1 > 2"
# elif [[ 3 -gt 4 ]];then
#   echo "3 > 4"
# else
#   echo "1 <= 2"
# fi
# shell if:
# if [[]] && || [[]];then
# if [ ! -f /etc/hosts ];then

# python if:
# if 1 > 2:
#     if 5 > 6:
#         print("5 > 6")
# elif 3 > 4:
#     print("3 > 4")
# else:
#     print("1 <= 2")

if 3 < 4 or 3 > 5:
    print("4 > 3 > 5")

if not 4 > 3 > 5:
    print("4 > 3 > 5")

# not and or: 逻辑关系运算符; 针对bool值;或产生布尔值的表达式;
# 判断一个数字是否是偶数
if 5 % 2 == 0:
    print("5 is ou")
else:
    print("5 is od")

# if单条件判断:
if 1 < 2:
    print("1 < 2")
else:
    print("2 < 1")

# if多条件判断:
if 1 < 2:
    print("1 < 2")
elif 1 < 3:
    print("1 < 3")
else:
    pass

# if的嵌套:
if 1 < 2:
    if 3 < 4:
        print(" 1 < 2 and 3 < 4")

if 1 < 2 and 3 < 4:
    print("1 < 2 and 3 < 4")

