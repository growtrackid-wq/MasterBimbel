import streamlit as st

# 1. Konfigurasi Dasar Halaman Utama
st.set_page_config(page_title="Masterbimbel - Dashboard", page_icon="🩺", layout="wide")

# Menghilangkan sidebar bawaan Streamlit agar tampilan lebih bersih
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# 2. Definisikan Halaman-Halaman Menu
tentang_kami_page = st.Page("pages/tentang_kami.py", title="Tentang Kami", icon="🏢")
materi_page = st.Page("pages/materi.py", title="Materi", icon="📚")
testimoni_page = st.Page("pages/testimoni.py", title="Testimoni", icon="⭐")
faq_page = st.Page("pages/faq.py", title="FAQ", icon="❓")
kontak_page = st.Page("pages/kontak.py", title="Kontak", icon="📞")
kebijakan_page = st.Page("pages/kebijakan.py", title="Kebijakan Privasi", icon="🛡️")

# Inisialisasi navigasi dalam posisi "hidden" (sembunyi), karena kita akan pakai tombol custom
pg = st.navigation(
    [tentang_kami_page, materi_page, testimoni_page, faq_page, kontak_page, kebijakan_page], 
    position="hidden"
)

# 3. Header Kanan Atas (Logo di kiri, Menu & Tombol Auth di kanan)
col_logo, col_space, col_menu, col_auth = st.columns([2, 3, 2, 2.5])

with col_logo:
    try:
        st.image("logo.png", width=150)
    except:
        st.subheader("🔺 MASTER BIMBEL")

with col_menu:
    # Menu Dropdown di Sebelah Kanan Atas
    with st.popover("☰ Menu", use_container_width=True):
        if st.button("🏢 Tentang Kami", use_container_width=True):
            st.switch_page("pages/tentang_kami.py")
        if st.button("📚 Materi", use_container_width=True):
            st.switch_page("pages/materi.py")
        if st.button("⭐ Testimoni", use_container_width=True):
            st.switch_page("pages/testimoni.py")
        if st.button("❓ FAQ", use_container_width=True):
            st.switch_page("pages/faq.py")
        if st.button("📞 Kontak", use_container_width=True):
            st.switch_page("pages/kontak.py")
        if st.button("🛡️ Kebijakan Privasi", use_container_width=True):
            st.switch_page("pages/kebijakan.py")

with col_auth:
    col_masuk, col_daftar = st.columns(2)
    with col_masuk:
        st.button("Masuk", use_container_width=True)
    with col_daftar:
        st.button("Daftar", type="primary", use_container_width=True)

st.divider()

# 4. Jalankan Halaman Aktif yang Dipilih User
pg.run()
