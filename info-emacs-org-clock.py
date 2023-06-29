#!/usr/bin/env python
"""Checks if a task is clocked in in Emacs Org-Mode and displays the time."""
import time
import json
from emacs import EmacsClient
emacs = EmacsClient()


if emacs.eval("(org-clocking-p)") is True:
    task = emacs.eval("(message org-clock-heading)")
    try:
        effort = int(emacs.eval(
            "(org-duration-to-minutes org-clock-effort)"))*60
    except Exception:
        effort = 0
    clock = int(emacs.eval("(org-clock-get-clocked-time)"))*60
    if effort > 0:
        percentage = int(round((clock/effort)*100))
        if percentage > 100:
            percentage = 100
        result = {
            "text": "[{}/{}] {}".format(
                time.strftime("%H:%M", time.gmtime(clock)),
                time.strftime("%H:%M", time.gmtime(effort)),
                task),
            "class": "clockedin",
            "percentage": percentage
        }
    else:
        result = {
            "text":  "[{}] {}".format(
                time.strftime("%H:%M", time.gmtime(clock)),
                task),
            "class": "clockedin",
            "percentage": 100
        }
else:
    result = {
        "text": "---",
        "class": "clockedout"
    }

print(json.dumps(result))
