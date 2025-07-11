# Don't Remove Credit Tg - @AndySX25

import time
import math
import os
import asyncio
from datetime import datetime,timedelta
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def hrb(value, digits= 2, delim= "", postfix=""):
    """Return a human-readable file size."""
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision = 0):
    """Return a human-readable time delta as a string."""
    pieces = []
    value = timedelta(seconds=seconds)
    
    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])

timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "🟢" * completed_length + "🔴" * remaining_length
                
            try:
                await reply.edit(
                    f'</b>╭──⌯════🌟 UPLOADING 🌟═════⌯──╮\n'
                    f'├⚡ {progress_bar}\n'
                    f'├🚀 Speed ➠ {sp}\n'
                    f'├📛 Progress ➠ {perc}\n'
                    f'├📟 Loaded ➠ {cur}\n'
                    f'├🧲 Size ➠ {tot}\n'
                    f'├🕑 ETA ➠ {eta}\n'
                    f'╰─══👨🏻‍💻 AndySX 👨🏻‍💻══─╯</b>'
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"Progress bar update failed: {e}")
