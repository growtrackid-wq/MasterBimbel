import base64
import streamlit as st

# 1. Konfigurasi Dasar
st.set_page_config(page_title="Masterbimbel - Dashboard", page_icon="🩺", layout="wide")

# Fungsi untuk membaca background.jpg lokal dan mengubahnya ke CSS Base64
def set_global_background(image_path="background.jpg"):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        b64_img = base64.b64encode(data).decode()
        
        bg_css = f"""
        <style>
            /* Mengubah Background Utama Seluruh Halaman */
            .stApp {{
                background-image: url("data:image/jpeg;base64,{b64_img}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            /* Menghilangkan background header bawaan Streamlit agar menyatu */
            header[data-testid="stHeader"] {{
                background-color: rgba(0, 0, 0, 0);
            }}

            /* Sembunyikan Sidebar Bawaan */
            [data-testid="stSidebarNav"] {{display: none;}}
            [data-testid="stSidebar"] {{display: none;}}

            /* Menghilangkan padding bawaan paling atas */
            .block-container {{
                padding-top: 1rem;
            }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)
    except Exception as e:
        # Jika file gambar gagal dibaca
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

# 3. Custom Banner Header dengan Gambar Background
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
        <div style="display: flex; justify-content: space-between; align-items: center; color: white;">
            <div>
                <h1 style="color: white; margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: 1px;">MASTER BIMBEL</h1>
                <p style="color: #f1f5f9; margin: 5px 0 0 0; font-size: 1rem; font-weight: 500;">Belajar Tepat, Lulus Cepat!!</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Tombol Menu & Auth (Di Bawah Banner / Sejajar Garis Horizontal)
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
