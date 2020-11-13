import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
@st.cache(persist=True)
def load_data():
   df=pd.read_csv('D:\ANKIT\GraduateAdmissions\data\Admission_Predict_Ver1.1.csv')
   return df

def gpa_chance(df):   
    sns.set_style('white')
    sns.scatterplot(x='CGPA',y='Chance of Admit ',data=df,size='Chance of Admit ',palette=sns.color_palette("coolwarm",5),hue='University Rating')
    sns.despine()
    st.pyplot()

def res_chance(df):
    sns.set_style('white')
    sct=sns.scatterplot(x='CGPA',y='Chance of Admit ',data=df,size='Research',palette=sns.dark_palette('purple',2),hue='Research',alpha=0.7)
    sct.axes.hlines(y=0.65, xmin=0, xmax=10, linewidth=5, color='r',alpha=0.7,linestyles='--', lw=1)
    sns.despine()
    st.pyplot()

def res_focus(df):  
    sns.set_style('white')
    sns.distplot(df.Research,label='RRRR',kde=False,color='r')
    sns.despine()
    st.pyplot()






"""
So there were 184 different CPGA values due to various factors namely:

considering CGPA values were not rounded to nearest decimal place leading to such similar scores
Dataset is of 500 entries which is a good representation ,but not necessarily extremely accurate

There ,might be many variations in larger datasets due to shear student variety such as increase in number of students with lesser CGPA but with better potential getting accepted. i.e more density increase in head and tail possibly. Obviously, there are more anomalies and outlies.
"""


def cgpa_dist(df):
    sns.set_style('white')
    sns.distplot(df.CGPA,bins=20, color="purple")
    sns.despine()
    st.pyplot()
def cgpa_mean_var(df):
    st.write("Mean CGPA:",round(df.CGPA.mean()*10),"Variance in CGPA is by",round(df.CGPA.var()*10),"%")
    st.write("Mode are :",df.CGPA.mode())

def cgpa_unique(df):
    unique_Uni=list(set(df['University Rating'].values))
    unique_CGPA=list(set(df['CGPA'].values))
    st.write("Number of unique universites ",len(unique_Uni),"and CGPA's",len(unique_CGPA))

def toefl_dist(df):
    sns.set_style('white')
    sns.distplot(df['TOEFL Score'],bins=20, color="green")
    sns.despine()
    st.pyplot()

def gre_dist(df):
    sns.set_style('white')
    sns.distplot(df['GRE Score'],bins=15, color="red")
    sns.despine()
    st.pyplot()
    

def lor_dist(df):
    sns.set_style('white')
    sns.distplot(df['LOR '],bins=5, color="red")
    sns.despine()
    st.pyplot()

def res_(df):
    return len(df[(df['Research']==1) & (df['Chance of Admit ']>0.7)])

def corr(df):
    mask = np.zeros_like(df.corr().values)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        sns.heatmap(df.corr(),annot=True,mask=mask)
        st.pyplot()


def cgpa_rel_GRE(df):
    sns.set_style('white')
    sns.regplot(x="GRE Score", y="CGPA", data=df,color='red')
    plt.title("GRE Score vs CGPA")
    sns.despine()
    st.pyplot()


def GRE_rel_LOR(df):
    sns.set_style('white')
    sns.lmplot(x="GRE Score", y="LOR ", data=df, hue="Research")
    plt.title("GRE Score vs CGPA")
    st.pyplot()

