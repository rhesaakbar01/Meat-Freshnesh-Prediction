import pandas as pd
import streamlit as st
import eda
import prediction
from PIL import Image
page = st.sidebar.selectbox('Choose Page:', ('Landing Page','Data Explorasi','Data Prediksi'))

if page == 'Landing Page':
    st.title('Graded Challenge 7')
    st.title('Deep Learning')
    st.write('')
    st.image('meat.jpg')
    st.write('')
    st.write('Name : Rhesa Akbar Elvarettano')
    st.write('Batch : SBY-003')
    st.write('Objective: Dalam project ini membuat model menggunakan deep learning untuk mengklasifikasikan gambar daging sesuai kelasnya yaitu kelas fresh, half & spoiled.')
    st.write('')
    st.write('Please select menu on the left bar !')
    st.write('')
elif page == 'Data Explorasi':
    eda.run()
else:
    prediction.run()