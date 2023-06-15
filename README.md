# Graduate_Admissions
*Project abandoned :(*

**Retrospection:**
- The dataset collected is prone to heavy representational biases. Moreover, simplifying prediction of Likelihood of being admitted to a Graduate School based on Test Scores and Proxy such as GPA is a form of Measurement Bias. The data fails to reflect and/or consider multiple factors such as  Net Finnancial Income, Deomgraphic,etc. Even then it would lend itself to Learning bias due to Representational/Sampling issues arising from data collected. EX: If factors such as age,gender, ethnicity are used then surely presence of a certain demographic will outweight others, this in-turn will lead to bias in our models by scoring similar candidates but with differrent backgrounds differently.
- Its been proven that factors such as GPA, Test Scores,etc are bad predictors of success both at finishing university as well as success outside university.
- A Complex model such as XGBoost/CatBoost will overfit and be biased. Simple estimators such as Linear Models or Decision Tree based models are better alternatives.
- From an ethical perspective the given dataset seems fit only for Statistical Analysis not for Predictive Analytics as it would lend to Deployment Biase.



*Refer [report](report/Report.pdf) for details such as architecture,methdology,etc.*

A Streamlit❤️ web app that predicts the chance of admission into masters program based on various factors using a Flask API  with Catboost model running as a background process on Windows .


<img src="https://github.com/Agrover112/Graduate_Admissions_Prediction/blob/main/Main_Page.png" alt="Main Page" style="height: 600px; width:1000px;"/>

## Demo

Refer demo video.

[![Demo Video](http://img.youtube.com/vi/fjgICznjG2Q/0.jpg)](http://www.youtube.com/watch?v=fjgICznjG2Q "")

## Getting Started

```
python -m pip install -r requirements.txt
```

## How to Run
To run the API as a background process on Windows follow the  instructions mentioned [here](https://towardsdatascience.com/deploying-flask-on-windows-b2839d8148fa)
or one could open another console using `tmux` or in `VSCode`.
Run this file which serves as the entry-point to the `Streamlit` frontend.
```
streamlit run streamlit-app/streamlit_app.py
```

### NOTE:
Following code boldy assumes the use of Windows. Since a Windows process is being spawned for serving the REST api. Also all file path need to be changed to match your dir structure.

