import streamlit as st

# Judul Utama
st.title("🛡️ Kebijakan Privasi")
st.caption("Terakhir diperbarui: 5 Agustus 2026")

st.write(
    "Di **Masterbimbel**, kami sangat menghargai privasi Anda dan berkomitmen untuk "
    "melindungi data pribadi yang Anda bagikan kepada kami. Kebijakan Privasi ini "
    "menjelaskan bagaimana kami mengumpulkan, menggunakan, dan melindungi informasi Anda "
    "saat menggunakan platform bimbel ini."
)

st.divider()

# Poin-Poin Kebijakan Privasi
with st.expander("1. Informasi yang Kami Kumpulkan", expanded=True):
    st.markdown(
        """
        Kami mengumpulkan beberapa jenis informasi untuk memberikan layanan pembelajaran terbaik:
        - **Data Identitas:** Nama lengkap, alamat email, dan nomor telepon/WhatsApp saat Anda mendaftar atau menghubungi layanan pengguna.
        - **Data Pengerjaan Ujian:** Rekam aktivitas pengerjaan soal tryout, skor, waktu penyelesaian, dan riwayat jawaban untuk analisis perkembangan belajar Anda.
        - **Data Teknis:** Informasi perangkat dan riwayat akses log standar untuk menjaga kestabilan sistem platform.
        """
    )

with st.expander("2. Penggunaan Informasi", expanded=False):
    st.markdown(
        """
        Informasi yang kami kumpulkan digunakan khusus untuk kepentingan operasional pembelajaran:
        - Menyediakan akses ke modul materi pembelajaran dan sistem tryout interaktif.
        - Menampilkan hasil evaluasi dan statistik kelulusan tryout secara akurat.
        - Menghubungi Anda terkait konfirmasi pendaftaran, pembaruan materi, atau informasi penting lainnya.
        - Meningkatkan kualitas materi dan kualitas platform secara berkelanjutan.
        """
    )

with st.expander("3. Perlindungan & Kerahasiaan Data", expanded=False):
    st.markdown(
        """
        - **Tidak Menjual Data:** Masterbimbel **tidak akan pernah menjual, menyewakan, atau membagikan** data pribadi Anda kepada pihak ketiga untuk kepentingan komersial.
        - **Keamanan Data:** Kami menerapkan langkah-langkah keamanan teknis untuk melindungi data Anda dari akses tanpa izin, perubahan, atau penghapusan yang tidak sah.
        - **Kerahasiaan Skor:** Rekapitulasi hasil tryout bersifat pribadi dan hanya dapat diakses oleh Anda serta tim akademis Masterbimbel untuk evaluasi.
        """
    )

with st.expander("4. Penggunaan Cookies & Layanan Pihak Ketiga", expanded=False):
    st.markdown(
        """
        - Platform kami menggunakan penyimpanan sesi internal (*session state*) untuk menyimpan progres pengerjaan ujian Anda secara sementara selama sesi berlangsung.
        - Beberapa tautan materi mengarah ke layanan tepercaya pihak ketiga (seperti Google Drive). Kami menyarankan Anda untuk membaca kebijakan privasi dari platform terkait saat membukanya.
        """
    )

with st.expander("5. Hak-Hak Pengguna", expanded=False):
    st.markdown(
        """
        Sebagai pengguna, Anda berhak untuk:
        - Meminta pembaruan atau koreksi terhadap data pribadi yang tidak akurat.
        - Meminta penghapusan akun atau riwayat belajar Anda dari sistem kami.
        - Mengajukan pertanyaan atau kendala terkait pengelolaan data pribadi Anda.
        """
    )

with st.expander("6. Perubahan Kebijakan Privasi", expanded=False):
    st.markdown(
        """
        Masterbimbel berhak untuk memperbarui Kebijakan Privasi ini sewaktu-waktu. Setiap perubahan akan langsung ditayangkan pada halaman ini. Penggunaan layanan secara berkelanjutan menandakan persetujuan Anda terhadap perubahan tersebut.
        """
    )

st.divider()

# Kontak Bantuan
st.info(
    "💬 **Punya pertanyaan seputar Kebijakan Privasi ini?**\n\n"
    "Hubungi tim support kami melalui menu **Kontak** atau email langsung ke **masterbimbel5@gmail.com**."
)
