#!/bin/python

def makePretty(func):
    def inner():
        print "I got decorated"
        func()
    return inner

@makePretty
def ordinary():
    print "I am ordinary"

ordinary()
print "\nNow we'll decorate the function\n"
#ordinary = makePretty(ordinary)
ordinary()
