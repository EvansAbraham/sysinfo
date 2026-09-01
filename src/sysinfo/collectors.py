import os
import platform
import shutil
import socket


def get_os_info():
    """Get the operating system name."""
    try:
        with open("/etc/os-release") as file:
            for line in file:
                if line.startswith("PRETTY_NAME="):
                    return line.strip().split("=", 1)[1].strip('"')
    except FileNotFoundError:
        pass

    return platform.system()



def get_cpu_info():
    """Get basic CPU information."""
    cpu_model = "Unknown"

    try:
        with open("/proc/cpuinfo") as file:
            for line in file:
                if line.startswith("model name"):
                    cpu_model = line.split(":", 1)[1].strip()
                    break
    except FileNotFoundError:
        pass

    return {
        "model": cpu_model,
        "architecture": platform.machine(),
        "cores": os.cpu_count(),
    }

def get_memory_info():
    """Get system memory and swap information."""
    memory = {}

    try:
        with open("/proc/meminfo") as file:
            for line in file:
                key, value = line.split(":", 1)

                parts = value.strip().split()
                number = int(parts[0])
                unit = parts[1] if len(parts) > 1 else None

                if unit == "kB":
                    number *= 1024

                memory[key] = number

    except FileNotFoundError:
        return {
            "total": 0,
            "used": 0,
            "available": 0,
            "swap_total": 0,
            "swap_used": 0,
        }

    total = memory.get("MemTotal", 0)
    available = memory.get("MemAvailable", 0)
    used = total - available

    swap_total = memory.get("SwapTotal", 0)
    swap_free = memory.get("SwapFree", 0)
    swap_used = swap_total - swap_free

    return {
        "total": total,
        "used": used,
        "available": available,
        "swap_total": swap_total,
        "swap_used": swap_used,
    }

def get_disk_info(path="/"):
    """Get disk usage information."""
    usage = shutil.disk_usage(path)

    return {
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
    }


def get_uptime():
    """Get system uptime in seconds."""
    with open("/proc/uptime") as file:
        return float(file.readline().split()[0])


def format_bytes(value):
    """Convert bytes into a human-readable value."""
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if value < 1024:
            return f"{value:.1f} {unit}"

        value /= 1024

    return f"{value:.1f} PB"


def format_uptime(seconds):
    """Convert seconds into a human-readable uptime."""
    seconds = int(seconds)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    parts = []

    if days:
        parts.append(f"{days}d")

    if hours:
        parts.append(f"{hours}h")

    if minutes:
        parts.append(f"{minutes}m")

    if not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)

def collect_system_info():
    """Collect all system information."""
    return {
        "os": get_os_info(),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "hostname": socket.gethostname(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "uptime": get_uptime(),
        "python": platform.python_version(),
    }
