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
            st.link_button("📂 Buka Folder Endokrin", "https://drive.google.com/drive/folders/1PlPLzWMb4LHTJtM36ZvUn_I8dr2Aty8Z?usp=sharing", use_container_width=True, type="primary")

    with col2:
        with st.container(border=True):
            st.markdown("### 🥑 Gastroenterohepatologi")
            st.caption("Sistem Pencernaan, Hati, Saluran Empedu, dan Gastrointestinal.")
            st.link_button("📂 Buka Folder Gastro", "https://drive.google.com/drive/folders/1wxjrjykHwZ-ZhF6SHj5MiRpQ5MAjFJKi?usp=sharing", use_container_width=True, type="primary")

    # Baris 2
    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            st.markdown("### ❤️ Kardiologi & Vaskular")
            st.caption("Kardiovaskular, EKG, Penyakit Jantung Koroner, dan Hipertensi.")
            st.link_button("📂 Buka Folder Kardiologi", "https://drive.google.com/drive/folders/1doZFx_pEHBf6vZvqgpU7JcHmzLvW03T1?usp=sharing", use_container_width=True, type="primary")

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
# TAB 2: SISTEM TRYOUT CBT (MODEL UJIAN SUNGGUHAN)
# ==========================================
with tab_tryout:
    st.subheader("Simulasi Ujian Computer Based Test (CBT)")
    st.write("Centang kotak di bawah ini untuk memulai pengerjaan soal interaktif.")
    
    mulai_ujian = st.checkbox("Mulai Simulasi Tryout Sekarang")
    
    if mulai_ujian:
        st.divider()

        # Load bank soal dari excel
        if 'data_soal' not in st.session_state:
            try:
                df_soal = pd.read_excel("bank_soal.xlsx")
                st.session_state.data_soal = df_soal
            except Exception as e:
                st.error(f"⚠️ Terjadi kesalahan saat membaca `bank_soal.xlsx`: {e}")
                st.stop()

        # Inisialisasi State Ujian
        if 'soal_sekarang' not in st.session_state:
            st.session_state.soal_sekarang = 0
        if 'jawaban_user' not in st.session_state:
            st.session_state.jawaban_user = {}  # Format: {idx_soal: 'A'}
        if 'ujian_selesai' not in st.session_state:
            st.session_state.ujian_selesai = False

        df = st.session_state.data_soal
        total_soal = len(df)
        idx = st.session_state.soal_sekarang

        # ------------------------------------------
        # A. HALAMAN PENGERJAAN SOAL
        # ------------------------------------------
        if not st.session_state.ujian_selesai:
            # Progress Bar
            progress = (idx + 1) / total_soal
            st.progress(progress, text=f"Soal No. {idx + 1} dari {total_soal}")

            st.markdown(f"### **Soal No. {df.loc[idx, 'No']}**")
            st.markdown(f"**{df.loc[idx, 'Soal']}**")

            # Susun Pilihan Jawaban (A - E)
            opsi = [
                f"A. {df.loc[idx, 'A']}", 
                f"B. {df.loc[idx, 'B']}", 
                f"C. {df.loc[idx, 'C']}", 
                f"D. {df.loc[idx, 'D']}"
            ]
            if 'E' in df.columns and pd.notna(df.loc[idx, 'E']):
                opsi.append(f"E. {df.loc[idx, 'E']}")

            # Ambil jawaban yang sebelumnya sudah pernah dipilih (jika ada)
            jawaban_sebelumnya = st.session_state.jawaban_user.get(idx, None)
            
            # Cari index dari jawaban sebelumnya untuk default radio button
            index_default = None
            if jawaban_sebelumnya:
                for i, o in enumerate(opsi):
                    if o.startswith(jawaban_sebelumnya):
                        index_default = i
                        break

            # Radio Button Opsi Jawaban
            pilihan = st.radio(
                "Pilih jawaban:", 
                opsi, 
                index=index_default, 
                key=f"radio_soal_{idx}"
            )

            # Simpan pilihan ke session_state setiap kali user memilih
            if pilihan:
                st.session_state.jawaban_user[idx] = pilihan.split(".")[0]

            st.write("") # Margin Spacing

            # Navigasi Tombol (Sebelumnya, Selanjutnya, Selesai)
            col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 2])

            with col_nav1:
                if st.button("⬅️ Sebelumnya", disabled=(idx == 0), use_container_width=True):
                    st.session_state.soal_sekarang -= 1
                    st.rerun()

            with col_nav2:
                if idx < total_soal - 1:
                    if st.button("Selanjutnya ➡️", type="primary", use_container_width=True):
                        st.session_state.soal_sekarang += 1
                        st.rerun()

            with col_nav3:
                # Tombol Selesai Ujian hanya muncul jika sudah di nomor terakhir atau kapan saja
                if idx == total_soal - 1:
                    if st.button("🏁 Selesai & Kumpulkan Ujian", type="primary", use_container_width=True):
                        st.session_state.ujian_selesai = True
                        st.rerun()

        # ------------------------------------------
        # B. HALAMAN HASIL & REKAPITULASI SOAL
        # ------------------------------------------
        else:
            st.balloons()
            st.subheader("📊 Hasil Simulasi Tryout CBT")

            # Hitung Nilai Benar & Salah
            benar = 0
            salah = 0
            tidak_dijawab = 0

            for i in range(total_soal):
                jawaban_user = st.session_state.jawaban_user.get(i, None)
                jawaban_benar = str(df.loc[i, 'Jawaban']).strip().upper()

                if jawaban_user is None:
                    tidak_dijawab += 1
                elif jawaban_user == jawaban_benar:
                    benar += 1
                else:
                    salah += 1

            skor_persen = round((benar / total_soal) * 100, 1)

            # Tampilkan Ringkasan Nilai Menggunakan Metrik Streamlit
            col_res1, col_res2, col_res3, col_res4 = st.columns(4)
            col_res1.metric("Skor Akhir", f"{skor_persen}%")
            col_res2.metric("Jawaban Benar ✅", f"{benar} Soal")
            col_res3.metric("Jawaban Salah ❌", f"{salah} Soal")
            col_res4.metric("Kosong ⚪", f"{tidak_dijawab} Soal")

            st.divider()
            st.subheader("🔍 Review & Pembahasan Soal")

            # Tampilkan Rincian Tiap Soal
            for i in range(total_soal):
                jawaban_user = st.session_state.jawaban_user.get(i, "Tidak Dijawab")
                jawaban_benar = str(df.loc[i, 'Jawaban']).strip().upper()

                is_correct = (jawaban_user == jawaban_benar)
                status_icon = "✅" if is_correct else "❌"

                with st.expander(f"Soal No. {df.loc[i, 'No']} - Status: {status_icon}"):
                    st.markdown(f"**{df.loc[i, 'Soal']}**")
                    
                    st.write(f"- **Jawaban Kamu:** `{jawaban_user}`")
                    st.write(f"- **Jawaban Benar:** `{jawaban_benar}`")

                    if 'Pembahasan' in df.columns and pd.notna(df.loc[i, 'Pembahasan']):
                        st.info(f"**Pembahasan:**\n\n{df.loc[i, 'Pembahasan']}")

            st.divider()
            
            # Tombol Ulang Ujian
            if st.button("🔄 Ulang Simulasi Ujian", type="primary"):
                st.session_state.soal_sekarang = 0
                st.session_state.jawaban_user = {}
                st.session_state.ujian_selesai = False
                st.rerun()
