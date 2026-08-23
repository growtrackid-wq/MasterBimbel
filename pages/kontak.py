from datetime import datetime
from google.oauth2.service_account import Credentials
import gspread
import streamlit as st

# ==========================================
# FUNGSI SIMPAN PESAN KE GOOGLE SHEET
# ==========================================
def simpan_pesan_ke_sheet(nama_user, kontak_user, isi_pesan):
    try:
        # Mengambil kredensial dari st.secrets
        credentials_dict = dict(st.secrets["gcp_service_account"])
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_info(
            credentials_dict, scopes=scopes
        )

        gc = gspread.authorize(creds)
        spreadsheet_id = st.secrets["gsheets"]["spreadsheet_id"]

        # Mengakses tab worksheet "PesanMasuk"
        sheet = gc.open_by_key(spreadsheet_id).worksheet("PesanMasuk")

        # Format waktu pendaftaran
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Menambahkan baris baru ke Google Sheet
        sheet.append_row([waktu_sekarang, nama_user, kontak_user, isi_pesan])
        return True
    except Exception as e:
        st.error(
            f"⚠️ Gagal menyimpan pesan. Pastikan tab 'PesanMasuk' sudah dibuat di Google Sheet. Error: {e}"
        )
        return False


# ==========================================
# TAMPILAN HALAMAN KONTAK
# ==========================================
# Header Halaman
st.title("📞 Kontak yang Bisa Dihubungi")
st.write(
    "Silakan hubungi kami melalui kanal komunikasi resmi Masterbimbel di bawah"
    " ini:"
)

st.write("")  # Spacing

# Membuat Layout dengan Grid/Card Container
col1, col2, col3 = st.columns(3)

# 1. INSTAGRAM
with col1:
    with st.container(border=True):
        st.markdown("### 📸 Instagram")
        st.markdown("**@Masterbimbell**")
        st.caption("Dapatkan update informasi terbaru & materi harian.")
        st.link_button(
            label="Ikuti di Instagram",
            url="https://www.instagram.com/Masterbimbell",
            use_container_width=True,
            type="primary",
        )

# 2. WHATSAPP
with col2:
    with st.container(border=True):
        st.markdown("### 💬 WhatsApp")
        st.markdown("**0821 9031 2466**")
        st.caption("Konsultasi pendaftaran & informasi program bimbel.")
        st.link_button(
            label="Kirim Pesan WhatsApp",
            url=(
                "https://wa.me/6282190312466?text=Halo%20Masterbimbel,%20saya%20ingin%20bertanya%20mengenai..."
            ),
            use_container_width=True,
            type="primary",
        )

# 3. EMAIL
with col3:
    with st.container(border=True):
        st.markdown("### ✉️ Email")
        st.markdown("**masterbimbel5@gmail.com**")
        st.caption("Pertanyaan resmi, kerja sama, atau bantuan akun.")
        st.link_button(
            label="Kirim Email",
            url="mailto:masterbimbel5@gmail.com",
            use_container_width=True,
            type="primary",
        )

st.divider()

# Formulir Kontak Tambahan
with st.expander("📬 Kirim Pesan Langsung dari Website", expanded=True):
    st.write(
        "Atau isi formulir di bawah ini untuk mengirim pesan langsung kepada"
        " kami:"
    )

    with st.form("form_kontak", clear_on_submit=True):
        nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
        email_user = st.text_input(
            "Alamat Email / Nomor WA",
            placeholder="contoh: nama@gmail.com atau 08123456789",
        )
        pesan = st.text_area(
            "Pesan / Pertanyaan", placeholder="Tuliskan pesan Anda di sini..."
        )

        submitted = st.form_submit_button("Kirim Pesan 🚀", type="primary")

        if submitted:
            if nama.strip() and email_user.strip() and pesan.strip():
                with st.spinner("Mengirim pesan ke database..."):
                    if simpan_pesan_ke_sheet(nama, email_user, pesan):
                        st.success(
                            "Terima kasih! Pesan kamu berhasil terkirim. Tim"
                            " kami akan segera menghubungi kamu."
                        )
                        st.balloons()
            else:
                st.warning(
                    "Mohon lengkapi semua bidang form sebelum mengirim."
                )
