#!/usr/bin/env python

#import bases

wordLength = 3
numberOfWords = 5
words = ['abc', 'bca', 'dac', 'dbc', 'cba']
#words = ['abc', 'bca']

tests = ['(ab)(bc)(ca)',
         'abc',
         '(abc)(abc)(abc)',
         '(zyx)bc']

def alien(test):
    numberOfGroups = test.count('(')
    if not numberOfGroups:
        numberOfGroups = 1

    listFlag = False
    combos = []
    tempList = []
    partList = []

    for char in test:
        if char == '(':
            listFlag = True
            continue
        elif char == ')':
            listFlag = False
            partList.append(tempList)
            tempList = []
            continue
        elif listFlag:
            tempList.append(char)
        else:
            partList.append(char)
            #tempList = []
        #print tempList

    #print partList
 
    assert len(partList) == wordLength

    wordCount = 0
    for word in words:
        letterCount = 0
        for index in range(0, wordLength):
            #print "Letter: {0}; Part: {1}".format(word[index], partList[index])
            if word[index] in partList[index]:
                #print "Got here"
                letterCount += 1
        #print letterCount
        if letterCount == 3:
            wordCount += 1

    return wordCount                    

for index in range(0, len(tests)):
    print "Case #{0}: {1}".format(index + 1, alien(tests[index]))
