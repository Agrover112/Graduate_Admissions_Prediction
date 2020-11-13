from waitress import serve
import logging
import app 
from app import load_model
if __name__=="__main__":
    logging.info("** Loading Catboost model and Flask starting server...")
    logging.info("** Please wait until server has fully started")
    #print("* Loading Catboost model and Flask starting server...","please wait until server has fully started")
    load_model()
    serve(app.app,host="0.0.0.0",port="8080",threads=6)