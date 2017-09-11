#!/usr/bin/env python

from math import sqrt, pow, floor, log
# from itertools import count, islice
#
# TOP = 20
# MAX = 232792560
#
# def isPrime(num):
#     return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))
#
# def getPrimesInRange():
#     return [x for x in range(2, TOP + 1) if isPrime(x)]
#
# def isNumberDivisible(testNum, verify=False):
#     test = True
#     for multiplier in range(1, TOP + 1):
#         if not verify:
#             if not testNum % multiplier == 0:
#                 test = False
#                 break
#
#     return test
#
# def getMultipliers(quotients):
#     decs = []
#     for qut in quotients:
#         decAbs = str(str(qut).split('.')[-1])
#         dec = float(decAbs) / pow(10, len(decAbs))
#         if dec != 0.0 and dec not in decs:
#             decs.append(dec)
#     print(decs)
#     mults = []
#     for dec in decs:
#         mult = 1.0 / dec
#         if mult not in mults:
#             mults.append(mult)
#     return mults
#
# #check = 2520
# #print(isNumberDivisible(check))
# #print(isPrime(20))
# #print(product)
#
# initTest = 1
# for prime in getPrimesInRange():
#     initTest *= prime
# print(initTest)
#
# quotients = []
# for n in range(1, TOP + 1):
#     quotients.append(float(initTest)/float(n))
#
# print(quotients)
# print(getMultipliers(quotients))



# ans = 0
# for check in range(1, MAX + 1):
#     if isNumberDivisible(check):
#         ans = check
#         break
#
# print('Answer: {}'.format(ans))

k = 20
N = 1
i = 0
check = True
limit = sqrt(k)
p = [2.0, 3.0, 5.0, 7.0, 11.0, 13.0, 17.0, 19.0, 23.0, 29.0, 31.0]

while p[i] <= k:
    a = 1
    if check:
        if p[i] <= limit:
            a = floor(log(k) / log(p[i]))
        else:
            check = False
    N *= p[i] ** a
    i += 1
print(N)