import re
import time

LOG_FILE = "/var/mc/latest.log"
OUTPUT = "player-activity.log"

join_re = re.compile(r"\[.*\]: (.+) joined the game")
quit_re = re.compile(r"\[.*\]: (.+) left the game")

seen = set()

while True:
    try:
        with open(LOG_FILE) as f:
            for line in f:
                j = join_re.search(line)
                q = quit_re.search(line)

                if j:
                    name = j.group(1)
                    if name not in seen:
                        seen.add(name)
                        with open(OUTPUT, "a") as out:
                            out.write(f"[JOIN] {name}\n")

                if q:
                    name = q.group(1)
                    if name in seen:
                        seen.remove(name)
                        with open(OUTPUT, "a") as out:
                            out.write(f"[QUIT] {name}\n")

    except:
        pass
    
    time.sleep(2)
