from sysinfo.collectors import (
    get_os_info,
    get_cpu_info,
    get_memory_info,
    get_disk_info,
    get_uptime,
    collect_system_info,
)


def test_get_os_info():
    result = get_os_info()

    assert isinstance(result, str)
    assert result


def test_get_cpu_info():
    result = get_cpu_info()

    assert isinstance(result, dict)
    assert "model" in result
    assert "architecture" in result
    assert "cores" in result

    assert isinstance(result["model"], str)
    assert isinstance(result["architecture"], str)
    assert isinstance(result["cores"], int)


def test_get_memory_info():
    result = get_memory_info()

    assert isinstance(result, dict)

    assert "total" in result
    assert "used" in result
    assert "available" in result
    assert "swap_total" in result
    assert "swap_used" in result

    assert result["total"] >= 0
    assert result["used"] >= 0
    assert result["available"] >= 0
    assert result["swap_total"] >= 0
    assert result["swap_used"] >= 0


def test_get_disk_info():
    result = get_disk_info()

    assert isinstance(result, dict)

    assert "total" in result
    assert "used" in result
    assert "free" in result

    assert result["total"] > 0
    assert result["used"] >= 0
    assert result["free"] >= 0


def test_get_uptime():
    result = get_uptime()

    assert isinstance(result, float)
    assert result >= 0


def test_collect_system_info():
    result = collect_system_info()

    assert isinstance(result, dict)

    expected_keys = {
        "os",
        "kernel",
        "architecture",
        "hostname",
        "cpu",
        "memory",
        "disk",
        "uptime",
        "python",
    }

    assert set(result.keys()) == expected_keys
