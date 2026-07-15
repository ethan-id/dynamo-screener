import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found"
    return json.loads(REPORT_PATH.read_text())


def test_report_exists_and_valid_json():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    _load_report()


def test_total_requests():
    """Criterion 2: total_requests equals the number of log lines."""
    report = _load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the count of distinct client IPs."""
    report = _load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path equals the most frequently requested path."""
    report = _load_report()
    assert report["top_path"] == "/index.html"
