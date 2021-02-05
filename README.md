# Graduate_Admissions

[![GitHub stars](https://img.shields.io/github/stars/Agrover112/Graduate_Admissions_Prediction)](https://github.com/Agrover112/Graduate_Admissions_Prediction/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Agrover112/Graduate_Admissions_Prediction)](https://github.com/Agrover112/Graduate_Admissions_Prediction/network)
[![GitHub license](https://img.shields.io/github/license/Agrover112/Graduate_Admissions_Prediction)](https://github.com/Agrover112/Graduate_Admissions_Prediction/blob/main/LICENSE)

A Streamlit❤️ web app that predicts the chance of admission into masters program based on various factors using a Flask API  with Catboost model running as a background process on Windows .


<img src="https://github.com/Agrover112/Graduate_Admissions_Prediction/blob/main/Main_Page.png" alt="Main Page" style="height: 100px; width:100px;"/>


# Features 

Refer demo video.

[![Demo Video](http://img.youtube.com/vi/fjgICznjG2Q/0.jpg)](http://www.youtube.com/watch?v=fjgICznjG2Q "")


# Installing packages

```
python -m pip install requirements.txt
```


# How to Run
To run the API as a background process on Windows follow the  instructions mentioned [here](https://towardsdatascience.com/deploying-flask-on-windows-b2839d8148fa)
or one could open another console using```tmux``` or in ```VSCode```.
Run this file which serves as the entry-point to the ```Streamlit``` frontend
```
streamlit run streamlit_app.py
```
