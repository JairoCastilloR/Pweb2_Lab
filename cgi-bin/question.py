#!/usr/bin/python3
import sqlite3
import json

#
conection = sqlite3.connect('imdb.db')
c = conection.cursor()

names = "SELECT * FROM actor"
#movies = "SELECT moviesID,|| ','|| title || ' is of the year ' || year AS "Movies at year ",score ||' with those votes ' || votes AS "Movies Scores " FROM movie"
#I put a variable extremely large for test
#casting = "SELECT movieid , actorid FROM casting"
movie =  "SELECT * FROM movies"

data = []

for row in c.execute(movie):
    data.append({
        'id_movie' : row[0],
        'name_movie' : row[1],
        'year' : row[2],
        'score' : row[3],
        'votes' : row[4],
        })
    print(row)

conection.close()

print("Content-type :application/json\n\n")
print(json.dumps(data))
