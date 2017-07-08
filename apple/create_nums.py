#!/usr/bin/env python

with open('Numbers.txt', 'w+') as f:
    for num in range(101):
        f.write('{}\t'.format(num) if num % 5 != 0 else '*\t')
        if num % 10 == 0:
            f.write('\n')
