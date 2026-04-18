import streamlit as st
import base64 # Import library tambahan ini

# 1. Konfigurasi Halaman (Wajib paling atas)
st.set_page_config(page_title="ClusMath", page_icon="🌿", layout="centered")

# --- FUNGSI PENTING UNTUK BACKGROUND GAMBAR ---
# Fungsi ini untuk membaca gambar dari GitHub dan mengubahnya jadi kode CSS
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Terapkan background gambar. 
# PASTIKAN NAMA FILE GAMBAR DI SINI SAMA DENGAN YANG KAMU UPLOAD DI GITHUB!
# Contoh di bawah, aku asumsikan nama filenya 'background_hijau.jpg'
try:
    bin_str = get_base64_of_bin_file('background_hijau.jpg') 
    
    # KODE CSS UNTUK MENAMPILKAN BACKGROUND GAMBAR
    page_bg_img = f'''
    <style>
    /* Menargetkan seluruh area aplikasi */
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover; /* Gambar menutupi seluruh layar */
        background-position: center; /* Gambar di tengah */
        background-repeat: no-repeat; /* Gambar tidak berulang */
        background-attachment: fixed; /* Gambar tidak ikut bergeser saat scroll */
    }}
    
    /* Membuat latar belakang area konten sedikit transparan */
    /* Agar teks tetap mudah dibaca di atas gambar */
    .stMarkdown, .stTextInput, .stButton {{
        background-color: rgba(255, 255, 255, 0.7); /* Putih transparan */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }}
    
    /* Desain Judul ClusMath (Tetap Hijau Tua agar kontras) */
    .judul-utama {{
        font-size: 75px;
        font-weight: 900;
        color: #1a531c; /* Hijau yang lebih gelap agar terbaca */
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: -10px;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.5); /* Shadow putih agar pop-out */
        background-color: transparent !important; /* Judul tidak usah pakai kotak putih */
    }}
    
    /* Desain Sub-Judul */
    .sub-judul {{
        font-size: 24px;
        color: #2e7d32;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        background-color: transparent !important;
    }}
    
    /* Desain Ikon Aritmetika Sosial */
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
    # Jika gambar tidak ditemukan di GitHub, gunakan warna hijau solid (back-up)
    st.markdown("""
        <style>
        .stApp { background-color: #f2fbf4; }
        .judul-utama { font-size: 70px; font-weight: 900; color: #2e7d32; text-align: center; }
        .sub-judul { font-size: 22px; color: #4caf50; text-align: center; }
        .ikon-aritmetika { font-size: 45px; text-align: center; letter-spacing: 20px; }
        </style>
    """, unsafe_allow_html=True)
    st.error("⚠️ Gambar background tidak ditemukan di GitHub. Pastikan nama filenya sama!")


# --- Bagian Konten yang Sama Seperti Sebelumnya ---

# Menampilkan Judul & Sub-judul
st.markdown('<div class="judul-utama">ClusMath</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-judul">🌿 Smart E-LKPD Aritmetika Sosial & Data Mining 🌿</div>', unsafe_allow_html=True)

# Elemen Visual Aritmetika Sosial (Emoji)
st.markdown('<div class="ikon-aritmetika">💰 🏷️ 🛒 📈 💸</div>', unsafe_allow_html=True)

st.write("---")

# Form Input Nama dan Kelas (Disusun ke Samping)
st.markdown("### 👤 Silakan Isi Identitasmu")
col1, col2 = st.columns(2)

with col1:
    nama = st.text_input("Nama Lengkap", placeholder="Contoh: Aghniya Izzati")
with col2:
    kelas = st.text_input("Kelas", placeholder="Contoh: VIII A")

st.write("")

# Tombol Aksi
if st.button("🚀 Mulai Belajar Terpersonalisasi", use_container_width=True):
    if nama and kelas:
        st.success(f"Halo, {nama} dari kelas {kelas}! Profil belajarmu sedang dianalisis... (Ini simulasi tempat Clustering K-Means akan berjalan nantinya)")
        st.balloons() # Efek animasi balon
    else:
        st.warning("Eits, pastikan kamu sudah mengisi Nama dan Kelas ya sebelum memulai!")
