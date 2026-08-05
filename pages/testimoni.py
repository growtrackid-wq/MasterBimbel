import streamlit as st

# Judul Halaman Testimoni
st.title("🌟 Testimoni Peserta Masterbimbel")
st.write("Pengalaman nyata para mahasiswa setelah mengikuti program pembelajaran di Masterbimbel:")

st.write("") # Spacing

# Tampilan 2 Kolom Card
col1, col2 = st.columns(2)

# --- TESTIMONI 1: Nur Afiah ---
with col1:
    with st.container(border=True):
        st.subheader("Nur Afiah")
        st.caption("📚 Reteker Kardiologi")
        st.markdown("⭐⭐⭐⭐⭐")
        
        # Badge Pencapaian Nilai
        st.success("🏆 **Nilai A-**")
        
        # Kutipan Testimoni
        st.markdown(
            "> \"Selama ikut bimbel blok kardiologi di Masterbimbel saya bisa dengan mudah "
            "memahami cara cepat membedakan gejala penyakit kardiovaskular dan cara mudah "
            "memahami EKG serta mendapatkan pengajar yang sangat luar biasa dengan metode ajar "
            "yang sangat mudah dipahami.\""
        )

# --- TESTIMONI 2: Irda Afifah Rahmat ---
with col2:
    with st.container(border=True):
        st.subheader("Irda Afifah Rahmat")
        st.caption("📚 Reteker Kardiologi")
        st.markdown("⭐⭐⭐⭐⭐")
        
        # Badge Pencapaian Nilai
        st.success("🏆 **Nilai B+**")
        
        # Kutipan Testimoni
        st.markdown(
            "> \"Gokil sih Masterbimbel! Ibarat kompas buat kami yang lagi belajar, materi "
            "yang awalnya kayak labirin, berkat Masterbimbel jadi jalan lurus yang gampang banget dicerna. "
            "Cara ngajar tentornya juga oke banget, detailnya tuh kayak lagi bedah anatomi materi, "
            "jadi pahamnya bener-bener mendalam. Nah, latihan soalnya ini nih yang kayak booster semangat, "
            "setiap selesai pertemuan langsung gaspol buat latihan. Sukses terus ya buat Masterbimbel! 💥\""
        )

st.divider()

# Footer Call-to-Action
st.info("💡 **Ingin meraih hasil maksimal seperti mereka?** Bergabunglah bersama kami sekarang juga!")
