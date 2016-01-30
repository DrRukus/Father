#!/usr/bin/env python

#C = 100
#numItems = 3
#prices = [5, 75, 25]
#C = 200
#numItems = 7
#prices = [150, 24, 79, 50, 88, 345, 3]
C = 8
numItems = 8
prices = [2, 1, 9, 4, 4, 56, 90, 3]

indices = []

for i in range(0, len(prices)):
    for j in range(i + 1, len(prices)):
        currentSum = prices[i] + prices[j]
        if currentSum == C:
            indices.append(i + 1)
            indices.append(j + 1)

print indices
