#!/usr/bin/env python

import sqlite3

DATA_DB = 'data/data.db'

def connectToDb():
    cnx = sqlite3.connect(DATA_DB)
    return cnx, cnx.cursor()

def closeDb(cnx, commit=False):
    if commit:
        cnx.commit()
    cnx.close()