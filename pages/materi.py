import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Set Konfigurasi Halaman Wide
st.set_page_config(page_title="Pusat Pembelajaran - Masterbimbel", layout="wide")

# ==========================================
# 1. INISIALISASI SESSION STATE LOGIN
# ==========================================
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""

# ==========================================
# 2. FUNGSI CEK EMAIL TERDAFTAR DI GOOGLE SHEET
# ==========================================
def cek_email_terdaftar(email_input):
    try:
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        
        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]
        sheet = gc.open_by_key(spreadsheet_id).sheet1
        
        # Ambil seluruh email dari Kolom C (Kolom ke-3)
        list_email = sheet.col_values(3)
        list_email_clean = [e.strip().lower() for e in list_email if e]
        
        return email_input.strip().lower() in list_email_clean
    except Exception as e:
        st.error(f"Gagal menghubungkan ke database: {e}")
        return False

# ==========================================
# 3. POP-UP DIALOG UNTUK MASUK (LOGIN)
# ==========================================
@st.dialog("🔑 Masuk Member Masterbimbel")
def form_login():
    st.write("Masukkan email yang Anda gunakan saat mengisi **Formulir Pendaftaran**:")
    email_input = st.text_input("Alamat Email Terdaftar", placeholder="contoh: nama@gmail.com")
    
    if st.button("Verifikasi & Masuk", type="primary", use_container_width=True):
        if not email_input:
            st.warning("⚠️ Mohon isi email Anda terlebih dahulu.")
        else:
            with st.spinner("Memeriksa data pendaftaran Anda..."):
                if cek_email_terdaftar(email_input):
                    st.session_state["is_logged_in"] = True
                    st.session_state["user_email"] = email_input.strip().lower()
                    st.success("✅ Email terverifikasi! Akses materi dan tryout berhasil dibuka.")
                    st.rerun()
                else:
                    st.error("❌ Email tidak ditemukan. Silakan tekan tombol 'Daftar' terlebih dahulu untuk melakukan pendaftaran.")

# ==========================================
# 4. HEADER UTAMA & STATUS LOGIN
# ==========================================
st.title("📚 Pusat Pembelajaran Masterbimbel")
st.write("Silakan pilih menu materi kuliah atau langsung uji kemampuanmu di menu Tryout.")

# Jika sudah login, tampilkan info akun & tombol logout
if st.session_state["is_logged_in"]:
    col_user, col_logout = st.columns([3, 1])
    with col_user:
        st.success(f"👤 **Login sebagai:** {st.session_state['user_email']}")
    with col_logout:
        if st.button("Keluar (Logout)", type="secondary", use_container_width=True):
            st.session_state["is_logged_in"] = False
            st.session_state["user_email"] = ""
            st.rerun()

st.divider()

# ==========================================
# 5. PERINGATAN BILA BELUM LOGIN
# ==========================================
if not st.session_state["is_logged_in"]:
    st.warning("🔒 **Akses Terkunci!** Silakan klik tombol **Masuk** di sudut kanan atas dan verifikasi email Anda untuk mengakses tautan Google Drive dan Tryout CBT.")

# Membuat Tab Utama: Kumpulan Slide vs Tryout CBT
tab_slide, tab_tryout = st.tabs(["📁 Kumpulan Slide Materi", "📝 Sistem Tryout CBT"])

# ==========================================
# TAB 1: KUMPULAN SLIDE MATERI (GOOGLE DRIVE)
# ==========================================
with tab_slide:
    st.subheader("Slide & Modul Pembelajaran Berdasarkan Sistem")
    st.write("Klik tombol **'📂 Buka Folder'** untuk mengakses materi di Google Drive:")

    # Baris 1
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 🩺 Endokrin & Metabolisme")
            st.caption("Diabetes Melitus, Tiroid, Adrenal, dan Gangguan Metabolik.")
            url_endokrin = "https://drive.google.com/drive/folders/1PlPLzWMb4LHTJtM36ZvUn_I8dr2Aty8Z?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Endokrin", url_endokrin, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Endokrin (Perlu Login)", disabled=True, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 🥑 Gastroenterohepatologi")
            st.caption("Sistem Pencernaan, Hati, Saluran Empedu, dan Gastrointestinal.")
            url_gastro = "https://drive.google.com/drive/folders/1wxjrjykHwZ-ZhF6SHj5MiRpQ5MAjFJKi?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Gastro", url_gastro, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Gastro (Perlu Login)", disabled=True, use_container_width=True)

    # Baris 2
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.markdown("### ❤️ Kardiologi & Vaskular")
            st.caption("Kardiovaskular, EKG, Penyakit Jantung Koroner, dan Hipertensi.")
            url_kardio = "https://drive.google.com/drive/folders/1doZFx_pEHBf6vZvqgpU7JcHmzLvW03T1?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Kardiologi", url_kardio, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Kardiologi (Perlu Login)", disabled=True, use_container_width=True)

    with col4:
        with st.container(border=True):
            st.markdown("### 🦟 Kedokteran Tropis (KedTrop)")
            st.caption("Infeksi Tropis, DHF, Malaria, Demam Tifoid, dan Parasitologi.")
            url_kedtrop = "https://drive.google.com/drive/folders/1IVspdEFwRoRCPx1_BYAZnN0woRDAM3WD?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder KedTrop", url_kedtrop, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder KedTrop (Perlu Login)", disabled=True, use_container_width=True)

    # Baris 3
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            st.markdown("### 🧠 Neuropsikiatri")
            st.caption("Neurologi (Saraf), Stroke, Kejang, serta Gangguan Psikiatri.")
            url_neuro = "https://drive.google.com/drive/folders/1yRrmN1AgK-9bHg8DPAsAqEyvzN5hDCV2?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Neuropsikiatri", url_neuro, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Neuropsikiatri (Perlu Login)", disabled=True, use_container_width=True)

    with col6:
        with st.container(border=True):
            st.markdown("### 🫁 Pulmonologi & Respirasi")
            st.caption("Sistem Respirasi, Asma, PPOK, Tuberculosis (TB), dan Pneumonia.")
            url_respi = "https://drive.google.com/drive/folders/1s42ZzH7ay4rKu_YaNlj6-Ox8HjT66D3e?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Respirasi", url_respi, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Respirasi (Perlu Login)", disabled=True, use_container_width=True)

    # Baris 4
    col7, col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            st.markdown("### 👁️ Special Sense (Indera)")
            st.caption("Indera Mata, Telinga Hidung Tenggorokan (THT), dan Dermatologi.")
            url_sense = "https://drive.google.com/drive/folders/1MFWypf6XLL1Wz1-dqUG8058xG7_h8fk9?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Special Sense", url_sense, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Special Sense (Perlu Login)", disabled=True, use_container_width=True)

    with col8:
        with st.container(border=True):
            st.markdown("### 🚽 Urologi & Ginjal")
            st.caption("Saluran Kemih, Infeksi Saluran Kemih (ISK), BPH, dan Ginjal.")
            url_uro = "https://drive.google.com/drive/folders/1sxsFjKpncecy4HcsjtmVDQGFYqZoWy8N?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Urologi", url_uro, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder Urologi (Perlu Login)", disabled=True, use_container_width=True)


# ==========================================
# TAB 2: SISTEM TRYOUT CBT (PROTECTED)
# ==========================================
with tab_tryout:
    st.subheader("Simulasi Ujian Computer Based Test (CBT)")
    
    if not st.session_state["is_logged_in"]:
        st.info("🔒 Fitur Tryout CBT ini dikunci. Silakan klik **Masuk** di pojok kanan atas untuk membuka ujian.")
    else:
        st.write("Centang kotak di bawah ini untuk memulai pengerjaan soal interaktif.")
        mulai_ujian = st.checkbox("Mulai Simulasi Tryout Sekarang")
        
        if mulai_ujian:
            st.divider()

            # Load bank soal dari excel
            if 'data_soal' not in st.session_state:
                try:
                    df_soal = pd.read_excel("bank_soal.xlsx")
                    st.session_state.data_soal = df_soal
                except Exception as e:
                    st.error(f"⚠️ Terjadi kesalahan saat membaca `bank_soal.xlsx`: {e}")
                    st.stop()

            # Inisialisasi State Ujian
            if 'soal_sekarang' not in st.session_state:
                st.session_state.soal_sekarang = 0
            if 'jawaban_user' not in st.session_state:
                st.session_state.jawaban_user = {}
            if 'ujian_selesai' not in st.session_state:
                st.session_state.ujian_selesai = False

            df = st.session_state.data_soal
            total_soal = len(df)
            idx = st.session_state.soal_sekarang

            # ------------------------------------------
            # A. HALAMAN PENGERJAAN SOAL
            # ------------------------------------------
            if not st.session_state.ujian_selesai:
                progress = (idx + 1) / total_soal
                st.progress(progress, text=f"Soal No. {idx + 1} dari {total_soal}")

                st.markdown(f"### **Soal No. {df.loc[idx, 'No']}**")
                st.markdown(f"**{df.loc[idx, 'Soal']}**")

                opsi = [
                    f"A. {df.loc[idx, 'A']}", 
                    f"B. {df.loc[idx, 'B']}", 
                    f"C. {df.loc[idx, 'C']}", 
                    f"D. {df.loc[idx, 'D']}"
                ]
                if 'E' in df.columns and pd.notna(df.loc[idx, 'E']):
                    opsi.append(f"E. {df.loc[idx, 'E']}")

                jawaban_sebelumnya = st.session_state.jawaban_user.get(idx, None)
                index_default = None
                if jawaban_sebelumnya:
                    for i, o in enumerate(opsi):
                        if o.startswith(jawaban_sebelumnya):
                            index_default = i
                            break

                pilihan = st.radio(
                    "Pilih jawaban:", 
                    opsi, 
                    index=index_default, 
                    key=f"radio_soal_{idx}"
                )

                if pilihan:
                    st.session_state.jawaban_user[idx] = pilihan.split(".")[0]

                st.write("") 

                col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 2])

                with col_nav1:
                    if st.button("⬅️ Sebelumnya", disabled=(idx == 0), use_container_width=True):
                        st.session_state.soal_sekarang -= 1
                        st.rerun()

                with col_nav2:
                    if idx < total_soal - 1:
                        if st.button("Selanjutnya ➡️", type="primary", use_container_width=True):
                            st.session_state.soal_sekarang += 1
                            st.rerun()

                with col_nav3:
                    if idx == total_soal - 1:
                        if st.button("🏁 Selesai & Kumpulkan Ujian", type="primary", use_container_width=True):
                            st.session_state.ujian_selesai = True
                            st.rerun()

            # ------------------------------------------
            # B. HALAMAN HASIL & REKAPITULASI SOAL
            # ------------------------------------------
            else:
                st.balloons()
                st.subheader("📊 Hasil Simulasi Tryout CBT")

                benar = 0
                salah = 0
                tidak_dijawab = 0

                for i in range(total_soal):
                    jawaban_user = st.session_state.jawaban_user.get(i, None)
                    jawaban_benar = str(df.loc[i, 'Jawaban']).strip().upper()

                    if jawaban_user is None:
                        tidak_dijawab += 1
                    elif jawaban_user == jawaban_benar:
                        benar += 1
                    else:
                        salah += 1

                skor_persen = round((benar / total_soal) * 100, 1)

                col_res1, col_res2, col_res3, col_res4 = st.columns(4)
                col_res1.metric("Skor Akhir", f"{skor_persen}%")
                col_res2.metric("Jawaban Benar ✅", f"{benar} Soal")
                col_res3.metric("Jawaban Salah ❌", f"{salah} Soal")
                col_res4.metric("Kosong ⚪", f"{tidak_dijawab} Soal")

                st.divider()
                st.subheader("🔍 Review & Pembahasan Soal")

                for i in range(total_soal):
                    jawaban_user = st.session_state.jawaban_user.get(i, "Tidak Dijawab")
                    jawaban_benar = str(df.loc[i, 'Jawaban']).strip().upper()

                    is_correct = (jawaban_user == jawaban_benar)
                    status_icon = "✅" if is_correct else "❌"

                    with st.expander(f"Soal No. {df.loc[i, 'No']} - Status: {status_icon}"):
                        st.markdown(f"**{df.loc[i, 'Soal']}**")
                        st.write(f"- **Jawaban Kamu:** `{jawaban_user}`")
                        st.write(f"- **Jawaban Benar:** `{jawaban_benar}`")

                        if 'Pembahasan' in df.columns and pd.notna(df.loc[i, 'Pembahasan']):
                            st.info(f"**Pembahasan:**\n\n{df.loc[i, 'Pembahasan']}")

                st.divider()
                
                if st.button("🔄 Ulang Simulasi Ujian", type="primary"):
                    st.session_state.soal_sekarang = 0
                    st.session_state.jawaban_user = {}
                    st.session_state.ujian_selesai = False
                    st.rerun()
