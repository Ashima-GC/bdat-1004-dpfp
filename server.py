import pymongo
import pandas as pd
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from datetime import datetime
import json

app = Flask(__name__)
# Route for index.html (Home Page)
@app.route('/')
def index():
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb+srv://ganesh:group54@cluster0.fsvkohb.mongodb.net/')
    # Access the database and collection
    db = client['StockDB']
    collection3 = db['Table']
    data_3 = collection3.find()
    data_list = list(data_3)
    data = pd.json_normalize(data_list[:10])
    data = data.round(1)
    data = data.drop("_id", axis =1)
    json_string = data.to_json()
    

    return render_template('/index1.html', tabledata=json_string)

@app.route('/Monthly Analysis')
def Monthly():
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb+srv://ganesh:group54@cluster0.fsvkohb.mongodb.net/')
    # Access the database and collection
    db = client['StockDB']
    collection2 = db['Monthly_data_2023']
    
    # Query and retrieve data
    data_2 = collection2.find()
    data_list = list(data_2)
    data = pd.json_normalize(data_list)
    data = data.round(1)
    high=[]
    low=[]
    year=[]
    volume_max = []
    volume_min = []
    for index, row in data.iterrows():
        year_value = row['month']
        high_value = row['highest_high']
        low_value = row['lowest_low']
        
        high.append(high_value)
        low.append(low_value)
        year.append(year_value)
    return render_template('/Monthly Analysis.html', high=high,low=low,year=year)

@app.route('/Yearly Analysis')
def Yearly():
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb+srv://ganesh:group54@cluster0.fsvkohb.mongodb.net/')
    # Access the database and collection
    db = client['StockDB']
    collection1 = db['yearly_data']
    collection2 = db['Monthly_data_2023']
    
    # Query and retrieve data
    data_1 = collection1.find()
    data_list = list(data_1)
    data = pd.json_normalize(data_list)
    data = data.round(1)
    high=[]
    low=[]
    year=[]
    volume_max = []
    volume_min = []
    for index, row in data.iterrows():
        year_value = row['year']
        high_value = row['highest_high']
        low_value = row['lowest_low']
        
        high.append(high_value)
        low.append(low_value)
        year.append(year_value)
    return render_template('/Yearly Analysis.html', high=high,low=low,year=year)


if __name__ == "__main__":
    app.run()