import time
import subprocess
from datetime import datetime

RESTART_HOUR = 6
SERVER_SCRIPT = "./start.sh"

def log(msg):
    with open("restart.log", "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

while True:
    now = datetime.now()
    if now.hour == RESTART_HOUR and now.minute == 0:
        log("Restart triggered.")
        subprocess.call(["screen", "-S", "mc", "-X", "stuff", "stop\n"])
        time.sleep(10)
        subprocess.Popen(["bash", SERVER_SCRIPT])
        log("Server restarted successfully.")
        time.sleep(60)
    time.sleep(5)
