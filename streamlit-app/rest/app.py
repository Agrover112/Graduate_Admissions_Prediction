from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.linear_model import Lasso,Ridge,BayesianRidge,ElasticNet,LinearRegression

import pandas as pd
import numpy as np

import sys
sys.path.insert(1, 'streamlit-app')

import logging

from gpa import load_data

#import joblib
import json
import flask
from flask import Flask,request
app=Flask(__name__)

FILE_NAME='D:\ANKIT\GraduateAdmissions\catboost_model.sav'
df=load_data()
model=None

logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(name)s %(threadname)s : %(message)s")
#print("Data loading.........","\nEmpty model object instantiated....")
logging.info("** ---------------LOGS----------------**")
logging.info("** ---------------****----------------**")
logging.info("** Data loading.........")
logging.info("** Empty model object instantiated....")




def preprocess():
    """
    Splits and drops categorical and predictor features from dataframe
    """
    X = df.drop(['Chance of Admit ','Serial No.'], axis=1).values
    y = df['Chance of Admit '].values
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20, shuffle=False)
    return X_train,X_test, y_train, y_test
def find_min_mse():
    """
    Applies mutiple models and prints list of models with least MSE which is our objective (i.e minimize MSE loss)
    """
    X_train,X_test, y_train, y_test=preprocess()

    models = [['DecisionTree :',DecisionTreeRegressor()],
           ['Linear Regression :', LinearRegression()],
           ['RandomForest :',RandomForestRegressor(n_estimators=150)],
           ['KNeighbours :', KNeighborsRegressor(n_neighbors = 2)],
           ['SVM :', SVR(kernel='linear')],
           ['AdaBoostClassifier :', AdaBoostRegressor(n_estimators=100)],
           ['Xgboost: ', XGBRegressor()],
           ['CatBoost: ', CatBoostRegressor(logging_level='Silent')],
           ['Lasso: ', Lasso()],
           ['Ridge: ', Ridge()],
           ['BayesianRidge: ', BayesianRidge()],
           ['ElasticNet: ', ElasticNet()],
           ]

    print("Mean Square Error...")



    res=[]
    d=[]
    for name,model in models:
        model = model
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        res.append( np.sqrt(mean_squared_error(y_test, predictions)))
        print(name, (np.sqrt(mean_squared_error(y_test, predictions))))
        d.append([np.sqrt(mean_squared_error(y_test, predictions)),name])

    #print(sorted(res))
    for i in d[:]:
        if i[0]==sorted(res)[0]:
            print(i[1])
    
        
def save():
    """
    Method that receives split data and saves the Model as .cbm file
    """
    X_train,_, y_train,__=preprocess()     
    model= CatBoostRegressor(logging_level='Silent')
    model.fit(X_train,y_train)
    model.save_model("D:\ANKIT\GraduateAdmissions\data\catboost",format="cbm")    
    #joblib.dump(model, FILE_NAME)
def load_model():
    """ Function that intializes global model state to that of saved ".cbm "catboost model   
    """
    global model
    model=CatBoostRegressor()
    model.load_model("D:\ANKIT\GraduateAdmissions\data\catboost")







@app.route('/')
def home():
  return {"message":"Welcome to API..."}

@app.route('/predict',methods=['POST'])
def predict():
    if flask.request.method == "POST":
        data = request.json
        inputs=np.array(data['Input'])
        chance=model.predict(data['Input'])[0]
        #print("Chance is :{}%".format(chance))
        app.logger.info(" **Chance :"+str(chance) )
        return {"Chance":chance}


# New users will have to run methods below
#save()
#load_model()
# Some inputs for verifying correct model loading and prediction
#print(model.predict(np.array([[315.0 , 105.0 , 2.0 , 3.0 , 3.0 , 7.5 , 1.0]]))[0])


if __name__=="__main__":
   logging.info("** Loading Catboost model and Flask starting server...")
   logging.info("** Please wait until server has fully started")
   #print("* Loading Catboost model and Flask starting server...","please wait until server has fully started")
   load_model()                                  #<---------Does'nt work when serving with waitress :D
   app.run(debug=False)

