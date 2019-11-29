import re


data = 'Last login: Thu Mar  2 10:04:52 2019 from 39.100.110.135'
print(data.split(":"))

# 希望根据空格,".",":"进行字符串的切割
result = re.split('[\' \':.]', data)
print(result)

data01 = 'What is the difference between python 2.7.13 and python 3.7.3 ?'
version = re.findall("[0-9.]+[0-9]", data01)
print(version)

res = re.compile("[0-9.]+[0-9]")    # 匹配x.x.x的模式
data02 = "192.168.123 abc abc 14.14.14 bcd"
result01 = res.findall(data01)
print(result01)
result02 = res.findall(data02)
print(result02)
