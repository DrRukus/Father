#!/bin/bash
# Script to evaluate arithmetic expressions

add() {
    echo $(($1 + $2))
}

subtract() {
    echo $(($1 - $2))
}

multiply() {
    echo $(($1 * $2))
}

divide() {
    echo $(($1 / $2))
}

if [[ $# -eq 3 ]] ; then
    case "$1" in
        "a") add $2 $3 ;;
        "s") subtract $2 $3 ;;
        "m") multiply $2 $3 ;;
        "d") divide $@ $3 ;;
        *) echo 'Invalid entry, sucka!'
    esac
else
    echo 'Invalid number of arguments, bitch!'
fi

