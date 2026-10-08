#!/usr/bin/env python3
"""Log analyzer - complete the TODOs.

This lesson teaches: variables, data types, control flow,
functions, file I/O, and error handling in Python.
"""
import sys
from collections import Counter
from pathlib import Path


def parse_log_line(line: str) -> dict | None:
    """Parse a Common Log Format line.

    Example input:
      127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024

    Returns a dict with keys: ip, timestamp, method, path, protocol, status, size
    or None if the line doesn't match the expected format.
    """
    # TODO: Implement parsing using string methods or regex
    # 1. Split the line into components
    # 2. Extract IP, timestamp, request line, status, size
    # 3. Parse the request line into method, path, protocol
    # 4. Convert status and size to int
    import re

    pattern = re.compile(
        r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d+) (\d+|-)'
    )
    match = pattern.match(line.strip())
    if not match:
        return None
    ip, timestamp, method, path, protocol, status, size = match.groups()
    return {
        "ip": ip,
        "timestamp": timestamp,
        "method": method,
        "path": path,
        "protocol": protocol,
        "status": int(status),
        "size": int(size) if size != "-" else 0,
    }


def analyze_log_file(path: Path) -> dict:
    """Analyze the log file and return statistics dict."""
    stats = {
        "total_requests": 0,
        "successful_requests": 0,
        "failed_requests": 0,
        "total_bytes": 0,
        "methods": Counter(),
        "paths": Counter(),
        "status_codes": Counter(),
        "top_ips": Counter(),
    }

    lines_analyzed = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            entry = parse_log_line(line)
            if entry is None:
                continue

            lines_analyzed += 1
            stats["total_requests"] += 1

            if 200 <= entry["status"] < 300:
                stats["successful_requests"] += 1
            elif entry["status"] >= 400:
                stats["failed_requests"] += 1

            stats["total_bytes"] += entry["size"]
            stats["methods"][entry["method"]] += 1
            stats["paths"][entry["path"]] += 1
            stats["status_codes"][entry["status"]] += 1
            stats["top_ips"][entry["ip"]] += 1

    return stats


def format_bytes(n: int) -> str:
    """Format byte count into human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 starter.py <log_file>")
        sys.exit(1)

    log_path = Path(sys.argv[1])
    if not log_path.exists():
        print(f"Error: File {log_path} not found")
        sys.exit(1)

    stats = analyze_log_file(log_path)

    print("Log Analysis Results:")
    print("=" * 50)
    print(f"Total requests:         {stats['total_requests']}")
    print(f"Successful requests (2xx): {stats['successful_requests']}")
    print(f"Failed requests (4xx/5xx): {stats['failed_requests']}")
    print(f"Total bytes served:     {format_bytes(stats['total_bytes'])}")

    if stats["methods"]:
        top_method, top_count = stats["methods"].most_common(1)[0]
        pct = (top_count / stats["total_requests"]) * 100 if stats["total_requests"] else 0
        print(f"Most common method:    {top_method} ({pct:.0f}%)")

    if stats["paths"]:
        top_path, top_count = stats["paths"].most_common(1)[0]
        print(f"Most requested path:   {top_path} ({top_count}x)")

    if stats["top_ips"]:
        top_ip, ip_count = stats["top_ips"].most_common(1)[0]
        print(f"Top IP address:        {top_ip} ({ip_count} requests)")

    if stats["total_requests"]:
        avg_size = stats["total_bytes"] / stats["total_requests"]
        print(f"Average response size:  {format_bytes(int(avg_size))}")


if __name__ == "__main__":
    main()
