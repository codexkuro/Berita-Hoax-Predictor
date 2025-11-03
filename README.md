# Berita-Hoax-Predictor
Aplikasi berbasis Machine Learning untuk mendeteksi apakah suatu berita termasuk hoaks atau bukan.

## ✨ Deskripsi
Berita-Hoax-Predictor adalah sebuah aplikasi yang dikembangkan untuk membantu masyarakat dalam memverifikasi kebenaran sebuah berita secara cepat dan mudah. Dengan menggunakan model pembelajaran mesin dan vektorisasi teks, aplikasi ini berupaya memerangi disinformasi dan meningkatkan literasi digital.

## 🎯 Fitur Utama
- Input berupa teks berita (judul, isi, atau keduanya)
- Prediksi otomatis apakah berita tersebut tergolong **Hoaks** atau **Bukan Hoaks**
- Model sudah dilatih sebelumnya (Logistic Regression)
- Menggunakan vektorisasi teks untuk pengolahan berita berbahasa Indonesia
- Antarmuka sederhana untuk memudahkan penggunaan

## 💾 Struktur Repository
```

├── app.py                           ← Skrip utama aplikasi untuk pengguna (UI / CLI)
├── vectorizer(logreg).1.3.pkl       ← File vektorisasi (pickle)
├── BeritaHoaxPredictor(logreg).1.3.pkl ← Model Machine Learning terlatih (pickle)
├── requirements.txt                 ← Daftar dependency Python
└── README.md                        ← Dokumentasi ini

````

## 🚀 Instalasi & Penggunaan
1. Clone repositori:
```bash
git clone https://github.com/codexkuro/Berita-Hoax-Predictor.git
cd Berita-Hoax-Predictor
````

2. Pasang virtual environment (opsional tapi direkomendasikan):

```bash
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

3. Install requirement:

```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi:

```bash
python app.py
```

5. Ikuti instruksi yang muncul (masukkan teks berita, sistem akan memprediksi statusnya: Hoaks / Bukan Hoaks).

## 🧠 Cara Kerja

1. Teks berita diinput oleh pengguna.
2. Teks diproses dan di-vektorisasi menggunakan `vectorizer(logreg).1.3.pkl`.
3. Vektor yang terbentuk diberikan ke model `BeritaHoaxPredictor(logreg).1.3.pkl` untuk menghasilkan prediksi.
4. Hasil prediksi ditampilkan ke pengguna.

## 🛠️ Kontribusi

Kami sangat menghargai kontribusi! Jika ingin:

* Memperbaiki bug
* Memperluas fungsi (misal dukungan multibahasa, UI web, API REST)
* Meningkatkan akurasi model dengan dataset lebih besar

Silakan buat *fork*, lakukan perubahan, lalu ajukan *pull request*.

Pastikan:

* Menjalankan `pip install -r requirements.txt` dan menguji bahwa perubahan tidak merusak fitur yang ada
* Menulis komit yang jelas dan deskriptif
* Menambahkan dokumentasi jika menambahkan fitur baru

## 📄 Lisensi

Lisensi untuk proyek ini: MIT License
© 2025 codexkuro

## 📞 Kontak

Jika ada pertanyaan, silakan hubungi: @akbrsmh.
Terima kasih atas minat dan kontribusinya untuk membantu masa depan informasi yang lebih baik!
