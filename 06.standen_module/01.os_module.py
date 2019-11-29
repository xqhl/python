import os


# result = os.path.split('/Users/hlions/Document/github/git.py')
# print(result[0])
#
# result = os.path.split('/Users/hlions/Document/github')
# print(result)
#
# path = os.path.dirname('/Users/hlions/Document/github/main.py')
# print(path)
#
# paths = os.path.splitext('main.py')
# print(paths)

# 获取当前目录的绝对路径
abspath = os.getcwd()
print(abspath)

# 查看当前系统指定文件夹下的内容 -> ls -a
content = os.listdir('/Users/liuchao/Documents/user')
print(content)

# 连接文件与目录路径
for i in content:
    print(os.path.join(abspath, i))

# 获取文件的大小
paths = '/Users/liuchao/Documents/user'
for files in content:
    abspath = os.path.join(paths, files)
    print(os.path.getsize(abspath))     # B

