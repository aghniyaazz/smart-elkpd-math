import streamlit as st

# --- MEMBUAT MENU NAVIGASI DI SAMPING KIRI ---
with st.sidebar:
    st.title("Menu E-LKPD")
    halaman = st.selectbox("Pilih Halaman:", ["Halaman Utama", "LKPD Refleksi"])

# ==========================================
# HALAMAN 1: KODE AWAL KAMU
# ==========================================
if halaman == "Halaman Utama":
    st.title("Materi Awal")
    st.write("Nah, di bagian bawah ini kamu bisa paste atau taruh kode app.py kamu yang awal-awal tadi.")
    
    # [PASTE KODE LAMA KAMU DI SINI]
    # Pastikan penulisan kodenya menjorok ke dalam (di-indent/di-tab) karena berada di bawah blok 'if'


# ==========================================
# HALAMAN 2: LKPD REFLEKSI (CANVA)
# ==========================================
elif halaman == "LKPD Refleksi":
    # CSS untuk mempercantik kotak input
    st.markdown("""
        <style>
        .stTextInput input {
            border-radius: 8px;
            border: 2px solid #8B4513; 
            background-color: white;
            text-align: center;
        }
        .stTextArea textarea {
            border-radius: 10px;
            border: 2px solid #8B4513;
            background-color: #FFF8DC; 
            font-family: sans-serif;
            font-size: 15px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Merakit Bagian 1: Soal Gambar
    st.image("bagian_1.png", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        jawaban_3 = st.text_input("Jawaban Gambar (3)", label_visibility="collapsed") 
    with col2:
        jawaban_4 = st.text_input("Jawaban Gambar (4)", label_visibility="collapsed")
    st.write("") 

    # Merakit Bagian 2: Esai
    st.image("bagian_2.png", use_container_width=True)
    jawaban_esai = st.text_area(
        "Jawaban Esai", 
        label_visibility="collapsed", 
        height=150, 
        placeholder="Ketik jawabanmu tentang Refleksi dengan bahasamu sendiri di sini..."
    )
    st.write("")

    # Merakit Bagian 3: Penutup
    st.image("bagian_3.png", use_container_width=True)

    # Tombol Kirim
    if st.button("Kumpulkan Jawaban"):
        if jawaban_esai:
            st.success("Jawaban refleksi berhasil disimpan! Hebat!")
        else:
            st.warning("Jangan lupa isi penjelasan refleksinya ya.")
