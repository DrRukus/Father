#!/bin/bash
echo "Please enter the first number: "
read first
echo "Please enter the second number: "
read second
if [ $first -eq 0 ] && [ $second -eq 0 ] ; then
    echo "Both numbers are zero"
elif [ $first -eq $second ] ; then
    echo "Both numbers are equal"
elif [ $first -gt $second ] ; then
    echo "The first number is larger"
else
    echo "The second number is larger"
fi
