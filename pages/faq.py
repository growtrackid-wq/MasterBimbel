import streamlit as st

# Judul Utama
st.title("❓ Pertanyaan yang Sering Diajukan (FAQ)")
st.write(
    "Punya pertanyaan seputar program bimbel, cara pendaftaran, atau sistem ujian di **Masterbimbel**? "
    "Temukan jawabannya di bawah ini!"
)

st.divider()

# Kategori 1: Pendaftaran & Program
st.subheader("📌 Pendaftaran & Program Bimbel")

with st.expander("Bagaimana cara mendaftar di Masterbimbel?"):
    st.write(
        "Anda dapat melakukan pendaftaran dengan menghubungi admin kami melalui menu **Kontak** "
        "(WhatsApp/Email) atau mengklik tombol WhatsApp resmi yang tersedia di platform ini. "
        "Admin akan membantu proses pendaftaran dan verifikasi akun Anda."
    )

with st.expander("Program pembelajaran apa saja yang tersedia?"):
    st.write(
        "Masterbimbel menyediakan program bimbingan belajar fokus kedokteran dan kesehatan, "
        "seperti Bimbingan Reteker, Blok Akademik, Persiapan UKMPPD, dan tryout latihan soal interaktif."
    )

with st.expander("Apakah ada jadwal bimbingan tatap muka / offline?"):
    st.write(
        "Saat ini seluruh modul, materi, dan tryout di platform ini diselenggarakan secara online "
        "sehingga Anda dapat belajar kapan saja dan di mana saja secara fleksibel."
    )

st.write("") # Spacing

# Kategori 2: Pembelajaran & Modul
st.subheader("📚 Pembelajaran & Akses Materi")

with st.expander("Bagaimana cara mengakses materi bimbingan?"):
    st.write(
        "Setelah terdaftar, Anda dapat membuka menu **Materi** pada navigasi utama. "
        "Materi dapat diunduh atau dipelajari langsung melalui tautan dokumen/video yang disediakan."
    )

with st.expander("Apakah materi pembelajaran bisa diakses selamanya?"):
    st.write(
        "Ya, materi yang sudah diberikan dapat Anda akses dan pelajari kembali selama masa periode program bimbingan Anda aktif."
    )

st.write("") # Spacing

# Kategori 3: Ujian & Tryout
st.subheader("📝 Sistem Ujian & Tryout")

with st.expander("Bagaimana sistem pengerjaan tryout di Masterbimbel?"):
    st.write(
        "Tryout dilakukan secara interaktif berbasis web. Anda dapat memilih bab/blok materi, "
        "menjawab soal pilihan ganda, dan langsung melihat skor serta pembahasan setelah selesai."
    )

with st.expander("Bagaimana jika terjadi kendala teknis saat mengerjakan tryout?"):
    st.write(
        "Sistem kami menyimpan progres jawaban Anda. Jika koneksi terputus, Anda dapat me-refresh halaman "
        "atau segera menghubungi tim CS melalui menu **Kontak** untuk bantuan teknis."
    )

st.divider()

# Kotak Bantuan Jika Pertanyaan Belum Terjawab
st.info(
    "💬 **Pertanyaan Anda belum terjawab di atas?**\n\n"
    "Jangan ragu untuk bertanya langsung kepada tim CS kami melalui halaman **Kontak**!"
)
