#!/bin/bash
months=('January' 'February' 'March' 'April' \
        'May' 'June' 'July' 'August' \
        'September' 'October' 'November' 'December')

echo 'Enter a month number.'
read num
month_index=$(($num - 1))

echo "Month # $num is ${months[$month_index]}"
