#!/bin/bash
func1() {
    echo 'This is from function 1'
}

func2() {
    echo 'This is from function 2'
}

func3() {
    echo 'This is from function 3'
}

echo 'Enter a number (1-3)'
read inp

re='^[1-3]+$'

if ! [[ $inp =~ $re ]] ; then
    echo 'Error: invalid entry.  Must be 1, 2, or 3' >&2 ; exit 1
else
    func$inp
fi
