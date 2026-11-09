import time
from datetime import datetime
import uuid
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components  # Komponen HTML/JS untuk Timer
import gspread
from google.oauth2.service_account import Credentials

# Set Konfigurasi Halaman Wide
st.set_page_config(page_title="Pusat Pembelajaran - Masterbimbel", layout="wide")

# ==========================================
# 1. INISIALISASI SESSION STATE LOGIN & SESI
# ==========================================
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""
if "session_token" not in st.session_state:
    st.session_state["session_token"] = ""

# ==========================================
# 2. FUNGSI DATABASE & MANAJEMEN SESI (SINGLE SESSION)
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

def simpan_atau_update_sesi(email, token):
    """Menyimpan atau memperbarui token sesi aktif di Google Sheet"""
    try:
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        
        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]
        
        try:
            sheet = gc.open_by_key(spreadsheet_id).worksheet("SesiAktif")
        except Exception:
            # Jika tab SesiAktif belum ada, buat otomatis
            sheet = gc.open_by_key(spreadsheet_id).add_worksheet(title="SesiAktif", rows=100, cols=3)
            sheet.append_row(["Email", "TokenSesi", "WaktuLogin"])

        records = sheet.get_all_records()
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        row_index = None
        for idx, row in enumerate(records, start=2): # Mulai baris 2 (setelah header)
            if str(row.get("Email", "")).strip().lower() == email.strip().lower():
                row_index = idx
                break
        
        if row_index:
            sheet.update_cell(row_index, 2, token)
            sheet.update_cell(row_index, 3, waktu_sekarang)
        else:
            sheet.append_row([email, token, waktu_sekarang])
        return True
    except Exception as e:
        print(f"Error sesi: {e}")
        return False

def validasi_sesi_aktif(email, current_token):
    """Memeriksa apakah token di session state masih sama dengan yang ada di database"""
    if not email or not current_token:
        return False
    try:
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        
        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]
        sheet = gc.open_by_key(spreadsheet_id).worksheet("SesiAktif")
        
        records = sheet.get_all_records()
        for row in records:
            if str(row.get("Email", "")).strip().lower() == email.strip().lower():
                db_token = str(row.get("TokenSesi", "")).strip()
                return db_token == current_token
        return False
    except Exception:
        return True

# ==========================================
# 3. CEK KEAKTIFAN SESI PADA SETIAP RERUN
# ==========================================
if st.session_state["is_logged_in"]:
    if not validasi_sesi_aktif(st.session_state["user_email"], st.session_state["session_token"]):
        st.session_state["is_logged_in"] = False
        st.session_state["user_email"] = ""
        st.session_state["session_token"] = ""
        st.error("⚠️ **Sesi Berakhir!** Akun Anda telah digunakan untuk login di perangkat atau tab browser lain.")
        st.stop()

# ==========================================
# 4. FUNGSI SIMPAN NILAI TRYOUT KE GOOGLE SHEET
# ==========================================
def simpan_nilai_ke_sheet(email, skor, benar, salah, kosong, total_soal):
    try:
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        
        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]
        
        try:
            sheet = gc.open_by_key(spreadsheet_id).worksheet("NilaiTryout")
        except Exception:
            sheet = gc.open_by_key(spreadsheet_id).sheet1

        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        baris_baru = [waktu_sekarang, email, skor, benar, salah, kosong, total_soal]
        
        sheet.append_row(baris_baru)
        return True
    except Exception as e:
        st.error(f"⚠️ Gagal menyimpan nilai ke database: {e}")
        return False

# ==========================================
# 5. POP-UP DIALOG UNTUK FORM LOGIN (MODAL)
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
                    new_token = str(uuid.uuid4())
                    clean_email = email_input.strip().lower()
                    
                    simpan_atau_update_sesi(clean_email, new_token)
                    
                    st.session_state["is_logged_in"] = True
                    st.session_state["user_email"] = clean_email
                    st.session_state["session_token"] = new_token
                    
                    st.success("✅ Email terverifikasi!")
                    st.rerun()
                else:
                    st.error("❌ Email tidak ditemukan. Pastikan Anda sudah mengisi form pendaftaran.")

# ==========================================
# 6. HEADER UTAMA & BANNER STATUS LOGIN
# ==========================================
st.title("📚 Pusat Pembelajaran Masterbimbel")
st.write("Silakan pilih menu materi kuliah atau langsung uji kemampuanmu di menu Tryout.")

if not st.session_state["is_logged_in"]:
    col_warning, col_login_btn = st.columns([3, 1])
    with col_warning:
        st.warning("🔒 **Akses Terkunci!** Klik tombol di samping untuk verifikasi email Anda.")
    with col_login_btn:
        if st.button("🔑 Masuk / Verifikasi", type="primary", use_container_width=True):
            form_login()
else:
    col_status, col_logout_btn = st.columns([3, 1])
    with col_status:
        st.success(f"👤 **Akses Aktif:** {st.session_state['user_email']}")
    with col_logout_btn:
        if st.button("Keluar (Logout)", type="secondary", use_container_width=True):
            st.session_state["is_logged_in"] = False
            st.session_state["user_email"] = ""
            st.session_state["session_token"] = ""
            st.rerun()

st.divider()

# ==========================================
# 7. INISIALISASI TAB UTAMA
# ==========================================
tab_slide, tab_tryout = st.tabs(["📁 Kumpulan Slide Materi", "📝 Sistem Tryout CBT"])

# ------------------------------------------
# TAB 1: KUMPULAN SLIDE MATERI
# ------------------------------------------
with tab_slide:
    st.subheader("Slide & Modul Pembelajaran Berdasarkan Sistem")
    st.write("Klik tombol **'📂 Buka Folder'** untuk mengakses materi di Google Drive:")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 🩺 SLIDE MATERI")
            st.caption("Semua Slide Materi yang telah dibahas.")
            url_slide = "https://drive.google.com/drive/folders/1PlPLzWMb4LHTJtM36ZvUn_I8dr2Aty8Z?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Folder Slide", url_slide, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder (Perlu Login)", disabled=True, use_container_width=True, key="btn_slide_locked")

    with col2:
        with st.container(border=True):
            st.markdown("### 📝 Video")
            st.caption("Video Penjelasan Tutor")
            url_coretan = "https://drive.google.com/drive/folders/1wxjrjykHwZ-ZhF6SHj5MiRpQ5MAjFJKi?usp=sharing"
            
            if st.session_state["is_logged_in"]:
                st.link_button("📂 Buka Video Penjelasan", url_coretan, use_container_width=True, type="primary")
            else:
                st.button("🔒 Buka Folder (Perlu Login)", disabled=True, use_container_width=True, key="btn_coretan_locked")

# ------------------------------------------
# TAB 2: SISTEM TRYOUT CBT (LIVE TICKING TIMER)
# ------------------------------------------
with tab_tryout:
    st.subheader("Simulasi Ujian Computer Based Test (CBT)")
    
    if not st.session_state["is_logged_in"]:
        st.info("🔒 Fitur Tryout CBT ini dikunci. Silakan klik **Masuk / Verifikasi** di bagian atas untuk membuka ujian.")
    else:
        st.write("Centang kotak di bawah ini untuk memulai pengerjaan soal interaktif.")
        mulai_ujian = st.checkbox("Mulai Simulasi Tryout Sekarang")
        
        if mulai_ujian:
            st.divider()

            # --- DIBUATKAN BANK SOAL ---
            if 'data_soal' not in st.session_state:
                try:
                    df_soal = pd.read_excel("bank_soal.xlsx")
                    st.session_state.data_soal = df_soal
                except Exception as e:
                    st.error(f"⚠️ Terjadi kesalahan saat membaca `bank_soal.xlsx`: {e}")
                    st.stop()

            # --- INISIALISASI SESSION STATE UJIAN ---
            if 'soal_sekarang' not in st.session_state:
                st.session_state.soal_sekarang = 0
            if 'jawaban_user' not in st.session_state:
                st.session_state.jawaban_user = {}
            if 'ujian_selesai' not in st.session_state:
                st.session_state.ujian_selesai = False

            # ==========================================
            # LOGIKA TIMER (TARGET WAKTU SELESAI)
            # ==========================================
            DURASI_MENIT = 150  # Durasi ujian dalam menit

            if 'waktu_selesai' not in st.session_state:
                st.session_state.waktu_selesai = time.time() + (DURASI_MENIT * 60)

            sisa_detik = max(0, int(st.session_state.waktu_selesai - time.time()))

            if sisa_detik <= 0 and not st.session_state.ujian_selesai:
                st.session_state.ujian_selesai = True
                st.warning("⏰ **Waktu Ujian telah habis!** Jawaban Anda otomatis dikumpulkan.")

            df = st.session_state.data_soal
            total_soal = len(df)
            idx = st.session_state.soal_sekarang

            # --- TAMPILAN JIKA UJIAN MASIH BERLANGSUNG ---
            if not st.session_state.ujian_selesai:
                col_timer, col_prog = st.columns([1.2, 2.8])
                
                with col_timer:
                    # Kode HTML & JS untuk Timer Berjalan Real-time
                    timer_code = f"""
                    <div style="
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        font-weight: bold;
                        color: #d9534f;
                        background-color: #fdf2f2;
                        border: 1.5px solid #d9534f;
                        padding: 8px 12px;
                        border-radius: 8px;
                        text-align: center;
                    ">
                        ⏳ Sisa Waktu: <span id="countdown">{divmod(sisa_detik, 60)[0]:02d}:{divmod(sisa_detik, 60)[1]:02d}</span>
                    </div>

                    <script>
                        var timeleft = {sisa_detik};
                        var downloadTimer = setInterval(function(){{
                            if(timeleft <= 0){{
                                clearInterval(downloadTimer);
                                document.getElementById("countdown").innerHTML = "00:00";
                                window.parent.postMessage({{type: 'streamlit:rerun'}}, '*');
                            }} else {{
                                var minutes = Math.floor(timeleft / 60);
                                var seconds = timeleft % 60;
                                minutes = minutes < 10 ? "0" + minutes : minutes;
                                seconds = seconds < 10 ? "0" + seconds : seconds;
                                document.getElementById("countdown").innerHTML = minutes + ":" + seconds;
                            }}
                            timeleft -= 1;
                        }}, 1000);
                    </script>
                    """
                    components.html(timer_code, height=60)

                with col_prog:
                    progress = (idx + 1) / total_soal
                    st.progress(progress, text=f"Soal No. {idx + 1} dari {total_soal}")

                st.markdown(f"### **Soal No. {df.loc[idx, 'No']}**")
                st.markdown(f"**{df.loc[idx, 'Soal']}**")

                # ==========================================
                # PENGECEKAN & MENAMPILKAN GAMBAR SOAL
                # ==========================================
                kolom_gambar = 'gambar' if 'gambar' in df.columns else ('Gambar' if 'Gambar' in df.columns else None)
                if kolom_gambar and pd.notna(df.loc[idx, kolom_gambar]) and str(df.loc[idx, kolom_gambar]).strip() != "":
                    nama_file_gambar = str(df.loc[idx, kolom_gambar]).strip()
                    
                    if not nama_file_gambar.startswith("http"):
                        url_gambar = f"https://raw.githubusercontent.com/growtrackid-wq/MasterBimbel/main/Images/{nama_file_gambar}"
                    else:
                        url_gambar = nama_file_gambar
                        
                    st.image(url_gambar, width=350, caption=f"Gambar Soal No. {df.loc[idx, 'No']}")

                # Menyiapkan Opsi Jawaban (Mendukung A, B, C, D, E)
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

            # --- TAMPILAN JIKA UJIAN SELESAI ---
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

                # --- PENYIMPANAN OTOMATIS KE SHEET ---
                if "nilai_tersimpan" not in st.session_state:
                    st.session_state["nilai_tersimpan"] = False

                if not st.session_state["nilai_tersimpan"]:
                    with st.spinner("Menyimpan hasil ujian Anda ke database..."):
                        if simpan_nilai_ke_sheet(
                            st.session_state["user_email"],
                            skor_persen,
                            benar,
                            salah,
                            tidak_dijawab,
                            total_soal
                        ):
                            st.session_state["nilai_tersimpan"] = True
                            st.toast("✅ Nilai berhasil tersimpan di Google Sheet!", icon="🎉")

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
                        
                        # Tampilkan gambar juga pada mode review jika ada
                        kolom_gambar_rev = 'gambar' if 'gambar' in df.columns else ('Gambar' if 'Gambar' in df.columns else None)
                        if kolom_gambar_rev and pd.notna(df.loc[i, kolom_gambar_rev]) and str(df.loc[i, kolom_gambar_rev]).strip() != "":
                            nama_file_gambar = str(df.loc[i, kolom_gambar_rev]).strip()
                            if not nama_file_gambar.startswith("http"):
                                url_gambar = f"https://raw.githubusercontent.com/growtrackid-wq/MasterBimbel/main/Images/{nama_file_gambar}"
                            else:
                                url_gambar = nama_file_gambar
                            st.image(url_gambar, width=300)

                        st.write(f"- **Jawaban Kamu:** `{jawaban_user}`")
                        st.write(f"- **Jawaban Benar:** `{jawaban_benar}`")

                        kolom_pembahasan = 'pembahasan' if 'pembahasan' in df.columns else ('Pembahasan' if 'Pembahasan' in df.columns else None)
                        if kolom_pembahasan and pd.notna(df.loc[i, kolom_pembahasan]):
                            st.info(f"**Pembahasan:**\n\n{df.loc[i, kolom_pembahasan]}")

                st.divider()
                
                # --- TOMBOL RESET UJIAN & TIMER ---
                if st.button("🔄 Ulang Simulasi Ujian", type="primary"):
                    st.session_state.soal_sekarang = 0
                    st.session_state.jawaban_user = {}
                    st.session_state.ujian_selesai = False
                    st.session_state["nilai_tersimpan"] = False
                    
                    if 'waktu_selesai' in st.session_state:
                        del st.session_state['waktu_selesai']
                        
                    st.rerun()
