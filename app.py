import streamlit as st
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import pickle
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pandas as pd

# Inisialisasi stemmer sekali aja
factory = StemmerFactory()
stemmer = factory.create_stemmer()
model = pickle.load(open('BeritaHoaxPredictor(logreg).1.3.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer(logreg).1.3.pkl', 'rb'))

def sastrawi(konten):
    """
    Melakukan stemming pada teks Bahasa Indonesia menggunakan Sastrawi.
    Parameter:
        konten (str): Kalimat atau teks yang ingin diproses
    Return:
        str: Teks hasil stemming
    """
    if not isinstance(konten, str):
        konten = str(konten)

    # Lowercase
    konten = konten.lower()

    # Hapus karakter non-alfabet (angka, simbol, dsb)
    konten = re.sub(r'[^a-z\s]', ' ', konten)

    # Hapus spasi berlebih
    konten = re.sub(r'\s+', ' ', konten).strip()

    # Stemming
    hasil = stemmer.stem(konten)

    return hasil

def system_predictor(narasi, judul, model):
  # Preprocessing narasi dan judul
  konten = pd.DataFrame({'narasi': [narasi], 'judul': [judul]})
  konten_val = konten.values
  konten_preprocesed = sastrawi(konten_val)
  text_vector = vectorizer.transform([konten_preprocesed])

  # Predict
  prediction = model.predict(text_vector)
  proba = model.predict_proba(text_vector)
  return prediction, proba

def main():

    # Inject custom CSS
    st.markdown("""
        <style>
            .header-container {
                background-color: #001f3f;
                padding: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                margin-bottom: 2rem;
            }
            
            .header-container1 {
                background-color: #0074D9;
                padding: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                margin-bottom: 2rem;
            }

            .header-title {
                color: white;
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 0.5rem;
            }

            .header-subtitle {
                color: #CCCCCC;
                font-size: 28px;
                text-align: center;
            }
            
            @media (max-width: 768px) {
                .header-title {
                    font-size: 28px;
                }
                .header-subtitle {
                    font-size: 14px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu("Menu", ["Berita Hoax Predictor", "About", "Contact"], icons = ['newspaper', 'question-circle-fill', 'person-lines-fill'],default_index=0)
    
    # Home Page 
    if (selected == "About"):
        st.markdown("""
            <div class="header-container">
                <div class="header-title">Tentang Aplikasi ❓</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        **BeritaHoaxPredictor** adalah aplikasi berbasis Machine Learning yang dirancang untuk membantu masyarakat memverifikasi kebenaran suatu berita secara cepat dan mudah.

        Di era digital saat ini, penyebaran hoax sangat masif, terutama di media sosial. Aplikasi ini hadir sebagai bentuk kontribusi kecil untuk meningkatkan literasi digital dan memerangi informasi palsu.
        """)

        st.markdown("---")
        st.markdown("""
                    <div class="header-container1">
                        <div class="header-subtitle">🔍 Cara Kerja Aplikasi</div>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("""
        1. Pengguna memasukkan isi berita (judul atau isi lengkap).
        2. Teks berita diproses menggunakan Natural Language Processing.
        3. Model Machine Learning memprediksi apakah berita tersebut **hoax** atau **fakta**.
        """)

        st.markdown("---")
        st.markdown("""
                    <div class="header-container1">
                        <div class="header-subtitle">🧠 Teknologi yang Digunakan</div>
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown("""
        - **Python**: Bahasa pemrograman utama.
        - **Streamlit**: Untuk membangun antarmuka pengguna (UI).
        - **Scikit-learn / TensorFlow**: Untuk membangun model prediksi.
        - **TF-IDF & NLP Libraries**: Untuk ekstraksi fitur dari teks.
        """)

        st.markdown("---")
        st.markdown("""
                    <div class="header-container1">
                        <div class="header-subtitle">👨‍💻 Tentang Pengembang</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image("Unknown.png", caption="Kuro")
        st.markdown("""
        **BeritaHoaxPredictor** dikembangkan oleh saya **Kuro**, seorang pelajar SMA yang memiliki ketertarikan mendalam di bidang **Artificial Intelligence**, **Data Science**, dan **pemrograman kreatif**.

        Saya suka dikenal sebagai pribadi yang suka mengeksplorasi hal-hal baru, selalu penasaran terhadap "bagaimana sesuatu bekerja", dan memiliki komitmen tinggi terhadap pembelajaran mandiri. Saya tidak hanya belajar untuk sekadar tahu, tetapi untuk **memahami secara mendalam** dan memegang prinsip bahwa memahami lebih penting daripada sekadar menghafal.

        Di balik proyek ini, ada semangat untuk menjadikan teknologi sebagai alat pemecah masalah nyata, terutama dalam melawan penyebaran informasi palsu di era digital. Saya percaya bahwa bahkan seorang pelajar pun bisa membuat kontribusi nyata jika didukung oleh keinginan belajar, eksperimen, dan niat baik.

        > _"Keep exploring no matter how hard the path is."_  
        > — Kuro

        Selain aktif dalam pengembangan AI, Saya juga tertarik dengan pendidikan, public speaking, dan pengembangan komunitas berbasis teknologi. Melalui proyek-proyek yang saya buat, saya berharap bisa menginspirasi lebih banyak generasi muda untuk tidak takut mengeksplorasi ide dan menciptakan sesuatu yang berdampak.
        """)


    if (selected == "Contact"):

        st.markdown("""
            <div class="header-container">
                <div class="header-title">📬 Hubungi Saya</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        Saya terbuka untuk kolaborasi, masukan, atau pertanyaan lebih lanjut.  
        Silakan hubungi Saya melalui kontak berikut:
        """)

        st.markdown("---")
        st.subheader("📱 Kontak Langsung")
        st.markdown("""
        - 📧 Email: `codewkuro@gmail.com`
        - 🐙 GitHub: [github.com/codexkuro](https://github.com/codexkuro)
        - 📷 Instagram: [@codexkuro](https://www.instagram.com/codexkuro?igsh=c3oxNjlieTQ0MW10)
        """)

        st.markdown("---")
        st.subheader("💡 Masukan atau Kritik?")

        st.info("Form pengiriman pesan belum aktif. Silakan hubungi Saya langsung via kontak di atas.")


    # Berita Hoax Predictor Page
    if (selected == "Berita Hoax Predictor"):
        # Header Section
        st.markdown("""
            <div class="header-container">
                <div class="header-title">📰 BeritaHoaxPredictor</div>
                <div class="header-subtitle">Deteksi kebenaran berita dengan teknologi Machine Learning</div>
            </div>
        """, unsafe_allow_html=True)
        with open("animejoget.json", "r", encoding="utf-8") as f:
            lottie_dance = json.load(f)
        st_lottie(lottie_dance, height=300)

        # Custom info box di bawah header
        st.markdown("""
            <div style="
                background-color: #0074D9;
                padding: 1rem 2rem;
                margin-bottom: 2rem;
                border-radius: 0.8rem;
                color: #CCCCCC;
                font-size: 15px;
                max-width: 100%;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            ">
                Masukkan judul dan narasi berita untuk melakukan prediksi apakah berita tersebut hoax atau valid.
                Gunakan bahasa Indonesia yang baik dan benar untuk hasil yang optimal.
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            judul = st.text_input("Masukkan Judul Berita:")
            narasi = st.text_area("Masukkan Narasi Berita:")
            prediksi = st.button("Prediksi")
        with col2:
            if prediksi:
                if narasi and judul:
                    # Panggil fungsi untuk melakukan prediksi
                    prediction, proba = system_predictor(narasi, judul, model)
                    if prediction[0] == 1:
                        st.error("Berita ini kemungkinan **Hoax**!\nCiri-ciri berita hoax:\n- Mengandung informasi yang tidak dapat diverifikasi\n- Sering menggunakan judul yang sensasional\n- Memuat klaim tanpa sumber yang jelas")
                        st.write(f"Probabilitas Hoax: {proba[0][1]:.2f}\tProbabilitas Valid: {proba[0][0]:.2f}")
                    else:
                        st.success("Berita ini kemungkinan **Valid**!\nCiri-ciri berita valid:\n- Memuat informasi yang dapat diverifikasi\n- Sering mencantumkan sumber yang jelas\n- Menggunakan bahasa yang netral")
                        st.write(f"Probabilitas Valid: {proba[0][0]:.2f}\tProbabilitas Hoax: {proba[0][1]:.2f}")
                else:
                    st.error("Mohon masukkan narasi dan judul berita.")
            else:
                pass
        
    

if __name__ == "__main__":
    main()