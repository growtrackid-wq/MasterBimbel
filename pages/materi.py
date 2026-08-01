import streamlit as st
import pandas as pd

st.title("📚 Pusat Pembelajaran Masterbimbel")
st.write("Silakan pilih menu materi kuliah atau langsung uji kemampuanmu di menu Tryout.")

# Membuat Tab Internal: Kumpulan Slide vs Tryout Ujian
tab_slide, tab_tryout = st.tabs(["📁 Kumpulan Slide Materi", "📝 Sistem Tryout CBT"])

with tab_slide:
    st.subheader("Kumpulan Slide Kuliah & Modul PDF")
    st.write("Berikut adalah materi referensi siap download:")
    
    # Contoh list slide materi bimbel
    st.info("📂 [Download] Modul Kardiologi - Pendekatan IMA Akut.pdf")
    st.info("📂 [Download] Modul Pediatri - Manifestasi Klinis Infeksi Dengue.pdf")

with tab_tryout:
    st.subheader("Simulasi Ujian Computer Based Test (CBT)")
    st.write("Klik tombol di bawah ini untuk memulai pengerjaan soal interaktif.")
    
    # Tombol pemicu mulai ujian
    mulai_ujian = st.checkbox("Mulai Simulasi Tryout Sekarang")
    
    if mulai_ujian:
        st.divider()
        # Masukkan logika kodingan bank soal yang sudah berhasil kamu buat sebelumnya di sini
        if 'data_soal' not in st.session_state:
            raw_data = {
                'No': [1, 2],
                'Soal': [
                    "Seorang pasien laki-laki berusia 45 tahun datang dengan keluhan nyeri dada kiri yang menjalar ke lengan kiri sejak 2 jam lalu. Diagnosis yang paling tepat adalah...",
                    "Seorang anak berusia 5 tahun dibawa ibunya dengan keluhan demam tinggi selama 4 hari disertai bintik merah di kulit. Uji Rumple Leede (+). Diagnosa awal yang tepat..."
                ],
                'A': ["Gastroesophageal Reflux Disease (GERD)", "Demam Berdarah Dengue (DBD)"],
                'B': ["Acute Coronary Syndrome (ACS)", "Campak / Morbili"],
                'C': ["Perikarditis Akut", "Demam Tifoid"],
                'D': ["Pneumotoraks", "Malaria"],
                'Jawaban': ["B", "A"],
                'Pembahasan': [
                    "Nyeri dada kiri yang menjalar ke lengan kiri merupakan gejala khas dari IMA/ACS akibat iskemia miokard.",
                    "Demam tinggi mendadak disertai manifestasi perdarahan (Rumple Leede positif) pada anak mengarah kuat pada Dengue Hemorrhagic Fever."
                ]
            }
            st.session_state.data_soal = pd.DataFrame(raw_data)

        if 'soal_sekarang' not in st.session_state:
            st.session_state.soal_sekarang = 0
        if 'sudah_cek' not in st.session_state:
            st.session_state.sudah_cek = False

        idx = st.session_state.soal_sekarang
        df = st.session_state.data_soal
        total_soal = len(df)

        if idx < total_soal:
            st.write(f"**Soal No. {df.loc[idx, 'No']} dari {total_soal}**")
            st.markdown(df.loc[idx, 'Soal'])
            
            opsi = [f"A. {df.loc[idx, 'A']}", f"B. {df.loc[idx, 'B']}", f"C. {df.loc[idx, 'C']}", f"D. {df.loc[idx, 'D']}"]
            pilihan = st.radio("Pilih jawaban:", opsi, index=None, key=f"ans_{idx}")
            
            if st.button("Cek Jawaban", disabled=(pilihan is None)):
                st.session_state.sudah_cek = True
                
            if st.session_state.sudah_cek:
                st.info(f"**Jawaban Benar:** {df.loc[idx, 'Jawaban']}\n\n**Pembahasan:** {df.loc[idx, 'Pembahasan']}")
                if st.button("Selanjutnya ➡️"):
                    st.session_state.soal_sekarang += 1
                    st.session_state.sudah_cek = False
                    st.rerun()
        else:
            st.success("🎉 Selesai! Kamu telah menyelesaikan tryout kali ini.")
            if st.button("Ulang Ujian 🔄"):
                st.session_state.soal_sekarang = 0
                st.rerun()