import os
import fnmatch


picture_format = ("*.gif", "*.tiff", "*.png")
# for files in os.listdir('error'):
#     for formats in picture_format:
#         if fnmatch.fnmatch(files, formats):
#             print(files)


for dirPath, dirList, fileList in os.walk('error'):
    for files in fileList:
        for formats in picture_format:
            if fnmatch.fnmatch(files, formats):
                print(os.path.join(dirPath, files))

print("*" * 20)

matchs = []
for dirPath, _, fileList in os.walk('error'):
    for formats in picture_format:
        for result in fnmatch.filter(fileList, formats):
            matchs.append(os.path.join(dirPath, result))
print(matchs)


# 找出指定目录下, 符合条件的文件; 包含了整个目录的各个层级;
