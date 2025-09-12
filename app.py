import streamlit as st

# Inisialisasi state
if "page" not in st.session_state:
    st.session_state.page = 1
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "jawaban" not in st.session_state:
    st.session_state.jawaban = {}

# Halaman 1 - Input Nama
if st.session_state.page == 1:
    st.title("🧠 Mini Quiz App: Profesi yang cocok untukmu di Tech Industry")
    st.session_state.nama = st.text_input("Masukkan Nama:")

    if st.button("Mulai Quiz") and st.session_state.nama.strip() != "":
        st.session_state.page = 2
        st.rerun()

# Halaman 2 - Pertanyaan Quiz
elif st.session_state.page == 2:
    st.title(f"Halo _:yellow[{st.session_state.nama}]_, Kamu cocok jadi apa di Tech Industry?")
    st.markdown("Jawab beberapa pertanyaan singkat ini untuk menemukan peran yang paling cocok buat kamu!:sunglasses:")

    # Pertanyaan 1 
    st.header("1. Kalau lagi waktu senggang, aktivitas apa yang paling seru buat kamu?")
    q1 = st.radio("Pilih satu:", [
        "Main teka-teki logika atau pecahin coding challenge 🧠",  # Programmer
        "Nge-sketch atau utak-atik desain di Figma ✏️",  # Designer
        "Ngeliatin data atau tren yang lagi happening 📊"  # Data Scientist
    ], key="q1")

    # Pertanyaan 2
    st.header("2. Menurut kamu, skill utama yang kamu banggain apa?")
    q2 = st.radio("Pilih satu:", [
        "Nalar logis yang tajam dan mikir sistematis.",  # Programmer
        "Kreativitas dan imajinasi yang nggak biasa.",  # Designer
        "Jago analisis dan super detail-oriented."  # Data Scientist
    ], key="q2")

    # Pertanyaan 3
    st.header("3. Kalo dikasih proyek, yang mana yang bikin kamu semangat?")
    q3 = st.radio("Pilih satu:", [
        "Bikin atau develop suatu aplikasi dari nol. 💻",  # Programmer
        "Design UI/UX yang bikin user experience mulus banget. 🎨",  # Designer
        "Ngelahirin insight keren dari analisis data yang gede. 📈"  # Data Scientist
    ], key="q3")

    # Pertanyaan 4
    st.header("4. Biasanya, gimana style kamu waktu menghadapi suatu masalah?")
    q4 = st.radio("Pilih satu:", [
        "Bikin algoritma atau urutan langkah yang rapi.",  # Programmer
        "Visualize solusi yang estetik dan easy-to-use.",  # Designer
        "Kumpulin dan analisis semua data yang ada dulu."  # Data Scientist
    ], key="q4")

    # Pertanyaan 5
    st.header("5. Di dunia tech, bagian apa yang paling bikin kamu tertarik?")
    q5 = st.radio("Pilih satu:", [
        "Gimana sebuah sistem atau bahasa pemrograman bisa jalan.",  # Programmer
        "Estetika dan experience dari sebuah desain interface.",  # Designer
        "Kekuatan data buat pengambilan keputusan yang tepat."  # Data Scientist
    ], key="q5")

    # Tombol untuk melihat hasil
    if st.button("Lihat Hasil!"):
        # Simpan jawaban
        st.session_state.jawaban = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5 }
        
        # Atur skor awal
        skor_programmer = 0
        skor_designer = 0
        skor_datascientist = 0
        
        # Hitung skor untuk setiap jawaban
        # Pertanyaan 1
        if q1 == "Main teka-teki logika atau pecahin coding challenge 🧠":
            skor_programmer += 1
        elif q1 == "Nge-sketch atau utak-atik desain di Figma ✏️":
            skor_designer += 1
        elif q1 == "Ngeliatin data atau tren yang lagi happening 📊":
            skor_datascientist += 1

        # Pertanyaan 2
        if q2 == "Nalar logis yang tajam dan mikir sistematis.":
            skor_programmer += 1
        elif q2 == "Kreativitas dan imajinasi yang nggak biasa.":
            skor_designer += 1
        elif q2 == "Jago analisis dan super detail-oriented.":
            skor_datascientist += 1
        
        # Pertanyaan 3
        if q3 == "Bikin atau develop suatu aplikasi dari nol. 💻":
            skor_programmer += 1
        elif q3 == "Design UI/UX yang bikin user experience mulus banget. 🎨":
            skor_designer += 1
        elif q3 == "Ngelahirin insight keren dari analisis data yang gede. 📈":
            skor_datascientist += 1
        
        # Pertanyaan 4
        if q4 == "Bikin algoritma atau urutan langkah yang rapi.":
            skor_programmer += 1
        elif q4 == "Visualize solusi yang estetik dan easy-to-use.":
            skor_designer += 1
        elif q4 == "Kumpulin dan analisis semua data yang ada dulu.":
            skor_datascientist += 1
        
        # Pertanyaan 5
        if q5 == "Gimana sebuah sistem atau bahasa pemrograman bisa jalan.":
            skor_programmer += 1
        elif q5 == "Estetika dan experience dari sebuah desain interface.":
            skor_designer += 1
        elif q5 == "Kekuatan data buat pengambilan keputusan yang tepat.":
            skor_datascientist += 1

        # Simpan skor
        st.session_state.skor = { "Programmer": skor_programmer, "Designer": skor_designer, "Data Scientist": skor_datascientist}
        
        # Pindah ke halaman hasil
        st.session_state.page = 3
        st.rerun()

# Halaman 3 - Hasil
elif st.session_state.page == 3:
    st.title(f"Yeayy _:yellow[{st.session_state.nama}]_, Ini Hasil Quiz-mu! 🎯")
    # Tentukan peran dengan skor tertinggi
    max_score = max(st.session_state.skor.values())
    max_roles = [role for role, score in st.session_state.skor.items() if score == max_score]
    
    if len(max_roles) == 1:
        if max_roles[0] == "Programmer":
            st.balloons()
            st.success("🔥 Kamu cocok banget jadi Programmer! Let's code! 💻")
            st.image("https://cdn-icons-png.flaticon.com/512/2920/2920277.png", width=150)
            st.markdown("""
            **Deskripsi:**
            Kamu memiliki pola pikir logis dan analitis yang kuat. Sebagai programmer, kamu akan menikmati 
            pemecahan masalah kompleks dan pembuatan solusi inovatif melalui kode.
            
            **Apa yang dilakukan Programmer?**
            - Menulis, menguji, dan memelihara kode untuk aplikasi dan sistem
            - Memecahkan masalah teknis dan debugging
            - Berkolaborasi dengan tim untuk mengembangkan produk digital
            - Terus belajar teknologi dan bahasa pemrograman terbaru
            
            **Skill yang diperlukan:**
            - Logika dan algoritma yang kuat
            - Penguasaan bahasa pemrograman (Python, JavaScript, dll)
            - Kemampuan problem-solving yang tajam
            - Attention to detail
            """)
        elif max_roles[0] == "Designer":
            st.balloons()
            st.success("🎨 Kamu cocok banget jadi UI/UX Designer! Let's create! ✨")
            st.image("https://cdn-icons-png.flaticon.com/512/2920/2920336.png", width=150)
            st.markdown("""
            **Deskripsi:**
            Kreativitas dan estetika adalah kekuatanmu. Sebagai designer, kamu akan unggul dalam 
            menciptakan pengalaman visual yang menarik dan fungsional bagi pengguna.
            
            **Apa yang dilakukan Designer?**
            - Merancang antarmuka pengguna (UI) yang intuitif dan menarik
            - Menciptakan pengalaman pengguna (UX) yang mulus
            - Membuat prototipe dan mockup untuk produk digital
            - Berkolaborasi dengan developer untuk menerapkan desain
            
            **Skill yang diperlukan:**
            - Kreativitas dan sense of aesthetics
            - Pemahaman tentang prinsip UX
            - Penguasaan tools design (Figma, Adobe XD, dll)
            - Empati terhadap kebutuhan pengguna
            """)
        else: # Data Scientist
            st.balloons()
            st.success("📊 Kamu cocok banget jadi Data Scientist! Let's analyze! 🔍")
            st.image("https://cdn-icons-png.flaticon.com/512/2920/2920330.png", width=150)
            st.markdown("""
            **Deskripsi:**
            Kamu memiliki kemampuan analitis yang tajam dan minat dalam menemukan pola tersembunyi. 
            Sebagai data scientist, kamu akan menjelajahi data untuk mendapatkan wawasan berharga.
            
            **Apa yang dilakukan Data Scientist?**
            - Mengumpulkan, membersihkan, dan menganalisis data
            - Membuat model prediktif dan machine learning
            - Visualisasi data untuk komunikasi insight
            - Memberikan rekomendasi berdasarkan analisis data
            
            **Skill yang diperlukan:**
            - Analisis statistik dan matematika
            - Pemrograman untuk analisis data (Python, R, SQL)
            - Pemahaman machine learning
            - Kemampuan storytelling dengan data
            """)
    else:
        st.snow()
        st.success(f"🎭 Kamu memiliki bakat di beberapa bidang: {len(max_roles)}{', '.join(max_roles)}!")
        st.image("https://cdn-icons-png.flaticon.com/512/3767/3767084.png", width=150)

        # Tentukan role hybrid berdasarkan kombinasi
        hybrid_roles = []
        if "Programmer" in max_roles and "Designer" in max_roles:
            hybrid_roles.append("Product Designer")
        if "Programmer" in max_roles and "Data Scientist" in max_roles:
            hybrid_roles.append("Data Engineer")
        if "Designer" in max_roles and "Data Scientist" in max_roles:
            hybrid_roles.append("UX Researcher") 

        st.markdown(f""" 
        ### :sunglasses: 🌟 Kamu Punya Bakat Ganda! 
        Hasil quiz menunjukkan bahwa kamu memiliki kombinasi skill yang berharga. 
        Kamu berpotensi di bidang: {', '.join(max_roles)}
        
        ### Saran Pengembangan:
        1. **Eksplorasi kedua bidang** untuk menemukan passion terkuatmu
        2. **Cari role hybrid** seperti {', '.join(hybrid_roles) if hybrid_roles else 'Product Manager atau Tech Lead'}
        3. **Terus belajar dan praktik** di kedua area untuk memperkuat skill-mu
        """)
    
    # Tampilkan skor detail
    with st.expander("Lihat detail skor"):
        st.write(f"Programmer: {st.session_state.skor['Programmer']} poin")
        st.write(f"Designer: {st.session_state.skor['Designer']} poin")
        st.write(f"Data Scientist: {st.session_state.skor['Data Scientist']} poin")
    
    if st.button("Ulangi Quiz"):
        st.session_state.page = 1
        st.rerun()

    # Tombol untuk berbagi hasil
    st.markdown("---")
    st.markdown("### 📣 Share hasil ini ke squad-mu!")
    share_text = f"Hai! Aku baru saja mengikuti quiz 'Profesi yang cocok untukmu di Tech Industry' dan hasilnya aku cocok jadi {', '.join(max_roles)}! Coba deh kamu juga! #TechQuiz"

# Footer
st.markdown("---")
st.caption("Mini Quiz App © 2025 | Dibuat dengan ❤️ pake Codespaces & Streamlit")