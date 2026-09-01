import json


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


def format_json(system_info):
    """Convert system information into formatted JSON."""
    data = {
        "os": system_info["os"],
        "kernel": system_info["kernel"],
        "architecture": system_info["architecture"],
        "hostname": system_info["hostname"],
        "cpu": {
            "model": system_info["cpu"]["model"],
            "cores": system_info["cpu"]["cores"],
        },
        "memory": {
            "used": format_bytes(system_info["memory"]["used"]),
            "total": format_bytes(system_info["memory"]["total"]),
            "available": format_bytes(system_info["memory"]["available"]),
        },
        "swap": {
            "used": format_bytes(system_info["memory"]["swap_used"]),
            "total": format_bytes(system_info["memory"]["swap_total"]),
        },
        "disk": {
            "used": format_bytes(system_info["disk"]["used"]),
            "total": format_bytes(system_info["disk"]["total"]),
            "free": format_bytes(system_info["disk"]["free"]),
        },
        "uptime": format_uptime(system_info["uptime"]),
        "python": system_info["python"],
    }

    return json.dumps(data, indent=2)
