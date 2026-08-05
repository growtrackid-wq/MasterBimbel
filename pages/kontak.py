import streamlit as st

# Header Halaman
st.title("📞 Kontak yang Bisa Dihubungi")
st.write("Silakan hubungi kami melalui kanal komunikasi resmi Masterbimbel di bawah ini:")

st.write("") # Spacing

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
            type="primary"
        )

# 2. WHATSAPP
with col2:
    with st.container(border=True):
        st.markdown("### 💬 WhatsApp")
        st.markdown("**0821 9031 2466**")
        st.caption("Konsultasi pendaftaran & informasi program bimbel.")
        # Link WhatsApp otomatis menggunakan format wa.me
        st.link_button(
            label="Kirim Pesan WhatsApp", 
            url="https://wa.me/6282190312466?text=Halo%20Masterbimbel,%20saya%20ingin%20bertanya%20mengenai...", 
            use_container_width=True, 
            type="primary"
        )

# 3. EMAIL
with col3:
    with st.container(border=True):
        st.markdown("### ✉️ Email")
        st.markdown("**masterbimbel5@gmail.com**")
        st.caption("Pertanyaan resmi, kerja sama, atau bantuan akun.")
        # Link mailto untuk membuka aplikasi email pengguna
        st.link_button(
            label="Kirim Email", 
            url="mailto:masterbimbel5@gmail.com", 
            use_container_width=True, 
            type="primary"
        )

st.divider()

# Formulir Kontak Tambahan (Opsional)
with st.expander("📬 Kirim Pesan Langsung dari Website"):
    st.write("Atau isi formulir di bawah ini untuk mengirim pesan langsung kepada kami:")
    
    with st.form("form_kontak", clear_on_submit=True):
        nama = st.text_input("Nama Lengkap")
        email_user = st.text_input("Alamat Email / Nomor WA")
        pesan = st.text_area("Pesan / Pertanyaan")
        
        submitted = st.form_submit_button("Kirim Pesan 🚀")
        if submitted:
            if nama and email_user and pesan:
                st.success("Terima kasih! Pesan kamu berhasil terkirim. Tim kami akan segera menghubungi kamu.")
            else:
                st.warning("Mohon lengkapi semua bidang form sebelum mengirim.")
