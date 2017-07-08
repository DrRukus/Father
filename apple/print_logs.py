#!/usr/bin/env python

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
