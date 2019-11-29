def ip_sort(log_path='access_log'):
    with open(file=log_path, mode='r') as log:
        ips = {}
        for lines in log.readlines():
            ip = lines.split()[0]
            if ip in ips.keys():
                ips[ip] += 1
            else:
                ips.setdefault(ip, 1)
        ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))
        return ips

