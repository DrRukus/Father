#!/usr/bin/env python

import sys

class Movie:
    def __init__(self, name, genre, watched):
        assert type(watched) == bool
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return '<Movie: {}; Watched: {}>'.format(self.name, self.watched)
