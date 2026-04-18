import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Smart E-LKPD Matematika", page_icon="🌱")

st.title("🌱 Smart E-LKPD: Personalized Math Learning")
st.write("Inovasi Pembelajaran Digital Ramah Lingkungan berbasis Data Mining")

# --- Bagian Input Data (Simulasi Identifikasi Gaya Belajar VAK) ---
st.header("1. Identifikasi Profil Belajar")
st.info("Siswa mengisi kuesioner singkat untuk menentukan gaya belajar terbaik.")

with st.expander("Klik untuk isi data gaya belajar"):
    v = st.slider("Seberapa suka kamu belajar dengan Gambar/Video? (Visual)", 0, 10, 5)
    a = st.slider("Seberapa suka kamu belajar dengan Mendengarkan? (Auditori)", 0, 10, 5)
    k = st.slider("Seberapa suka kamu belajar dengan Praktik/Gerak? (Kinestetik)", 0, 10, 5)

# --- Proses Data Mining (K-Means Clustering) ---
# Data dummy untuk 'melatih' cluster sederhana
X = np.array([[10, 2, 2], [2, 10, 2], [2, 2, 10], [8, 3, 3], [3, 8, 3], [3, 3, 8]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Prediksi cluster untuk input siswa
user_data = np.array([[v, a, k]])
cluster_result = kmeans.predict(user_data)[0]

# --- Output Diferensiasi (Smart E-LKPD) ---
st.header("2. Materi Terpersonalisasi (Smart Content)")

if cluster_result == 0: # Cluster Visual
    st.success("Tipe Belajar: **Visual**")
    st.write("### 📐 Materi: Geometri Bidang Datar")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Ganti dengan link video edukasi
    st.write("Silakan amati infografis di bawah ini untuk memahami konsep luas.")

elif cluster_result == 1: # Cluster Auditori
    st.success("Tipe Belajar: **Auditori**")
    st.write("### 📐 Materi: Logika Matematika")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Ganti dengan link podcast edukasi
    st.write("Dengarkan penjelasan konsep implikasi melalui audio di atas.")

else: # Cluster Kinestetik
    st.success("Tipe Belajar: **Kinestetik**")
    st.write("### 📐 Materi: Statistik Terapan")
    st.write("Ayo lakukan simulasi interaktif! Geser slider di bawah untuk melihat perubahan grafik secara real-time.")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Data A', 'Data B', 'Data C'])
    st.line_chart(chart_data)

# --- Sisi Green Competition ---
st.sidebar.header("Green Impact")
st.sidebar.write("""
- **Zero Paper:** Mengeliminasi penggunaan LKS cetak.
- **Efisiensi Energi:** Konten yang presisi mengurangi waktu penggunaan perangkat yang sia-sia.
- **Sustainable Edu:** Digitalisasi pendidikan yang inklusif.
""")
