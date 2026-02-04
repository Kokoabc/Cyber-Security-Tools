import time
import os

# Telling the script which file to monitor
LOG_FILE_PATH = "server_logs.txt"

def monitor_log():
    print(f"[*] Starting Watchdog on {LOG_FILE_PATH}...")
    
    # Creating the log file if it's missing so the script doesn't crash
    if not os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'w') as f:
            f.write("System Initialized\n")

    with open(LOG_FILE_PATH, "r") as f:
        # Jumping to the end of the file so we only see NEW logs
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1) 
                continue
            
            # The "Security Logic" - checking for specific threats
            if "CRITICAL" in line.upper() or "ERROR" in line.upper():
                print(f"[!] SECURITY ALERT: {line.strip()}")
            else:
                print(f"[+] Clean entry: {line.strip()}")

if __name__ == "__main__":
    try:
        monitor_log()
    except KeyboardInterrupt:
        print("\n[*] Watchdog stopped by user.")
