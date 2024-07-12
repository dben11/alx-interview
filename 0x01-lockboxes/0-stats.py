#!/usr/bin/python3
import sys
import datetime
from time import sleep
import random

#initializing varaibles
total_file_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
}
#Reading the input from the stdin
while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        except keyboardInterruption:
            break
