import streamlit as st

# Judul Halaman
st.title("Tentang Kami")

# Paragraf Deskripsi
st.write(
    "**Master Bimbel** adalah platform bimbingan belajar kedokteran terpercaya yang "
    "dirancang khusus untuk membantu mahasiswa kedokteran dan calon dokter meraih "
    "impian akademisnya. Kami memahami bahwa perjalanan menjadi seorang dokter "
    "membutuhkan dedikasi tinggi, pemahaman materi yang mendalam, dan strategi "
    "belajar yang tepat."
)

st.subheader("Mengapa Memilih Kami?")

# Poin-poin Keunggulan
st.markdown(
    """
* **Pengajar Profesional:** Dibimbing langsung oleh mentor dokter teruji dan berpengalaman.
* **Materi Terintegrasi:** Kurikulum yang dirancang khusus untuk persiapan perkuliahan, ujian koas, hingga UKMPPD (CBT & OSCE).
* **Metode Interaktif:** Pembahasan soal yang mendalam (*high-yield*) serta pendampingan belajar yang terstruktur.
* **Fasilitas Terbaik:** Akses latihan soal, modul eksklusif, dan diskusi interaktif kapan saja.
"""
)
