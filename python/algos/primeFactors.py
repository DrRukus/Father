#!/usr/bin/env python

# lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
#              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
#              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
#              167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
#              229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
#              283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
#
# #num = 26352718
# num = 600851475143
#
# def isPrime(num):
#     numberOfFactors = 0
#     for n in range(1, num + 1):
#         if num % n == 0:
#             numberOfFactors += 1
#     return numberOfFactors == 2
#
# def getPrimeFactors(num):
#     factors = set()
#     if not isPrime(num):
#         for n in range(1, num):
#             if n % 5 == 0:
#                 continue
#             if num % n == 0 and isPrime(n):
#                     factors.add(n)
#     else:
#        factors.update({1, num})
#     return sorted(factors)
#
# def getMaxPrimeFactor(num):
#     return max(getPrimeFactors(num))
#
# print(getMaxPrimeFactor(num))
#n = 13195
n = 26352718
#n = 600851475143
i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print (n)
