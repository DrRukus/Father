#!/usr/bin/env python

wordLength = 3
numberOfWords = 5
words = ['abc', 'bca', 'dac', 'dbc', 'cba']

test = '(ab)(bc)(ca)'
#test = 'abc'
numberOfGroups = test.count('(')
if not numberOfGroups:
    numberOfGroups = 1

listFlag = False
combos = []
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
    partList.append(test)

print partList

for smlist in partList:
    for i in range(0, len(smList)):
       
        
