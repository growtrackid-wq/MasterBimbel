import streamlit as st

# 1. Hero Banner / Judul Utama
st.markdown("""
    <div style="background-color: #f8f9fa; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; border-left: 6px solid #ff4b4b;">
        <h1 style="color: #1e293b; margin-bottom: 0.5rem; font-size: 2.2rem;">Tentang Kami</h1>
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            <b>Master Bimbel</b> adalah platform bimbingan belajar kedokteran terpercaya yang dirancang khusus untuk membantu mahasiswa kedokteran dan calon dokter meraih impian akademisnya. Kami memahami bahwa perjalanan menjadi seorang dokter membutuhkan dedikasi tinggi, pemahaman materi yang mendalam, dan strategi belajar yang tepat.
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. Sub-judul
st.markdown("### 🚀 Mengapa Memilih Kami?")
st.write("Kami memberikan fasilitas dan metode belajar terbaik untuk mendampingi perjalanan studi kedokteranmu.")
st.write("")

# 3. Tampilan Kartu (Cards) 2x2 Grid
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 👨‍⚕️ Pengajar Profesional")
        st.write("Dibimbing langsung oleh mentor dokter teruji dan berpengalaman di bidangnya.")

    st.write("") # Jarak
    
    with st.container(border=True):
        st.markdown("### 💡 Metode Interaktif")
        st.write("Pembahasan soal yang mendalam (*high-yield*) serta pendampingan belajar yang terstruktur.")

with col2:
    with st.container(border=True):
        st.markdown("### 📚 Materi Terintegrasi")
        st.write("Kurikulum khusus untuk persiapan perkuliahan, ujian koas, hingga UKMPPD (CBT & OSCE).")

    st.write("") # Jarak

    with st.container(border=True):
        st.markdown("### 🏆 Fasilitas Terbaik")
        st.write("Akses latihan soal, modul eksklusif, dan diskusi interaktif kapan saja dan di mana saja.")

# 4. Banner Call to Action (CTA) di Bawah
st.write("")
st.divider()

col_cta1, col_cta2 = st.columns([3, 1])
with col_cta1:
    st.subheader("Siap Mencapai Impian Doktermu?")
    st.write("Bergabunglah bersama ribuan mahasiswa kedokteran lainnya di Master Bimbel.")
with col_cta2:
    st.write("")
    st.button("Mulai Belajar Sekarang", type="primary", use_container_width=True)
