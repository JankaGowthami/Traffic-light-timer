
from flask import Flask,request
app = Flask(__name__)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred


@app.route('/', methods=['GET', 'POST'])
def index():
    dis = int(request.form.get('distance'))
    no = int(request.form.get('no_vehc'))
    day = int(request.form.get('day'))
    time = int(request.form.get('time'))
    age = int(request.form.get('age'))
    purpose = int(request.form.get('purpose'))
    
    
    p = reg('traffic_dataset.csv',["distance","no_vehc","day","time","age","purpose"],"outcome",[dis,no,time,age,purpose])
    print("Bot : The outcome is: ",p)
    
    return p

if __name__ == '__main__':
    app.run(debug=True)