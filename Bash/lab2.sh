#!/bin/bash

echo 'Please enter a directory name.'
read NEWDIR
mkdir /home/dschmidt/$NEWDIR
cd /home/dschmidt/$NEWDIR
pwd
touch file1.new
touch file2.new
ls -l
echo 'Contents of first file...' > file1.new
echo 'Contents of second file...' > file2.new
cat file1.new
cat file2.new
echo 'Goodbye, bitches!'
