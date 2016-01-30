#!/usr/bin/env python

#message = "goodbye world"
#correctCode = "4666 66632299933096667775553"
message = "hello world"
correctCode = "4433555 555666096667775553"
codeDef = {"2": "abc",
           "3": "def",
           "4": "ghi",
           "5": "jkl",
           "6": "mno",
           "7": "pqrs",
           "8": "tuv",
           "9": "wxyx",
           "0": " "}
letterIndex = 0
currentDigit = None
code = ""
foundLetter = False

for letter in message.lower():
    for codeDigit, codeString in codeDef.iteritems():
        for i in range(0, len(codeString)):
            if codeString[i] == letter:
                if currentDigit == codeDigit:
                    code += " "
                currentDigit = codeDigit
                letterIndex = i + 1
                foundLetter = True
                break
        if foundLetter:
            break
    for i in range(0, letterIndex):
        code += currentDigit
    foundLetter = False

print "Code:         " + code
print "Correct Code: " + correctCode
