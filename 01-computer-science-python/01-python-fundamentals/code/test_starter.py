import pytest
from starter import parse_log_line, analyze_log_file
from pathlib import Path


def test_parse_log_line():
    line = '127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = parse_log_line(line)
    assert result is not None
    assert result["ip"] == "127.0.0.1"
    assert result["method"] == "GET"
    assert result["path"] == "/index.html"
    assert result["protocol"] == "HTTP/1.1"
    assert result["status"] == 200
    assert result["size"] == 1024

    # Test with size '-' (no bytes)
    line2 = '192.168.1.1 - - [10/Oct/2024:14:30:01 +0000] "GET /notfound HTTP/1.1" 404 -'
    result2 = parse_log_line(line2)
    assert result2 is not None
    assert result2["size"] == 0

    # Test malformed line
    assert parse_log_line("not a valid log line") is None


def test_analyze_log_file(tmp_path):
    log_content = '''\
127.0.0.1 - - [10/Oct/2024:14:30:00 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.1 - - [10/Oct/2024:14:30:01 +0000] "POST /api/data HTTP/1.1" 201 512
127.0.0.1 - - [10/Oct/2024:14:30:02 +0000] "GET /about HTTP/1.1" 404 0
'''
    log_file = tmp_path / "test.log"
    log_file.write_text(log_content)

    stats = analyze_log_file(log_file)
    assert stats["total_requests"] == 3
    assert stats["successful_requests"] == 2  # 200 + 201
    assert stats["failed_requests"] == 1      # 404
    assert stats["total_bytes"] == 1536       # 1024 + 512 + 0
    assert stats["methods"]["GET"] == 2
    assert stats["methods"]["POST"] == 1
    assert stats["paths"]["/index.html"] == 1
    assert stats["paths"]["/api/data"] == 1
    assert stats["paths"]["/about"] == 1
    assert stats["status_codes"][200] == 1
    assert stats["status_codes"][201] == 1
    assert stats["status_codes"][404] == 1
    assert stats["top_ips"]["127.0.0.1"] == 2
    assert stats["top_ips"]["192.168.1.1"] == 1