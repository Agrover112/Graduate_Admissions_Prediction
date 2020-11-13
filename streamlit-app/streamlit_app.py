import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from page import Components ,Sections
st.beta_set_page_config(page_title='UROPX-GradAmdissions',page_icon='https://avatars2.githubusercontent.com/u/62988119?s=200&v=4')
image_1=Image.open('D:\\ANKIT\\GraduateAdmissions\\streamlit-app\\img\\Graduate-Admissions_blue.png')
#PAGE_CONFIG={'page_title':'UROPX-GradAmdissions'}





cols=st.beta_columns([1,5,1])
cols[1].image(image_1,use_full_column_width=True,width=700)
st.title("Graduate Admission's Analysis ")

#bc_2.image('streamlit-app//img//Graduate-Admissions_blue.png')


pg=Sections()
pg.sections(Components.sidebar() )
Components.page_ending()

##val=st.beta_color_picker('chose')
#print(val)