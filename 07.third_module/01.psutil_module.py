# psutil: 监控CPU, Memory, Disk, Network, Process
import psutil

# 监控CPU
print("本机的逻辑CPU数为: {}".format(psutil.cpu_count()))
print("本机CPU整体所占时间: {}".format(psutil.cpu_times(percpu=False)))
print("本机CPU分别所占时间: {}".format(psutil.cpu_times(percpu=True)))

# 在指定的时间段内,去调取CPU的占用百分比;
cpu_total_percent = psutil.cpu_times_percent(interval=5)
print("本机CPU整体所占百分比: {}".format(cpu_total_percent))
print("cpu整体占用百分比: {}%".format(cpu_total_percent.user + cpu_total_percent.system))
cpu_total_percent = psutil.cpu_times_percent(interval=5, percpu=True)
print("本机CPU分别所占百分比: {}".format(cpu_total_percent))

# 监控CPU的空闲百分比, 若小于20%, 则进行报警
def cpu_idle_monitor(time_len=1):
    cpu_percent = psutil.cpu_times_percent(interval=time_len)
    use_total_percent = cpu_percent.system + cpu_percent.user
    if use_total_percent >= 80:
        print("cpu已经快到达极限了...请迅速处理")    # yagmail发送邮件
    else:
        print("cpu此时状态良好")

# cpu_idle_monitor()


# 监控memory
# psutil.virtual_memory()
# psutil.swap_memory()
print("系统的内存使用情况: {}".format(psutil.virtual_memory()))
print("交换分区使用情况: {}".format(psutil.swap_memory()))

# 监控disk
print("磁盘的总体使用情况: {}".format(psutil.disk_partitions()))
print("指定分区查看该分区的使用情况: {}".format(psutil.disk_usage(path="/")))






