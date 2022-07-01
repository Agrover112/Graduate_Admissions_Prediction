# Graduate_Admissions
*Project abandoned :(*

**Retrospection: Catboost  heavily overfits just as magically as XGBoost despite lower RMSE,Higher Accuracy KFold and further testing is required,
so you are better off using something like an LinearRegression or an LSVM/C
Thanks**

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

