#!/usr/bin/env python

from bases import IntegerBaseConverter

base = 2
for number in range(0, 65):
    newNumber = IntegerBaseConverter(number, base)

    print newNumber
