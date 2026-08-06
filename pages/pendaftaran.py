import streamlit as st
import urllib.parse
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

st.markdown("## 📝 Formulir Pendaftaran Bimbingan")
st.write("Lengkapi data diri Anda di bawah ini untuk memulai bimbingan di **Master Bimbel**.")

# ==========================================
# FUNGSI KONEKSI KE GOOGLE SHEETS
# ==========================================
def simpan_ke_google_sheets(nama, email_pendaftar, no_wa, univ, status, program, catatan_user, file_uploaded):
    try:
        # 1. Kredensial dari st.secrets
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
        
        # 2. Hubungkan ke Google Sheets
        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]
        sheet = gc.open_by_key(spreadsheet_id).sheet1
        
        # 3. Keterangan Bukti Pembayaran
        info_bukti = "Lampiran di WA" if file_uploaded is not None else "Tidak Ada"
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_data = [
            timestamp,
            nama,
            email_pendaftar,
            no_wa,
            univ,
            status,
            program,
            catatan_user if catatan_user else "-",
            info_bukti
        ]
        
        sheet.append_row(row_data)
        return True, None

    except Exception as e:
        return False, str(e)

# ==========================================
# TAMPILAN FORMULIR PENDAFTARAN
# ==========================================
with st.container(border=True):
    with st.form("form_pendaftaran_lengkap", clear_on_submit=False):
        st.subheader("1. Data Diri Mahasiswa")
        col_nama, col_email = st.columns(2)
        with col_nama:
            nama_lengkap = st.text_input("Nama Lengkap (dengan Gelar jika ada)*", placeholder="contoh: Ahmad Subagja, S.Ked")
        with col_email:
            email = st.text_input("Alamat Email*", placeholder="contoh: ahmad@gmail.com")
            
        col_hp, col_univ = st.columns(2)
        with col_hp:
            no_wa = st.text_input("Nomor WhatsApp (Aktif)*", placeholder="contoh: 081234567890")
        with col_univ:
            universitas = st.text_input("Asal Universitas / Fakultas Kedokteran*", placeholder="contoh: FK Universitas Indonesia")

        st.divider()
        st.subheader("2. Program & Jenjang Bimbingan")
        
        status_mhs = st.radio(
            "Status Mahasiswa Saat Ini*",
            ["Pre-Klinik (Semester 1-8)", "Kepaniteraan Klinik (Koas)", "Persiapan UKMPPD / Alumni"],
            horizontal=True
        )
        
        program_pilihan = st.selectbox(
            "Pilih Program Utama*",
            [
                "Kelas Reguler Pre-Klinik (Pendampingan Ujian Semester)",
                "Kelas Intensif Stase Klinik (Koas)",
                "Bimbingan UKMPPD CBT (Try Out & Pembahasan High-Yield)",
                "Bimbingan UKMPPD OSCE (Simulasi & Checksheet)",
                "Private 1-on-1 Mentoring"
            ]
        )

        catatan = st.text_area("Catatan Khusus / Target Belajar", placeholder="Tuliskan mata kuliah atau stase yang ingin difokuskan...")

        st.divider()
        st.subheader("3. Dokumen Pendukung (Opsional)")
        ktm_file = st.file_uploader("Unggah Bukti Pembayaran", type=["jpg", "jpeg", "png", "pdf"])

        st.markdown("<br>", unsafe_allow_html=True)
        btn_submit = st.form_submit_button("Kirim Pendaftaran", type="primary", use_container_width=True)

    if btn_submit:
        if not nama_lengkap or not email or not no_wa or not universitas:
            st.error("⚠️ Mohon lengkapi seluruh kolom bertanda bintang (*) sebelum melanjutkan.")
        else:
            with st.spinner("Sedang menyimpan data pendaftaran..."):
                sukses, err = simpan_ke_google_sheets(
                    nama_lengkap, email, no_wa, universitas, status_mhs, program_pilihan, catatan, ktm_file
                )
            
            if sukses:
                st.success("✅ Form Pendaftaran Berhasil Diisi dan Tersimpan!")
                
                # Format Pesan Otomatis ke WhatsApp Admin
                pesan_wa = (
                    f"Halo Admin Master Bimbel, saya telah mengisi formulir pendaftaran via Website!\n\n"
                    f"📌 *DETAIL PENDAFTARAN*\n"
                    f"• *Nama:* {nama_lengkap}\n"
                    f"• *Email:* {email}\n"
                    f"• *No WA:* {no_wa}\n"
                    f"• *Universitas:* {universitas}\n"
                    f"• *Status:* {status_mhs}\n"
                    f"• *Program:* {program_pilihan}\n"
                    f"• *Catatan:* {catatan if catatan else '-'}\n\n"
                    f"*(Saya melampirkan foto bukti pembayaran di chat ini)*"
                )
                
                nomor_admin = "6282157263167" 
                link_whatsapp = f"https://wa.me/{nomor_admin}?text={urllib.parse.quote(pesan_wa)}"

                st.info("Langkah terakhir: Klik tombol di bawah ini untuk mengonfirmasi pendaftaran & kirim foto bukti bayar ke WhatsApp Admin.")
                st.link_button("📲 Konfirmasi & Kirim Data ke WhatsApp Admin", link_whatsapp, use_container_width=True)
            else:
                st.error(f"❌ Gagal menyimpan data ke database. Error: {err}")

# Tombol Kembali ke Dashboard
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⬅️ Kembali ke Halaman Utama"):
    st.switch_page("pages/tentang_kami.py")
