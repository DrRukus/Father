#!/usr/bin/env python

"""
Procedure:
    1. Check contents of "TestLogs" dir and 
       create list of all files with .log extension.
    2. Iterate through list of .log files.
    3. For every file, read lines into list.
    4. Check each line for substring "DeviceInfo".
    5. If substring found, grab 3rd field and print
"""

import os

logDir = 'TestLogs'
logs = [file for file in os.listdir(logDir) if '.log' in file]

for log in logs:
    with open('{}/{}'.format(logDir, log), 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'DeviceInfo' in line:
                try:
                    print line.split('\t')[3]
                except IndexError:
                    print "Input data not formatted properly!"
