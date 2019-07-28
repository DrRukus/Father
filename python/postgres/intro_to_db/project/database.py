#!/usr/bin/env python

from psycopg2 import pool


class Database(object):

    __connection_pool = None

    @classmethod
    def initialize(cls,
                   **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(minconn=1,
                                                          maxconn=10,
                                                          **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        cls.__connection_pool.closeall()


class CursorFromConnectionFromPool(object):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value is not None:
            print(exception_value)
            print(traceback)
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
