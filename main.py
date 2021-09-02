from flask import Flask, jsonify, request
import csv

all_movies= []

with open ('movies.csv', 'r', encoding = 'utf-8') as f:
    reader_data = csv.reader (f)
    data = list (reader_data)
    all_movies=data[1:]

liked_movies = []
unliked_movies = []
did_not_watch = []

app = Flask (__name__)

@app.route("/get-movie")

def get_movie ():
    return jsonify({
        "data" : all_movies [0], 
        "status" : "success"
    })

@app.route ("/liked-movie", methods = ["POST"])
def liked_movie ():
    movie = all_movies [0]
    all_movies = all_movies [1:]
    liked_movies.append(movies)
    return jsonify({
        "status" : "success"
    }), 201

@app.route ("/unliked-movie", methods = ["POST"])
def not_liked_movie ():
    movie = all_movies [0]
    all_movies = all_movies [1:]
    unliked_movies.append(movies)
    return jsonify({
        "status" : "success"
    }), 201

@app.route ("/unwatched-movie", methods = ["POST"])
def unwatched_movie ():
    movie = all_movies [0]
    all_movies = all_movies [1:]
    did_not_watch.append(movies)
    return jsonify({
        "status" : "success"
    }), 201

if __name__=="__main__":
    app.run()