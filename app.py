import base64
import streamlit as st

# 1. Konfigurasi Dasar
st.set_page_config(page_title="Masterbimbel - Dashboard", page_icon="🩺", layout="wide")

# Fungsi untuk membaca background.jpg lokal dan mengatur CSS responsif
def set_global_background(image_path="background.jpg"):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        
        bg_css = f"""
        <style>
            /* 1. Mengubah Background Utama Seluruh Halaman */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{b64_img}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            /* 2. Memaksa Teks & Judul Tetap Gelap dan Jelas */
            .stApp p, .stApp label, .stApp li {{
                color: #0f172a !important;
            }}
            
            .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
                color: #0f172a !important;
                font-weight: 700 !important;
            }}

            /* 3. Style Khusus Tombol Popover (Menu) */
            div[data-testid="stPopover"] > button {{
                background-color: #ffffff !important;
                color: #0f172a !important;
                border: 1px solid #cbd5e1 !important;
                font-weight: 600 !important;
            }}
            
            div[data-testid="stPopover"] > button p,
            div[data-testid="stPopover"] > button span,
            div[data-testid="stPopover"] > button svg {{
                color: #0f172a !important;
                fill: #0f172a !important;
            }}

            /* 4. Style Khusus Tombol Biasa (Masuk) */
            .stButton > button {{
                background-color: #ffffff !important;
                color: #0f172a !important;
                border: 1px solid #cbd5e1 !important;
                font-weight: 600 !important;
            }}
            
            .stButton > button p,
            .stButton > button span {{
                color: #0f172a !important;
            }}

            /* 5. Style Tombol Primary (Daftar) */
            .stButton > button[kind="primary"] {{
                background-color: #ff4b4b !important;
                border: none !important;
            }}
            
            .stButton > button[kind="primary"] p,
            .stButton > button[kind="primary"] span {{
                color: #ffffff !important;
            }}

            /* Hover Effect untuk Tombol */
            .stButton > button:hover, div[data-testid="stPopover"] > button:hover {{
                border-color: #0f172a !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
            }}

            /* 6. Memastikan Container / Cards (Kotak Fitur) Selalu Putih dan Bergaris Jelas di Semua Mode */
            div[data-testid="stVerticalBlockBorderWrapper"] > div {{
                background-color: rgba(255, 255, 255, 0.95) !important;
                border-radius: 10px !important;
                padding: 14px !important;
                border: 1px solid #e2e8f0 !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
            }}

            /* 7. Menghilangkan Background Header Bawaan Streamlit */
            header[data-testid="stHeader"] {{
                background-color: rgba(0, 0, 0, 0) !important;
            }}

            /* 8. Sembunyikan Sidebar Bawaan */
            [data-testid="stSidebarNav"] {{display: none;}}
            [data-testid="stSidebar"] {{display: none;}}

            /* 9. Padding Atas */
            .block-container {{
                padding-top: 1rem;
            }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"File background '{image_path}' tidak ditemukan di folder utama.")

# Panggil fungsi background global
set_global_background("background.jpg")


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
        padding: 2rem 2rem 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="color: #ffffff !important; margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: 1px;">MASTER BIMBEL</h1>
                <p style="color: #f1f5f9 !important; margin: 5px 0 0 0; font-size: 1rem; font-weight: 500;">Belajar Tepat, Lulus Cepat!!</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Tombol Menu & Auth
col_menu, col_space, col_auth = st.columns([2, 5, 3])

with col_menu:
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

# 5. Jalankan Halaman Aktif
pg.run()
