#!/usr/bin/env python

words = ['abc', 'bca', 'dac', 'dbc', 'cba']

test = '(ab)(bc)(ca)'
#test = 'abc'

listFlag = False
tempList = []
partList = []

if '(' in test:
    for char in test:
        if char == '(':
            listFlag = True
            continue
        elif char == ')':
            listFlag = False
        if listFlag:
            tempList.append(char)
        else:
            partList.append(tempList)
            tempList = []
        #print tempList
else:
    print 'Seriously?'

print partList

combos = []

for smlist in partList:
    for i in range(0, len(smList):
        
