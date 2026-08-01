import streamlit as st
import pandas as pd

# Judul Utama Halaman
st.title("📚 Pusat Pembelajaran Masterbimbel")
st.write("Silakan pilih menu materi kuliah atau langsung uji kemampuanmu di menu Tryout.")

# Membuat Tab Utama: Kumpulan Slide vs Tryout CBT
tab_slide, tab_tryout = st.tabs(["📁 Kumpulan Slide Materi", "📝 Sistem Tryout CBT"])

# ==========================================
# TAB 1: KUMPULAN SLIDE MATERI (GOOGLE DRIVE)
# ==========================================
with tab_slide:
    st.subheader("Slide & Modul Pembelajaran Berdasarkan Sistem")
    st.write("Klik tombol **'📂 Buka Folder'** untuk mengakses materi di Google Drive:")

    # Baris 1
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 🩺 Endokrin & Metabolisme")
            st.caption("Diabetes Melitus, Tiroid, Adrenal, dan Gangguan Metabolik.")
            st.link_button("📂 Buka Folder Endokrin", "https://drive.google.com/drive/folders/1PlPLzWMb4LHTJtM36ZvUn_I8dr2Aty8Z?usp=sharing")

    with col2:
        with st.container(border=True):
            st.markdown("### 🥑 Gastroenterohepatologi")
            st.caption("Sistem Pencernaan, Hati, Saluran Empedu, dan Gastrointestinal.")
            st.link_button("📂 Buka Folder Gastro", "https://drive.google.com/drive/folders/1wxjrjykHwZ-ZhF6SHj5MiRpQ5MAjFJKi?usp=sharing")

    # Baris 2
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.markdown("### ❤️ Kardiologi & Vaskular")
            st.caption("Kardiovaskular, EKG, Penyakit Jantung Koroner, dan Hipertensi.")
            st.link_button("📂 Buka Folder Kardiologi", "https://drive.google.com/drive/folders/1doZFx_pEHBf6vZvqgpU7JcHmzLvW03T1?usp=sharing")

    with col4:
        with st.container(border=True):
            st.markdown("### 🦟 Kedokteran Tropis (KedTrop)")
            st.caption("Infeksi Tropis, DHF, Malaria, Demam Tifoid, dan Parasitologi.")
            st.link_button("📂 Buka Folder KedTrop", "https://drive.google.com/drive/folders/1IVspdEFwRoRCPx1_BYAZnN0woRDAM3WD?usp=sharing", use_container_width=True, type="primary")

    # Baris 3
    col5, col6 = st.columns(2)
    with col5:
        with st.container(border=True):
            st.markdown("### 🧠 Neuropsikiatri")
            st.caption("Neurologi (Saraf), Stroke, Kejang, serta Gangguan Psikiatri.")
            st.link_button("📂 Buka Folder Neuropsikiatri", "https://drive.google.com/drive/folders/1yRrmN1AgK-9bHg8DPAsAqEyvzN5hDCV2?usp=sharing", use_container_width=True, type="primary")

    with col6:
        with st.container(border=True):
            st.markdown("### 🫁 Pulmonologi & Respirasi")
            st.caption("Sistem Respirasi, Asma, PPOK, Tuberculosis (TB), dan Pneumonia.")
            st.link_button("📂 Buka Folder Respirasi", "https://drive.google.com/drive/folders/1s42ZzH7ay4rKu_YaNlj6-Ox8HjT66D3e?usp=sharing", use_container_width=True, type="primary")

    # Baris 4
    col7, col8 = st.columns(2)
    with col7:
        with st.container(border=True):
            st.markdown("### 👁️ Special Sense (Indera)")
            st.caption("Indera Mata, Telinga Hidung Tenggorokan (THT), dan Dermatologi.")
            st.link_button("📂 Buka Folder Special Sense", "https://drive.google.com/drive/folders/1MFWypf6XLL1Wz1-dqUG8058xG7_h8fk9?usp=sharing", use_container_width=True, type="primary")

    with col8:
        with st.container(border=True):
            st.markdown("### 🚽 Urologi & Ginjal")
            st.caption("Saluran Kemih, Infeksi Saluran Kemih (ISK), BPH, dan Ginjal.")
            st.link_button("📂 Buka Folder Urologi", "https://drive.google.com/drive/folders/1sxsFjKpncecy4HcsjtmVDQGFYqZoWy8N?usp=sharing", use_container_width=True, type="primary")


# ==========================================
# TAB 2: SISTEM TRYOUT CBT
# ==========================================
with tab_tryout:
    st.subheader("Simulasi Ujian Computer Based Test (CBT)")
    st.write("Centang kotak di bawah ini untuk memulai pengerjaan soal interaktif.")
    
    mulai_ujian = st.checkbox("Mulai Simulasi Tryout Sekarang")
    
    if mulai_ujian:
        st.divider()

        # Inisialisasi Bank Soal di Session State
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
            st.markdown(f"### **Soal No. {df.loc[idx, 'No']} dari {total_soal}**")
            st.markdown(f"**{df.loc[idx, 'Soal']}**")
            
            opsi = [
                f"A. {df.loc[idx, 'A']}", 
                f"B. {df.loc[idx, 'B']}", 
                f"C. {df.loc[idx, 'C']}", 
                f"D. {df.loc[idx, 'D']}"
            ]
            
            pilihan = st.radio("Pilih jawaban:", opsi, index=None, key=f"ans_{idx}")
            
            st.write("") # Margin spacing
            
            # Kolom Tombol
            col_btn1, col_btn2 = st.columns([1, 4])
            
            with col_btn1:
                if st.button("Cek Jawaban", disabled=(pilihan is None), use_container_width=True):
                    st.session_state.sudah_cek = True
            
            if st.session_state.sudah_cek:
                jawaban_user = pilihan.split(".")[0] if pilihan else ""
                jawaban_benar = df.loc[idx, 'Jawaban']
                
                if jawaban_user == jawaban_benar:
                    st.success(f"✅ **Jawaban kamu BENAR! ({jawaban_benar})**")
                else:
                    st.error(f"❌ **Jawaban kamu SALAH! Jawaban yang benar adalah {jawaban_benar}**")
                    
                st.info(f"**Pembahasan:**\n\n{df.loc[idx, 'Pembahasan']}")
                
                with col_btn2:
                    if st.button("Selanjutnya ➡️", type="primary"):
                        st.session_state.soal_sekarang += 1
                        st.session_state.sudah_cek = False
                        st.rerun()
        else:
            st.balloons()
            st.success("🎉 **Selesai!** Kamu telah menyelesaikan simulasi tryout kali ini.")
            if st.button("Ulang Ujian 🔄", type="primary"):
                st.session_state.soal_sekarang = 0
                st.session_state.sudah_cek = False
                st.rerun()
