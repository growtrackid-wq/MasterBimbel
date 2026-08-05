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
            /* 1. Background Utama */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{b64_img}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            /* 2. Warna Teks Utama */
            .stApp p, .stApp label, .stApp li {{
                color: #0f172a !important;
            }}
            
            .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
                color: #0f172a !important;
                font-weight: 700 !important;
            }}

            /* 3. PAKSA TOMBOL POPOVER (MENU) AGAR PUTIH DI DARK MODE */
            div[data-testid="stPopover"] button,
            div[data-testid="stPopover"] [data-baseweb="button"] {{
                background-color: #ffffff !important;
                background: #ffffff !important;
                color: #0f172a !important;
                border: 1px solid #cbd5e1 !important;
            }}

            /* Paksa Teks dan Icon Panah di Dalam Tombol Menu */
            div[data-testid="stPopover"] button *,
            div[data-testid="stPopover"] [data-baseweb="button"] * {{
                color: #0f172a !important;
                fill: #0f172a !important;
            }}

            /* 4. PAKSA TOMBOL MASUK AGAR PUTIH */
            .stButton > button:not([kind="primary"]) {{
                background-color: #ffffff !important;
                background: #ffffff !important;
                color: #0f172a !important;
                border: 1px solid #cbd5e1 !important;
            }}
            .stButton > button:not([kind="primary"]) * {{
                color: #0f172a !important;
            }}

            /* 5. PAKSA TOMBOL DAFTAR (PRIMARY) */
            .stButton > button[kind="primary"] {{
                background-color: #ff4b4b !important;
                background: #ff4b4b !important;
                border: none !important;
            }}
            .stButton > button[kind="primary"] * {{
                color: #ffffff !important;
            }}

            /* 6. PERBAIKAN KOTAK CARD / FITUR (Agar muncul di Dark Mode) */
            div[data-testid="stVerticalBlockBorderWrapper"] {{
                background-color: rgba(255, 255, 255, 0.9) !important;
                border: 1px solid #cbd5e1 !important;
                border-radius: 10px !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
            }}

            /* Header transparan */
            header[data-testid="stHeader"] {{
                background-color: rgba(0, 0, 0, 0) !important;
            }}

            /* Sembunyikan Sidebar Bawaan */
            [data-testid="stSidebarNav"], [data-testid="stSidebar"] {{
                display: none;
            }}

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

# 5. Contoh Struktur Fitur dengan Border Container (Agar Kotak Muncul Konsisten)
st.markdown("### 🚀 Mengapa Memilih Kami?")
st.write("Kami memberikan fasilitas dan metode belajar terbaik untuk mendampingi perjalanan studi kedokteranmu.")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("#### 🧑‍⚕️ Pengajar Profesional")
        st.write("Dibimbing langsung oleh mentor dokter teruji dan berpengalaman di bidangnya.")

with col2:
    with st.container(border=True):
        st.markdown("#### 📚 Materi Terintegrasi")
        st.write("Kurikulum khusus untuk persiapan perkuliahan, ujian koas, hingga UKMPPD (CBT & OSCE).")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("#### 💡 Metode Interaktif")
        st.write("Pembahasan soal yang mendalam (high-yield) serta pendampingan belajar yang terstruktur.")

with col4:
    with st.container(border=True):
        st.markdown("#### 🏆 Fasilitas Terbaik")
        st.write("Akses latihan soal, modul eksklusif, dan diskusi interaktif kapan saja dan di mana saja.")

# 6. Jalankan Halaman Utama/Subhalaman
pg.run()
