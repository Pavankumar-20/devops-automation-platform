import time
import shutil

import psutil
from prometheus_client import Gauge, start_http_server

cpu_usage = Gauge(
    "system_cpu_usage_percent",
    "CPU usage percentage"
)

memory_usage = Gauge(
    "system_memory_usage_percent",
    "Memory usage percentage"
)

disk_usage = Gauge(
    "system_disk_usage_percent",
    "Disk usage percentage"
)


def collect_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)

    disk = shutil.disk_usage("/")
    disk_usage.set(disk.used / disk.total * 100)


if __name__ == "__main__":
    print("Starting metrics server on port 8000")

    start_http_server(8000)

    while True:
        collect_metrics()
        time.sleep(5)
