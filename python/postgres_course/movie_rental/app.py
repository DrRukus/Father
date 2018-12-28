#!/usr/bin/env python

from user import User
from movie import Movie
"""
user = User('Daniel')

user.add_movie('Diehard', 'Action', True)
user.add_movie('Predator', 'Action', False)
user.add_movie('Total Recall', 'Action', True)
user.add_movie('Gleaming the Cube', 'Action', False)

# print(user.watched_movies())
print(user.movies)
user.save_to_file()
"""

user = User.read_csv('Daniel.csv')

#user.delete_movie('Diehard')

print(user.movies)
