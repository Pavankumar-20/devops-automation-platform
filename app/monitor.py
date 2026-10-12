
import platform
import shutil
from datetime import datetime

import psutil


def check_system():
    print("=" * 45)
    print("DEVOPS SYSTEM HEALTH MONITOR")
    print("=" * 45)

    print(f"Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Operating System: {platform.system()}")
    print(f"Hostname: {platform.node()}")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    disk_percent = disk.used / disk.total * 100

    print(f"\nCPU Usage: {cpu:.1f}%")
    print(f"Memory Usage: {memory.percent:.1f}%")
    print(f"Disk Usage: {disk_percent:.1f}%")

    print("\nHEALTH REPORT")

    print("WARNING: High CPU usage" if cpu >= 80
          else "OK: CPU usage normal")

    print("WARNING: High memory usage" if memory.percent >= 80
          else "OK: Memory usage normal")

    print("WARNING: High disk usage" if disk_percent >= 80
          else "OK: Disk usage normal")

    print("=" * 45)


if __name__ == "__main__":
    check_system()
