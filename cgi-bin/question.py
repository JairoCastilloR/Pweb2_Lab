#!/usr/bin/python3
import sqlite3
import json

#
conection = sqlite3.connect('imdb.db')
c = conection.cursor()

names = "SELECT name FROM actor"
#movies = "SELECT moviesID,|| ','|| title || ' is of the year ' || year AS "Movies at year ",score ||' with those votes ' || votes AS "Movies Scores " FROM movie"
#I put a variable extremely large for test
casting = "SELECT movieid , actorid FROM casting"
movie =  "SELECT title, year, score, votes  FROM movies"
complete = casting + movie + names 
data = []

for row in c.execute(casting):
    data.append({
        'id_movie' : row[0],
        'id_actor' : row[1],
        #'name_movie' : row[2],
        #'year' : row[3],
        #'score' : row[4],
        #'votes' : row[5],
        #'name_actor' : row[6]
        })
    print(row)

conection.close()

print("Content-type :application/json\n\n")
print(json.dumps(data))
