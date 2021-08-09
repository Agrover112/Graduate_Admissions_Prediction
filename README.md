# Graduate_Admissions
*Project no longer being maintained*

*Refer [report](report/Report.pdf) for details such as architecture,methdology,etc.*

A Streamlit❤️ web app that predicts the chance of admission into masters program based on various factors using a Flask API  with Catboost model running as a background process on Windows .

<img src="https://github.com/Agrover112/Graduate_Admissions_Prediction/blob/main/Main_Page.png" alt="Main Page" style="height: 100px; width:100px;"/>

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
Following code Boldy assumes the use of Windows. Since a Windows process is being spawned for the REST api serving. Also all file path need to be changed to match your dir structure.
