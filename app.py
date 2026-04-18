import streamlit as st
import base64
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# 1. Konfigurasi Halaman & Portrait Mode
st.set_page_config(page_title="ClusMath", page_icon="🌿", layout="centered")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    # Menggunakan gambar background yang sudah diupload ke GitHub
    bin_str = get_base64_of_bin_file('background_hijau.jpg') 
    
    page_bg_img = f'''
    <style>
    .block-container {{
        max-width: 450px !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        margin-top: 30px;
        margin-bottom: 30px;
    }}

    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .judul-utama {{
        font-size: 60px;
        font-weight: 900;
        color: #1a531c;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
    }}
    
    .sub-judul {{
        font-size: 20px;
        color: #2e7d32;
        text-align: center;
        font-weight: bold;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ Background tidak ditemukan, menggunakan mode standar.")

# --- Tampilan Utama ---
st.markdown('<div class="judul-utama">ClusMath</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-judul">🌿 Smart E-LKPD Aritmetika Sosial 🌿</div>', unsafe_allow_html=True)
st.write("---")

# --- Identitas Siswa ---
st.markdown("### 👤 Identitas")
nama = st.text_input("Nama Lengkap")
kelas = st.text_input("Kelas")

# --- Tes Gaya Belajar VAK ---
st.markdown("### 🧠 Tes Gaya Belajar")
st.write("Isilah kuesioner singkat berikut sesuai dirimu (Skala 0-10):")

with st.container():
    score_v = st.slider("Seberapa mudah kamu memahami materi melalui Gambar/Grafik? (Visual)", 0, 10, 5)
    score_a = st.slider("Seberapa suka kamu mendengarkan penjelasan langsung/rekaman? (Auditori)", 0, 10, 5)
    score_k = st.slider("Seberapa suka kamu belajar sambil mempraktikkan/bergerak? (Kinestetik)", 0, 10, 5)

st.write("")

# --- Tombol Proses Clustering ---
if st.button("🚀 Analisis Profil Belajar", use_container_width=True):
    if nama and kelas:
        # 1. Menyiapkan Mesin K-Means (Logic Data Mining)
        # Kita buat 3 pusat klaster (Centroid) sebagai referensi ideal V, A, dan K
        # Format: [Skor Visual, Skor Auditori, Skor Kinestetik]
        centroids = np.array([
            [10, 2, 2], # Ideal Visual
            [2, 10, 2], # Ideal Auditori
            [2, 2, 10]  # Ideal Kinestetik
        ])
        
        # Inisialisasi model dengan 3 klaster
        model = KMeans(n_clusters=3, init=centroids, n_init=1)
        model.fit(centroids) # 'Melatih' model dengan titik ideal
        
        # 2. Input data siswa
        data_siswa = np.array([[score_v, score_a, score_k]])
        
        # 3. Prediksi Cluster (Clustering Proses)
        cluster = model.predict(data_siswa)[0]
        
        st.balloons()
        st.success(f"Analisis Selesai! Berikut profil belajarmu, {nama}:")

        # --- Hasil Skoring & Rekomendasi ---
        col1, col2, col3 = st.columns(3)
        col1.metric("Visual", score_v)
        col2.metric("Auditori", score_a)
        col3.metric("Kinestetik", score_k)

        if cluster == 0:
            st.info("🎯 **Gaya Belajar: VISUAL**")
            st.write("Kamu akan lebih cepat paham materi Aritmetika Sosial melalui **Infografis, Video, dan Diagram warna-warni**.")
        elif cluster == 1:
            st.info("🎯 **Gaya Belajar: AUDITORI**")
            st.write("Kamu akan lebih nyaman belajar melalui **Penjelasan Suara, Diskusi, dan Podcast Matematika**.")
        else:
            st.info("🎯 **Gaya Belajar: KINESTETIK**")
            st.write("Kamu cocok belajar materi ini melalui **Simulasi Jual-Beli Interaktif dan Praktik Langsung**.")
            
        st.write("---")
        st.button("📖 Masuk ke Materi E-LKPD")
        
    else:
        st.error("Silakan isi Nama dan Kelas terlebih dahulu!")
