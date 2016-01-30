#!/usr/bin/env python

#import bases

wordLength = 3
numberOfWords = 5
words = ['abc', 'bca', 'dac', 'dbc', 'cba']
#words = ['abc', 'bca']

#test = '(abc)(abc)(abc)'
#test = '(ab)(bc)(ca)'
#test = 'abc'
test = '(zyx)bc'
numberOfGroups = test.count('(')
if not numberOfGroups:
    numberOfGroups = 1

listFlag = True
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
    for letter in test:
        partList.append(letter)

print partList

assert len(partList) == wordLength

wordCount = 0
for word in words:
    letterCount = 0
    for index in range(0, wordLength):
        print "Letter: {0}; Part: {1}".format(word[index], partList[index])
        if word[index] in partList[index]:
            print "Got here"
            letterCount += 1
    print letterCount
    if letterCount == 3:
        wordCount += 1

print wordCount                    
