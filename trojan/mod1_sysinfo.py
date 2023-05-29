import platform
import socket
import psutil
import hashlib
import getmac

system = platform.system()
node = platform.node()
release = platform.release()
version = platform.version()
architecture = platform.machine()
processor = platform.processor()
id = hashlib.md5(getmac.get_mac_address().encode()).hexdigest

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

cpu_count = psutil.cpu_count()
cpu_usage = psutil.cpu_percent()

memory = psutil.virtual_memory()
total_memory = memory.total
available_memory = memory.available
used_memory = memory.used
memory_percent = memory.percent

disk = psutil.disk_usage('/')
total_disk = disk.total
used_disk = disk.used
free_disk = disk.free
disk_percent = disk.percent


class SysInfo:
    def __init__(self):
        self.fetch_info()
    
    def fetch_info(self):
        data = {
            'id': id,
            'hostname': hostname,
            'operating_system': system + ' ' + node,
            'architecture': architecture,
            'processor': processor,
            'public_ip': ip_address,
            'disk_total': total_disk,
            'disk_used': disk.used,
        }

        return data