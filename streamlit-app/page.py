import streamlit as st
import streamlit.components.v1 as comp
import PIL
from PIL import Image
from dataclasses import dataclass
import requests
from gpa import *
from rest import app
from flask import Flask,request,jsonify
import requests
import json

st.set_option('deprecation.showPyplotGlobalUse', False)
GTHB=Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\GitHub-Mark-32px.png")
MDM=Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\MediumIcon32px.png")
TWT=Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\Twitter-Logo32pxLossless.png")


@dataclass
class Logos:
    GITHUB: PIL.PngImagePlugin.PngImageFile = Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\GitHub-Mark-32px.png")
    MEDIUM:PIL.PngImagePlugin.PngImageFile = Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\MediumIcon32px.png")
    TWITTER:PIL.PngImagePlugin.PngImageFile =Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\Twitter-Logo32pxLossless.png")
    AUTHOR: PIL.PngImagePlugin.PngImageFile = Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\Author.png")
    
RLTY=Image.open("D:\ANKIT\GraduateAdmissions\streamlit-app\img\Realities.PNG")


class Sections:

    def intro(self):
        with st.beta_container():
            cols=st.beta_columns([1,3,1])
            st.markdown('# Introduction')
            st.write("Let's begin our journey today. In this blog I intend to impart imformation about Graduate Admissions")
            st.markdown("""
            ![Should I or Should I not?](https://www.verywellmind.com/thmb/9k_CEmh1VVR7Bug2KL_rUGUPR3w=/768x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/what-happens-when-you-think-4688619_round3_standardsize-9871b8430824491fb39590ef45571de4.gif)""")
            st.markdown("""
            Applying for graduate program can become a bit confusing especially with lot of factors determining your admission.
            It is important to have a crystal clear idea of which program intrigues and suits you the most with your given background and profile.
            One of the first thing's that one should understand when applying for a graduate program is to get accustomed to the variety of  programs in various countries and how each country has a somewhat different take on the same program.
            There are many diverse programs which you should consider. Most graduate programs are often research oriented.
                        
            
            """)
    def lb(self):
        st.title('Reasons for pursuing a Masters')
        with st.beta_container():
            st.markdown("""
            There might be many reasonss why one might want to pursue such a degree.The common one's include:
            - **Deep dive into a particular field**

            A common reason for many aspirant's is striving to know more about a particular field of interst in much more depth. This usually stems
            out of curiosity.
            - **Switching your career**

            Often many aspirants chose to switch their career after exposure to a given field of choice. They might or might not have complete idea of their field of interest , coming from related field .
            This is usually good since such candidates can bring their perspective and expertise(if related) into the current role.
            - **Looking for new  Challenge**

            Many aspirants might be looking to challenge and enhance their skills . It might serve as a personal challenge that they are willing to overcome.
            - **Carrer growth**

            There are many statistics regarding career growth after a Master's degree. Although usuallly such statistics learn towards higher incomes after completion,
            one should not purely base the decision for money's sake.This can end up being dangerous as you might regret doing your job a lot.
            """)
            with st.beta_expander('~Expand more '):
                st.markdown('Well that took a **different turn** altogether😶')
                st.image(RLTY,caption="Funny ")
    def GPA(self):
        with st.beta_container():
            #cols[0].markdown("<img src='https://cdn.dribbble.com/users/3555306/screenshots/6635665/44.jpg' width='700' height='400' />",unsafe_allow_html=True)
            st.markdown("Let's analyze  the given data set of [Graduate Admissions for Masters](https://www.kaggle.com/mohansacharya/graduate-admissions).")
            df=load_data()
            col=st.beta_columns([1,1,1])
            if col[1].checkbox('Press to View Data'):
                st.write(df.head())
            st.markdown("Plot below we can clearly identify that GPA <8 are in danger. Universities seem to favor students with higher CGPA , thus becoming an important factor for applications. However, other factors are important too ")
           

            cols=st.beta_columns([1,1])    
            with cols[0]:    
             gpa_chance(df)
            with cols[1]:
                res_chance(df)
            st.markdown("It's pretty clear that you need  some research experience since most having 65% or greater admit chance all seem to have research experience with exceptions of few.")

            st.markdown('Now we examine the frequency of applicants who had reseach experience. The chart on the right shows the former')
            res_focus(df)
            st.markdown("# Distribution of various features")
            cols=st.beta_columns([1,1])
            with cols[0]:
                cgpa_dist(df)
                gre_dist(df)
                cgpa_mean_var(df)
            with cols[1]:
                toefl_dist(df)
                lor_dist(df)
                cgpa_unique(df)
            st.markdown("""
            It is clear the above features follow a normal distribution , where all are symmetric excpet the last which has a negative skew.
            One can see that applicants try and get more number of LOR's (of good quality) thus trying to maximize their chances.
            Moreover, the CGPA can be clearly seen to vary between 8-9 ,TOEFL of 110-115 and GRE Score of 310 -330
            """)
            st.write("There are ",res_(df),"applications whom have a greater than 70% chance having done some research.")
            st.markdown("# Correlation of Chance of Admit with all factors")
            corr(df)
            st.markdown("One can clearly notice the high importance of standardized tests and CGPA ,besides the importance of a strong clear research goal and LOR.LORs would usually be gained as a result of research experience therefore having a higher impact")
            cols=st.beta_columns([1,1])
            with cols[0]:
                cgpa_rel_GRE(df)
                st.markdown("People with higher CGPA usually have higher GRE scores")
            with cols[1]:
                GRE_rel_LOR(df)
                st.markdown("Less relation between LOR and GRE score since LOR's depend more on research.")


    def prediction(self):
        with st.beta_container():
            st.markdown('Find where you stand')
            gre_score=st.text_input("GRE SCORE")
            if gre_score:
                gre_score=int(gre_score)
            toefl_score=st.text_input("TOEFL SCORE:")
            if toefl_score:
                toefl_score=int(toefl_score)
            univ_rating=st.text_input("University Rating(1.0-5.0):")
            if univ_rating:
                univ_rating=float(univ_rating)
            sop=st.text_input("SOP Strength(1.0-5.0):")
            if sop:
                sop=float(sop)
            lor=st.text_input("LOR Strength(1.0-5.0):")
            if lor:
                lor=float(lor)
            cgpa=st.text_input("CGPA(1.0-10.0):")
            if cgpa:
                cgpa=float(cgpa)
            rsch=st.text_input("Research Done or Not (1/0):")
            if rsch:
                rsch=int(rsch)
            """
            Encountering st.number_input() defaulting to zero bug(proly not fixed in this version)
            gre_score=st.number_input("GRE SCORE:",format="%f",max_value=340.0,step=1.0)
            toefl_score=st.number_input("TOEFL SCORE:",format="%f",max_value=120.0,step=1.0)
            univ_rating=st.number_input("University Rating:",format="%f",min_value=1.0,max_value=5.0,step=0.5)
            sop=st.number_input("SOP Strength",format="%f",max_value=5.0,min_value=1.0,step=0.5)
            lor=st.number_input("LOR Strength",format="%f",max_value=5.0,step=0.5)
            cgpa=st.number_input("CGPA",format="%f",min_value=0.0,max_value=10.0,step=0.01)
            rsch=st.number_input("Research Done or Not ?(1/0)",format="%f",min_value=0.0,max_value=1.0)
            """

            inp_array=np.array([[gre_score,toefl_score,univ_rating,sop,lor,cgpa,rsch]])
            print(inp_array)
            payload={'Input':inp_array.tolist()}
            st.write("Your Input",payload)
            if st.button("Know your chance"):
                response=requests.post("http://DESKTOP-YourDesktopID:8080/predict",json=payload) #change
                #response=requests.post("http://127.0.0.1:5000/predict",json=payload)
                res=json.loads(response.text)
                st.write("Your chance is",res["Chance"],"%")
 

    def sections(self,opt:str):
        if opt =='Intro':
            self.intro()
        if opt == "Let's begin":
            self.lb()
        if opt == 'Does GPA really matter?':
            self.GPA()
        if opt == 'Find where you stand':
            self.prediction()




class Components:
    @staticmethod
    def sidebar():
        with st.beta_container():
            cols=st.sidebar.beta_columns([1,8,1])
            cols[1].image(Logos.AUTHOR,use_column_width=True)
            cols[1].subheader('Agrover112')
            cols[1].write('Humans trying to undestand machines.....🎯')
            opt=cols[1].radio('Sections',['Intro',"Let's begin",'Does GPA really matter?','Find where you stand'],index=0)
        return opt

    @staticmethod
    def page_ending():
        with st.beta_expander("Learn More:"):
            cols=st.beta_columns([1,1,1,1,1])
            cols[2].write('**Contact Author**')
            cols=st.beta_columns([1,1,1,1,1])
            cols[0].image(Logos.GITHUB)
            cols[1].markdown("[Agrover112](https://github.com/Agrover112)")
            cols[0].image(Logos.MEDIUM)
            cols[1].markdown("[@agrover112](https://medium.com/@agrover112)")
            cols[0].image(Logos.TWITTER)
            cols[1].markdown("[@agrover112](https://twitter.com/agrover112)")

            #cols=st.beta_columns([1,1,1])
            cols[4].markdown('@{} UROP-*X*'.format(2020))
            cols[4].markdown('Terms of Use')
            cols[4].markdown('[MIT LICENSE](https://opensource.org/licenses/MIT)')