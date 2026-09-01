#!/bin/bash

DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$DISK_USAGE" -lt 80 ]; then
    echo "HEALTHY"
    exit 0
elif [ "$DISK_USAGE" -lt 90 ]; then
    echo "WARNING"
    exit 1
else
    echo "CRITICAL"
    exit 2
fi
