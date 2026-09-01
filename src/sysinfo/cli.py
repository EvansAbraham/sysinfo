import argparse
import subprocess
from pathlib import Path

from .collectors import collect_system_info
from .formatters import format_bytes, format_uptime, format_json

VERSION = "0.1.0"

def main():
    """Display system information."""
    parser = argparse.ArgumentParser( description="Display system information." ) 
    parser.add_argument( 
        "--version", 
        action="version", 
        version=f"sysinfo {VERSION}", 
    ) 
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output system information as JSON.",
    )
    parser.add_argument(
        "--health",
        action="store_true",
        help="Run the system health check.",
    )
    args = parser.parse_args()
    system_info = collect_system_info()

    if args.json:
        print(format_json(system_info))
        return
    if args.health:
        run_health_check()
        return

    print("=" * 50)
    print("             SYSTEM INFORMATION")
    print("=" * 50)

    print(f"OS           : {system_info['os']}")
    print(f"Kernel       : {system_info['kernel']}")
    print(f"Architecture : {system_info['architecture']}")
    print(f"Hostname     : {system_info['hostname']}")

    print()
    print(f"CPU          : {system_info['cpu']['model']}")
    print(f"CPU Cores    : {system_info['cpu']['cores']}")

    print()
    print(
        f"Memory       : "
        f"{format_bytes(system_info['memory']['used'])} / "
        f"{format_bytes(system_info['memory']['total'])}"
    )

    print(
        f"Swap         : "
        f"{format_bytes(system_info['memory']['swap_used'])} / "
        f"{format_bytes(system_info['memory']['swap_total'])}"
    )

    print(
        f"Disk         : "
        f"{format_bytes(system_info['disk']['used'])} / "
        f"{format_bytes(system_info['disk']['total'])}"
    )

    print(f"Uptime       : {format_uptime(system_info['uptime'])}")

    print()
    print(f"Python       : {system_info['python']}")

def run_health_check(): 
    """Run the system health check Bash script.""" 
    script_path = ( 
        Path(__file__).resolve().parent / "health.sh" 
        ) 
    result = subprocess.run( 
        [script_path], 
        capture_output=True, text=True, ) 
    print(f"System Health: {result.stdout.strip()}")


if __name__ == "__main__":
    main()
