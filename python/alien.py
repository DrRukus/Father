#!/usr/bin/env python

wordLength = 3
numberOfWords = 5
words = ['abc', 'bca', 'dac', 'dbc', 'cba']
#words = None

tests = ['(ab)(bc)(ca)',
         'abc',
         '(abc)(abc)(abc)',
         '(zyx)bc']

def alien(words, wordLength, test):
    assert words

    listFlag = False
    tempList = []
    partList = []

    for char in test:
        if char == '(':
            listFlag = True
        elif char == ')':
            listFlag = False
            partList.append(tempList)
            tempList = []
        elif listFlag:
            tempList.append(char)
        else:
            partList.append(char)
 
    assert len(partList) == wordLength

    wordCount = 0
    for word in words:
        letterCount = 0
        for index in range(0, wordLength):
            if word[index] in partList[index]:
                letterCount += 1
        if letterCount == wordLength:
            wordCount += 1

    return wordCount                    

for index in range(0, len(tests)):
    print "Case #{0}: {1}".format(index + 1, alien(words, wordLength, tests[index]))
