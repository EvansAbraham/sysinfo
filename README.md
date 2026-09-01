# sysinfo

A lightweight Linux system information command-line utility written in Python.

`sysinfo` collects essential system information and presents it in a clean, human-readable format. It also supports machine-readable JSON output and a simple system health check.

## Features

- Operating system and distribution information
- Linux kernel version
- CPU model and core count
- System architecture
- Hostname
- Memory usage
- Swap usage
- Disk usage
- System uptime
- Python version
- JSON output for scripting and automation
- System health check
- Command-line interface with `--help` and `--version`
- Debian package support

## Installation

### From source

Clone the repository and install it with Python:

```bash
git clone https://github.com/EvansAbraham/sysinfo.git
cd sysinfo

python3 -m venv .venv
source .venv/bin/activate

python -m pip install .
```

After installation, the `sysinfo` command will be available:

```bash
sysinfo
```

## Usage

### Display system information

```bash
sysinfo
```

Example:

```text
==================================================
             SYSTEM INFORMATION
==================================================
OS           : Zorin OS 18.1
Kernel       : 6.8.0-124-generic
Architecture : x86_64
Hostname     : evansabraham-Lenovo-E41-25

CPU          : AMD PRO A4-4350B R4, 5 COMPUTE CORES 2C+3G
CPU Cores    : 2

Memory       : 2.5 GB / 3.7 GB
Swap         : 0.0 B / 1.8 GB
Disk         : 44.9 GB / 156.1 GB
Uptime       : 1h 23m

Python       : 3.14.3
```

### JSON output

Use `--json` when the output needs to be consumed by scripts or other tools:

```bash
sysinfo --json
```

Example:

```json
{
  "os": "Zorin OS 18.1",
  "kernel": "6.8.0-124-generic",
  "architecture": "x86_64",
  "hostname": "evansabraham-Lenovo-E41-25",
  "cpu": {
    "model": "AMD PRO A4-4350B R4, 5 COMPUTE CORES 2C+3G",
    "cores": 2
  },
  "memory": {
    "used": "2.5 GB",
    "total": "3.7 GB",
    "available": "1.2 GB"
  },
  "swap": {
    "used": "0.0 B",
    "total": "1.8 GB"
  },
  "disk": {
    "used": "44.9 GB",
    "total": "156.1 GB",
    "free": "103.2 GB"
  },
  "uptime": "1h 23m",
  "python": "3.14.3"
}
```

### System health check

Run the health check with:

```bash
sysinfo --health
```

Example:

```text
System Health: HEALTHY
```

The health check is implemented using a small Bash component integrated with the Python CLI.

### Version

```bash
sysinfo --version
```

Example:

```text
sysinfo 0.1.0
```

### Help

```bash
sysinfo --help
```

## Development

Create a development environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and development dependencies:

```bash
python -m pip install -e .
python -m pip install pytest build
```

Run the test suite:

```bash
pytest
```

The project currently includes tests for the system information collectors and output formatters.

## Building

Build the Python source distribution:

```bash
python -m build --sdist
```

The resulting source archive will be placed in:

```text
dist/
```

## Debian Packaging

The project also contains Debian packaging metadata under `debian/`.

Build the Debian package with:

```bash
dpkg-buildpackage -us -uc
```

This produces the Debian source package and binary package in the parent directory.

## Project Structure

```text
sysinfo/
├── debian/
│   ├── changelog
│   ├── control
│   ├── copyright
│   ├── rules
│   └── source/
│       └── format
├── src/
│   └── sysinfo/
│       ├── __init__.py
│       ├── cli.py
│       ├── collectors.py
│       ├── formatters.py
│       └── health.sh
├── tests/
│   ├── test_collectors.py
│   └── test_formatters.py
├── pyproject.toml
└── README.md
```

## Design Goals

The project is intentionally small and focused on practical Linux system tooling.

The main goals are:

- Keep the command-line interface simple.
- Separate system data collection from presentation.
- Provide both human-readable and machine-readable output.
- Keep the implementation easy to test and extend.
- Demonstrate integration between Python, Linux system interfaces, and Bash.
- Support standard Python packaging and Debian packaging workflows.

## Requirements

- Python 3.10 or newer
- Linux
- Standard system utilities required by the health-check component

## License

This project is licensed under the MIT License.

Copyright © 2026 Evans Abraham.