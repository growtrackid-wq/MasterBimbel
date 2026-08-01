import streamlit as st

# 1. Konfigurasi Dasar
st.set_page_config(page_title="Masterbimbel - Dashboard", page_icon="🩺", layout="wide")

# Styling CSS untuk merapikan tombol menu agar terlihat seperti Navbar profesional
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stSidebar"] {display: none;}
        .block-container { padding-top: 1rem; }

        /* Kustomisasi gaya tombol navigasi */
        div[data-testid="stColumn"] button {
            border: none !important;
            background-color: transparent !important;
            color: #0f172a !important;
            font-weight: 800 !important;
            font-size: 1.5rem !important;
            transition: all 0.2s ease-in-out;
        }
        div[data-testid="stColumn"] button:hover {
            color: #1d4ed8 !important;
            background-color: #f1f5f9 !important;
            border-radius: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Definisikan Halaman Menu
tentang_kami_page = st.Page("pages/tentang_kami.py", title="Tentang Kami", icon="🏢")
materi_page = st.Page("pages/materi.py", title="Materi", icon="📚")
testimoni_page = st.Page("pages/testimoni.py", title="Testimoni", icon="⭐")
faq_page = st.Page("pages/faq.py", title="FAQ", icon="❓")
kontak_page = st.Page("pages/kontak.py", title="Kontak", icon="📞")
kebijakan_page = st.Page("pages/kebijakan.py", title="Kebijakan Privasi", icon="🛡️")

pg = st.navigation(
    [tentang_kami_page, materi_page, testimoni_page, faq_page, kontak_page, kebijakan_page], 
    position="hidden"
)

# 3. Custom Banner Header
banner_url = "https://raw.githubusercontent.com/growtrackid-wq/MasterBimbel/main/pages/banner.jpg"

st.markdown(f"""
    <div style="
        background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{banner_url}');
        background-size: cover;
        background-position: center;
        padding: 2.2rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    ">
        <h1 style="color: white; margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: 1px;">MASTER BIMBEL</h1>
        <p style="color: #f1f5f9; margin: 6px 0 0 0; font-size: 1rem; font-weight: 500;">Belajar Tepat, Lulus Cepat!!</p>
    </div>
""", unsafe_allow_html=True)

# 4. Navbar Horizontal Profesional (Sejajar dalam 1 Baris)
c1, c2, c3, c4, c5, c6, c_space, c_masuk, c_daftar = st.columns([1.2, 1, 1, 0.9, 0.9, 1.4, 1.5, 1, 1])

with c1:
    if st.button("🏢 Tentang", use_container_width=True): st.switch_page("pages/tentang_kami.py")
with c2:
    if st.button("📚 Materi", use_container_width=True): st.switch_page("pages/materi.py")
with c3:
    if st.button("⭐ Testi", use_container_width=True): st.switch_page("pages/testimoni.py")
with c4:
    if st.button("❓ FAQ", use_container_width=True): st.switch_page("pages/faq.py")
with c5:
    if st.button("📞 Kontak", use_container_width=True): st.switch_page("pages/kontak.py")
with c6:
    if st.button("🛡️ Privasi", use_container_width=True): st.switch_page("pages/kebijakan.py")

with c_masuk:
    st.button("Masuk", use_container_width=True)
with c_daftar:
    st.button("Daftar", type="primary", use_container_width=True)

st.divider()

# 5. Jalankan Halaman Aktif
pg.run()
