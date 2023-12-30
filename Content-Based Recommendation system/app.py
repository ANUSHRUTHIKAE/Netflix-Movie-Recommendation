from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

movies = pd.read_pickle('Content-Based Recommendation system/movies_list.pkl')
similarity = pd.read_pickle('Content-Based Recommendation system/similarity.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend_books',methods=['post'])
def recommend():
    movie_name = request.form.get('user_input')
    index = movies[movies['original_title']==movie_name].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    data = []
    for i in distance[1:6]:
        data.append(movies.iloc[i[0]].original_title)
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)