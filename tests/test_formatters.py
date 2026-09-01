from sysinfo.formatters import format_bytes, format_uptime, format_json


def test_format_bytes():
    assert format_bytes(0) == "0.0 B"
    assert format_bytes(1024) == "1.0 KB"
    assert format_bytes(1024 * 1024) == "1.0 MB"
    assert format_bytes(1024 * 1024 * 1024) == "1.0 GB"


def test_format_uptime():
    assert format_uptime(0) == "0s"
    assert format_uptime(60) == "1m"
    assert format_uptime(3600) == "1h"
    assert format_uptime(86400) == "1d"
    assert format_uptime(90061) == "1d 1h 1m"


def test_format_json():
    system_info = {
        "os": "Test OS",
        "kernel": "6.0",
        "architecture": "x86_64",
        "hostname": "test-machine",
        "cpu": {
            "model": "Test CPU",
            "cores": 2,
        },
        "memory": {
            "used": 1024,
            "total": 2048,
            "available": 1024,
            "swap_used": 0,
            "swap_total": 4096,
        },
        "disk": {
            "used": 1024,
            "total": 4096,
            "free": 3072,
        },
        "uptime": 60,
        "python": "3.14.3",
    }

    result = format_json(system_info)

    assert '"os": "Test OS"' in result
    assert '"model": "Test CPU"' in result
    assert '"used": "1.0 KB"' in result
    assert '"uptime": "1m"' in result
