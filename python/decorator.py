#!/usr/bin/env python

class Hero(object):
    def __init__(self, name, home_planet):
        self.name = name
        self.home_planet = home_planet

    def __str__(self):
        print "Character Bio:"
        print "====================================="
        print "Name: {0}".format(self.name)
        print "Home Planet: {0}".format(self.home_planet)

spongebob = Hero("Spongebob", "Earth")

print spongebob