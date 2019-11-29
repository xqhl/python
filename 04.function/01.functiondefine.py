# 函数function
# 函数的定义, 函数参数, 函数返回值
# 用过的类型转化函数: int(); float(); str(); bool(); list(), tuple(), dict(), set()
# 用过的普通函数: print() chr() open() str: replace()
# 特点: 1.你不用去管里面怎么写的; 2.函数调用起来很方便并且节约代码

# # 函数的定义: 函数在大多数语言中, 是能够执行一个功能的代码片段
# def abc(param):
#     print(param)
# # 函数的调用
# abc("hello world")
# abc("hello kitty")

# 分析日志的函数
def logAnalysis(logpath):
    with open(file=logpath, mode='r') as log:
        x = {}
        for lines in log.readlines():
            if lines.split()[0] in x.keys():
                x[lines.split()[0]] += 1
            else:
                x.setdefault(lines.split()[0], 1)
        x = list(x.items())
        for i in range(len(x)):
            for j in range(len(x) - 1):
                if x[j][1] < x[j+1][1]:
                    x[j], x[j+1] = x[j+1], x[j]
        return dict(x)

result = logAnalysis('../03.threeday/access_log')
print(result)

# def abc(param):
#     print(param)












