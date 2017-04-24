#!/usr/bin/env python

operators = {'+': __add__(),
             '-': __sub__(),
             '*': __mul__(),
             '/': __truediv__()}

def ops(left, right, op):
    return left.operators[op](right)

ops(4, 3, '+')
