from __future__ import print_function

import os, sys, psutil
from datetime import datetime

dt = datetime.now()

try:
    pid = int(sys.argv[1])
except IndexError:
    pid = os.getppid()

proc_create_timestamp = psutil.Process(pid).create_time()

this_proc_create_timestamp = psutil.Process(os.getpid()).create_time()

delta = datetime.fromtimestamp(this_proc_create_timestamp) - datetime.fromtimestamp(proc_create_timestamp)

milliseconds = delta.seconds * 10.**3 + delta.microseconds / 10.**3
print("%.0f ms" % milliseconds, end='')
