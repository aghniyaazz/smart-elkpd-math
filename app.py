import streamlit as st
import base64

# 1. Konfigurasi Halaman (Wajib paling atas)
st.set_page_config(page_title="ClusMath", page_icon="🌿", layout="centered")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    bin_str = get_base64_of_bin_file('background_hijau.jpg') 
    
    # PERHATIKAN: Semua kode CSS harus ada di dalam tanda kutip f''' dan ''' ini
    page_bg_img = f'''
    <style>
    /* 1. Memaksa tampilan menjadi Portrait (seperti layar HP) */
    .block-container {{
        max-width: 450px !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        margin-top: 30px;
        margin-bottom: 30px;
    }}

    /* 2. Menargetkan seluruh area aplikasi untuk Background Gambar */
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* 3. Desain Judul dan Ikon */
    .judul-utama {{
        font-size: 75px;
        font-weight: 900;
        color: #1a531c;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: -10px;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
        background-color: transparent !important;
    }}
    
    .sub-judul {{
        font-size: 24px;
        color: #2e7d32;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        background-color: transparent !important;
    }}
    
    .ikon-aritmetika {{
        font-size: 50px;
        text-align: center;
        letter-spacing: 25px;
        margin-bottom: 30px;
        background-color: transparent !important;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.error("⚠️ Gambar background tidak ditemukan di GitHub. Pastikan nama filenya sama!")


# --- Bagian Konten Selanjutnya (Judul, Form Input, Tombol) ditaruh di bawah sini ---

st.markdown('<div class="judul-utama">ClusMath</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-judul">🌿 Smart E-LKPD Aritmetika Sosial & Data Mining 🌿</div>', unsafe_allow_html=True)
st.markdown('<div class="ikon-aritmetika">💰 🏷️ 🛒 📈 💸</div>', unsafe_allow_html=True)
st.write("---")

st.markdown("### 👤 Silakan Isi Identitasmu")
col1, col2 = st.columns(2)

with col1:
    nama = st.text_input("Nama Lengkap", placeholder="Contoh: Aghniya Izzati")
with col2:
    kelas = st.text_input("Kelas", placeholder="Contoh: VIII A")

st.write("")

if st.button("🚀 Mulai Belajar Terpersonalisasi", use_container_width=True):
    if nama and kelas:
        st.success(f"Halo, {nama} dari kelas {kelas}! Profil belajarmu sedang dianalisis...")
        st.balloons()
    else:
        st.warning("Eits, pastikan kamu sudah mengisi Nama dan Kelas ya sebelum memulai!")
