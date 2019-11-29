# 思考题:
ip = {'192.168.123.10': 34, '12.34.56.78': 12, '90.12.34.56': 19}
# 对上方的字典进行排序 -> 根据值进行排序;
iplist = list(ip.items())
for i in range(len(iplist)):
    for j in range(len(iplist) - 1):
        if iplist[j][1] < iplist[j+1][1]:
            iplist[j], iplist[j+1] = iplist[j+1], iplist[j]
print(dict(iplist))


# 从access_log中读取ip地址, 并统计每个ip访问的次数, 且提取出排名前十的IP地址;
with open(file="access_log", mode='r') as log:
    ips = {}
    for lines in log.readlines():
        if lines.split()[0] in ips.keys():
            ips[lines.split()[0]] += 1
        else:
            ips.setdefault(lines.split()[0], 1)
    ips = list(ips.items())
    for i in range(len(ips)):
        for j in range(len(ips) - 1):
            if ips[j][1] < ips[j+1][1]:
                ips[j], ips[j+1] = ips[j+1], ips[j]
    print(dict(ips[:10]))

# 请统计出网站的PV量及UV量; -> 就是在access_log中统计出接受过多少次访问?和有多少个不同的ip访问
with open(file='access_log', mode='r') as log:
    content = log.readlines()       # 把文件内容锁定到内存中,使用变量名调用内容
    pv = len(content)
    ips = {}
    for lines in content:
        if lines.split()[0] in ips.keys():
            ips[lines.split()[0]] += 1
        else:
            ips.setdefault(lines.split()[0], 1)
    print(ips)
    uv = len(ips)
    print("pv: {}, uv: {}".format(pv, uv))


# 练习题:
# 1. 如何获取到文件的行数? 请用代码表示
with open(file='access_log', mode='r') as log:
    print(len(log.readlines()))

# 2. 请统计出threekingdom.txt中"刘备","曹操","关羽","郭嘉"各出现的次数
character = ("刘备", "曹操", "关羽", "郭嘉", "主公")
with open(file='kingdoms.txt', mode='r') as file:
    content = file.read()
    new_content = content.replace("\n", "").replace(" ", "")
    for i in character:
        print("{}出现的次数为: {}".format(i, new_content.count(i)))

# 3. 请统计出threekingdom.txt中"青龙偃月刀","丈八蛇矛","雌雄双股剑","方天画戟"各出现的次数

# 4. 请统计出access_log中,(200, 404, 502, 504)状态码出现的次数;
codes = ('200', '404', '502', '504')
with open(file="access_log", mode='r') as log:
    code = {}
    for lines in log.readlines():
        if lines.split()[8] in code.keys() and lines.split()[8] in codes:
            code[lines.split()[8]] += 1
        elif not lines.split()[8] in code.keys() and lines.split()[8] in codes:
            code.setdefault(lines.split()[8], 1)
    code = list(code.items())
    print(code)

