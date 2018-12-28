#!/usr/bin/env python

from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def add_movie(self, name, genre, watched=False):
        if type(watched) == str:
            watched = True if watched== 'True' else False
        self.movies.append(Movie(name, genre, watched))

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name,
                                  self.movies))

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def save_to_file(self):
        with open('{}.csv'.format(self.name), 'w') as f:
            f.write(self.name + '\n')

            for movie in self.movies:
                # Create CSV-formated string
                movie_str = '{},{},{}\n'.format(movie.name.replace(' ', '_'),
                                                movie.genre.replace(' ', '_'),
                                                movie.watched)
                f.write(movie_str)

    @classmethod
    def read_csv(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        user = cls(lines[0])
        for movie in lines[1:]:
            user.add_movie(*movie.rstrip('\n').split(','))
        return user
