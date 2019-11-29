import paramiko
import os
#
#
# client = paramiko.SSHClient()   # ssh root@192.168.123.11
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # continue(yes/no)? yes
# client.connect(
#     hostname='39.100.110.135',
#     port=22,
#     username='***',
#     password='***'
# )
#
# stdin, stdout, stderr = client.exec_command(command='ls -l /etcc', timeout=1)
# print(stdout.read().decode('utf-8'))
# print(stderr.read().decode('utf-8'))
#
# client.close()

# client = paramiko.SSHClient()
# client.close()

# with paramiko.SSHClient() as client:
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('39.100.110.135', 22, '***', '***')
#     _, stdout, stderr = client.exec_command('ls -l /etc')
#     print(stdout.read().decode('utf-8'))


# 基于秘钥对儿连接 -> 需要提前做好秘钥认证
# private_key = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')    # 指定本地私钥文件
# with paramiko.SSHClient() as client:
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('39.100.110.135', 22, 'bavduer', pkey=private_key)
#     _, stdout, stderr = client.exec_command('ls /home/bavduer')
#     result = stdout.read().decode('utf-8')
#     print(result, type(result))
#     print(len(result))


# 利用paramiko模块在远程主机中, 运行一个脚本(初始化脚本)
# with paramiko.SSHClient() as client:
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect('39.100.110.135', 22, 'bavduer', pkey=private_key)
#     os.system('scp helloworld.sh bavduer@39.100.110.135:/home/bavduer/initserver.sh')
#     client.exec_command('bash /home/bavduer/initserver.sh')

# 写一个为终端, 可以让用户输入登录的账号和密码, 以及IP地址;
def terminal(IPAddress, user='root', passwd='123!@#'):
    with paramiko.SSHClient() as terminals:
        terminals.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        terminals.connect(IPAddress, 22, user, passwd)
        while True:
            command = input("{}@localhost~: ".format(user))
            if command in ("exit", "logout"):
                print("正在退出...")
                break
            else:
                _, out, error = terminals.exec_command(command)
                result = out.read().decode('utf-8')
                if len(result) != 0:
                    print(result)
                else:
                    print(error.read().decode('utf-8'))

# ip = input('ip address: ')
# user = input('username: ')
# password = input("password: ")
# terminal(ip, user, password)

private_key = paramiko.RSAKey.from_private_key_file('/Users/liuchao/.ssh/id_rsa')
with paramiko.Transport(('39.100.110.135', 22)) as transport:
    transport.connect(username='bavduer', pkey=private_key)
    # 执行远程连接
    # client = paramiko.SSHClient()
    # client._transport = transport
    # _, stdout, stderr = client.exec_command('ls -l /etc')
    # print(stdout.read().decode('utf-8'))
    # 构建文件服务器: 可以往服务器上传文件或下载文件
    sftp = paramiko.SFTPClient.from_transport(transport)
    abspath = os.getcwd()
    for files in os.listdir("./"):
        sftp.put(localpath=os.path.join(abspath, files),
                 remotepath='/home/bavduer/{}'.format(files))
    # sftp.get(remotepath='/etc/bash.bashrc', localpath='./bashrc')
    # sftp.put(localpath='bashrc', remotepath='/home/bavduer/bashrc.rc.rc.rc')


# 把initserver.sh分发到该网段中存活主机里面;
# 使用python来分发;
# sshfor(ping ip) -> online ip file -> python with(file) -> lines -> ip -> paramiko()
# 前提: 需要提前把秘钥传送到远程主机中; -> shell脚本实现;
