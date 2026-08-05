import streamlit as st

# Judul Halaman Testimoni
st.title("🌟 Testimoni Peserta Masterbimbel")
st.write("Pengalaman nyata para mahasiswa setelah mengikuti program pembelajaran di Masterbimbel:")

st.write("") # Spacing

# Tampilkan Poster Gambar dalam 2 Kolom Sejajar
col1, col2 = st.columns(2)

with col1:
    # Mengisi gambar poster Nur Afiah
    st.image(
        "testimoni1.jpg", 
        caption="Testimoni Nur Afiah - Reteker Kardiologi (Nilai A-)", 
        use_container_width=True
    )

with col2:
    # Mengisi gambar poster Irda Afifah
    st.image(
        "testimoni2.jpg", 
        caption="Testimoni Irda Afifah Rahmat - Reteker Kardiologi (Nilai B+)", 
        use_container_width=True
    )

st.divider()

# Footer Call-to-Action
st.info("💡 **Ingin meraih hasil maksimal seperti mereka?** Bergabunglah bersama kami sekarang juga!")
