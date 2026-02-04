# Cyber-Security-Tools
A collection of Python-based security utilities for log monitoring and threat detection
# Python Security Watchdog

A lightweight, automated log-monitoring utility designed to detect security threats in real-time.

## Overview
This script monitors system logs (`server_logs.txt`) and identifies critical security events using signature-based detection. It is optimized for performance by using "file tailing," ensuring minimal CPU impact while providing instant alerts.

## Key Features
- **Real-time Monitoring:** Detects "CRITICAL" and "UNAUTHORIZED" keywords as they are written.
- **Resource Efficient:** Uses the `f.seek` method to avoid re-reading old data.
- **Scalable:** Built as a foundation for future Machine Learning integration.

## Setup
1. Clone the repo: `git clone https://github.com/Kokoabc/Cyber-Security-Tools.git`
2. Run the script: `python watchdog.py`
3. Add entries to `server_logs.txt` to trigger alerts.
