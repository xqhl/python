# 文件读写
file = open(file='./train', mode='r')

# content = file.read()   # 读取文件通篇内容
# print(content)

# content = file.readline()   # 逐行读取
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)

content = file.readlines()  # 将文件中每行内容放置到列表中, 以此来精确的处理每一行

file.close()


with open(file='train', mode='r') as file:
    print(file.readlines())

with open(file="aaa.txt", mode='a') as file:
    file.write("abc/abc/abc\n")
    file.writable()
    file.writelines(["abc\n", "cdb\n", "nml\n"])

# with open(file="aaa.txt", mode='w') as file:
#     file.write("cdf/cdf/cdf")











