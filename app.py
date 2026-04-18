import streamlit as st

# 1. Konfigurasi Halaman (Wajib paling atas)
st.set_page_config(page_title="ClusMath", page_icon="🌿", layout="centered")

# 2. Custom CSS untuk Background Hijau & Desain Font
st.markdown("""
    <style>
    /* Mengubah background utama menjadi hijau muda yang segar */
    .stApp {
        background-color: #f2fbf4; 
    }
    
    /* Desain Judul ClusMath */
    .judul-utama {
        font-size: 70px;
        font-weight: 900;
        color: #2e7d32; /* Hijau tua */
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
        margin-bottom: -15px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Desain Sub-Judul */
    .sub-judul {
        font-size: 22px;
        color: #4caf50;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }
    
    /* Desain Ikon Aritmetika Sosial */
    .ikon-aritmetika {
        font-size: 45px;
        text-align: center;
        letter-spacing: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Menampilkan Header & Judul
st.markdown('<div class="judul-utama">ClusMath</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-judul">🌿 Smart E-LKPD Aritmetika Sosial & Data Mining 🌿</div>', unsafe_allow_html=True)

# 4. Elemen Visual Aritmetika Sosial (Uang, Diskon, Belanja, Profit)
st.markdown('<div class="ikon-aritmetika">💰 🏷️ 🛒 📈 💸</div>', unsafe_allow_html=True)

st.write("---")

# 5. Form Input Nama dan Kelas (Disusun ke Samping)
st.markdown("### 👤 Silakan Isi Identitasmu")
col1, col2 = st.columns(2)

with col1:
    nama = st.text_input("Nama Lengkap", placeholder="Contoh: Aghniya Izzati")
with col2:
    kelas = st.text_input("Kelas", placeholder="Contoh: VIII A")

st.write("")

# 6. Tombol Aksi
if st.button("🚀 Mulai Belajar Terpersonalisasi", use_container_width=True):
    if nama and kelas:
        st.success(f"Halo, {nama} dari kelas {kelas}! Profil belajarmu sedang dianalisis... (Ini simulasi tempat Clustering K-Means akan berjalan nantinya)")
        st.balloons() # Efek animasi balon saat berhasil
    else:
        st.warning("Eits, pastikan kamu sudah mengisi Nama dan Kelas ya sebelum memulai!")
