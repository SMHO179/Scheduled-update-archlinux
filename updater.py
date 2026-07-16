#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime, timedelta

UPDATE_TIME = (2, 0)  

def seconds_until(hour, minute):
    now = datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if target <= now:
        target += timedelta(days=1)

    return (target - now).total_seconds()

while True:
    wait = seconds_until(*UPDATE_TIME)

    print(f"Waiting {wait / 3600:.2f} hours until update...")
    time.sleep(wait)

    print("Downloading updates...")

    subprocess.run(
        ["sudo", "pacman", "-Syyu", "--noconfirm"],
        check=False,
    )

    print("Done. Waiting for tomorrow...")
