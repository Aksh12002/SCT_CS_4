from datetime import datetime

REPORT_FILE = "security_report.txt"


def generate_defensive_report():
    content = f"""
Security Awareness Report
Generated: {datetime.now()}

This tool demonstrates ethical, application-scoped keystroke monitoring.

How malicious keyloggers differ:
- Run without user knowledge
- Capture system-wide keystrokes
- Hide processes and files
- Transmit data remotely

How to detect keyloggers:
- Check running processes
- Review startup programs
- Use antivirus / EDR tools
- Monitor unusual system hooks

This project logs keystrokes ONLY inside the app window
and requires explicit user consent.
"""

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(content.strip())

    return REPORT_FILE
