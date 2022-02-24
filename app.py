from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.thhpe.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mbti", methods=["GET"])
def mbti_get():
    mbti_list = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'mbtis':mbti_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
