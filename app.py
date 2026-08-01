import streamlit as st

# 1. Konfigurasi Dasar Halaman Utama
st.set_page_config(page_title="Masterbimbel - Dashboard", page_icon="🩺", layout="wide")

# 2. Definisikan Halaman-Halaman Menu Sesuai Gambar
tentang_kami_page = st.Page("pages/tentang_kami.py", title="Tentang Kami", icon="🏢")
materi_page = st.Page("pages/materi.py", title="Materi", icon="📚")
testimoni_page = st.Page("pages/testimoni.py", title="Testimoni", icon="⭐")
faq_page = st.Page("pages/faq.py", title="FAQ", icon="❓")
kontak_page = st.Page("pages/kontak.py", title="Kontak", icon="📞")
kebijakan_page = st.Page("pages/kebijakan.py", title="Kebijakan Privasi", icon="🛡️")

# 3. Inisialisasi Navigasi (Bisa ditaruh di Sidebar atau Navbar atas otomatis oleh Streamlit)
pg = st.navigation([tentang_kami_page, materi_page, testimoni_page, faq_page, kontak_page, kebijakan_page])

# 4. Tambahkan Tombol Masuk / Daftar di Bagian Atas
col_logo, col_space, col_auth = st.columns([2, 5, 3])

with col_logo:
    # Menggunakan file logo lokal kamu jika ada, atau teks placeholder sementara
    try:
        st.image("logo.png", width=150)
    except:
        st.subheader("🔺 MASTER BIMBEL")

with col_auth:
    col_masuk, col_daftar = st.columns(2)
    with col_masuk:
        st.button("Masuk", use_container_width=True)
    with col_daftar:
        # Menggunakan format warna bawaan untuk tombol primary
        st.button("Daftar", type="primary", use_container_width=True)

st.divider()

# 5. Jalankan halaman yang sedang aktif dipilih user
pg.run()