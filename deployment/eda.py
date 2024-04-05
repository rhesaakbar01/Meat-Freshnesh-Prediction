import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat Tittle
    st.title('Prediksi Kesegaran Daging')

    # Membuat Sub Header
    st.subheader('Eda untuk menganalisa Dataset Meat Freshness Image mengklasifikasikan daging sesuai kelasnya')

    # Menambahakan Gambar
    st.image('eda_meat.jpg')

    # Menambahkan Deskripsi
    st.write('## WELCOME')
    st.write('Pada page kali ini, penulis akan melakukan ekspolrasi sederhana pada dataset Meat Freshness Image dengan menampilkan beberapa gambar daging yang disesuaikan dengan kelas.')

    # Membuat Garis Lurus
    st.markdown('---')

    # Membuat Countplot
    st.write('### Membuat visualisasi sederhana dari 4 gambar berdasarkan kelasnya')
    fig = plt.figure(figsize=(15, 4))
    st.image('eda_daging.png')
    st.write('## Ciri-ciri:')
    st.write('`Daging Busuk (SPOILED):` Warna secara keseluruhan sudah sangat gelap atau berubah menjadi warna coklat atau hitam & Permukaan daging terlihat sangat kering dan mungkin ada tanda-tanda pertumbuhan jamur atau bakteri.')
    
    # Membuat Garis Lurus
    st.markdown('---')
    st.write('`Daging Segar (FRESH):` Warna cerah dan merata, Permukaan daging tampak lebih berwarna merah cerah, lembab dan berkilau & Tidak ada tanda-tanda busuk atau perubahan warna yang signifikan.')
    
    # Membuat Garis Lurus
    st.markdown('---')
    st.write('`Daging Setengah Segar (HALF):` Warna mungkin sudah mulai gelap atau kusam di beberapa bagian & Permukaan daging mungkin tampak sedikit kering.')
    
    # Membuat Garis Lurus
    st.markdown('---')

if __name__== '__main__':
    run()