#!/usr/bin/python3
import sqlite3
import json

#
conection = sqlite3.connect('imdb.db')
c = conection.cursor()

for row in c.execute('SELECT * FROM actor'):
    print(row)
conection.close()

print("Content-type :application/json\n\n")
