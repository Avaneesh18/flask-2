from flask import Flask,jsonify,request
import csv
import pandas as pd
import numpy as np 

with open('shared_articles.csv' , encoding='utf-8')as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
    all_articles = data[1:] 

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route('/flask-mk-2')

def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-movie",methods = ["POST"])

def liked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_movies.append(articles)

    return jsonify({
        "status": "success"
    }),201

def not_liked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)

    return jsonify({
        "status": "success"
    }),201

if __name__ == '__main__':
   app.run()

#-----------------------------------------------------------------

from content_filtering.py import get_recommendation()
from demographic_filtering.py import df
from demographic_filtering.py import 
from storage.py import not_liked_articles
from storagre.py import liked_articles 
