# netwatch/netwatch.py

import os
import psutil
import time
import threading

class NetWatch:
    def __init__(self, interval=1):
        self.pid = os.getpid()
        self.proc = psutil.Process(self.pid)
        self.interval = interval
        self.running = False
        self.thread = None

    def _monitor(self):
        print(f"[NetWatch] Monitoring PID {self.pid}...\n")
        while self.running:
            conns = self.proc.connections(kind="inet")
            if conns:
                print("[NetWatch] Active connections:")
                for conn in conns:
                    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                    print(f"  {conn.status} | {laddr} -> {raddr}")
            else:
                print("[NetWatch] No active network connections.")
            time.sleep(self.interval)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._monitor, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        print("\n[NetWatch] Monitoring stopped.")
