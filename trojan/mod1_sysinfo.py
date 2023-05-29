import platform
import socket
import psutil
import uuid

# Get system information
system = platform.system()
node = platform.node()
release = platform.release()
version = platform.version()
architecture = platform.machine()
processor = platform.processor()
id = uuid.uuid4()

# Get network information
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_usage = psutil.cpu_percent()

# Get memory information
memory = psutil.virtual_memory()
total_memory = memory.total
available_memory = memory.available
used_memory = memory.used
memory_percent = memory.percent

# Get disk information
disk = psutil.disk_usage('/')
total_disk = disk.total
used_disk = disk.used
free_disk = disk.free
disk_percent = disk.percent

print(id)
print(f"System: {system}")
print(f"Node: {node}")
print(f"Release: {release}")
print(f"Version: {version}")
print(f"Architecture: {architecture}")
print(f"Processor: {processor}\n")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}\n")

# Print memory information
print("Memory Information:")
print(f"Total Memory: {total_memory} bytes")
print(f"Available Memory: {available_memory} bytes")
print(f"Used Memory: {used_memory} bytes")
print(f"Memory Percent: {memory_percent}%\n")
print("Disk Information:")

print(f"Total Disk Space: {total_disk} bytes")
print(f"Used Disk Space: {used_disk} bytes")
print(f"Free Disk Space: {free_disk} bytes")
print(f"Disk Usage: {disk_percent}%")
