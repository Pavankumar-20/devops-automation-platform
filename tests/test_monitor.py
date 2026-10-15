import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MONITOR_SCRIPT = PROJECT_ROOT / "app" / "monitor.py"


def test_monitor_script_exists():
    assert MONITOR_SCRIPT.is_file()


def test_monitor_runs_successfully():
    result = subprocess.run(
        [sys.executable, str(MONITOR_SCRIPT)],
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0, result.stderr
    assert "DEVOPS SYSTEM HEALTH MONITOR" in result.stdout
    assert "CPU Usage:" in result.stdout
    assert "Memory Usage:" in result.stdout
    assert "Disk Usage:" in result.stdout
