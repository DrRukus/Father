#!/bin/bash
DATE=$(date +"%Y%m%d%H%M")
cp $1 /home/dschmidt/scripts/backups/$1_$DATE.py
