# Analisis Keputusan Bisnis - Business Framing TM 2

## 📌 Deskripsi Tugas
Tugas ini merupakan simulasi studi kasus bisnis berbasis data, dimana mahasiswa berperan sebagai **tim Data Science** di sebuah marketplace e-commerce di Brasil yang sedang menghadapi tantangan bisnis. Perusahaan mengalami peningkatan keluhan pelanggan dan perlambatan pertumbuhan transaksi.

Dalam rapat manajemen, muncul **tiga pandangan berbeda** mengenai akar masalah:
- **Tim Operasional** → Masalah utama adalah **keterlambatan pengiriman**
- **Tim Produk** → Masalah utama adalah **kualitas seller/produk yang buruk** (tercermin dari review rendah)
- **Tim Finance** → Masalah utama adalah **biaya pengiriman terlalu tinggi**, sehingga pelanggan enggan order ulang

Manajemen meminta tim Data Science untuk memberikan rekomendasi. **Namun, sebelum membuat model apapun, tim harus menjawab pertanyaan fundamental:**
> "Apa sebenarnya masalah bisnisnya dan keputusan apa yang perlu diambil?"

## 🎯 Tujuan Pembelajaran
Tugas ini bertujuan melatih **kemampuan business framing**, yaitu:
- Membedakan antara masalah teknis dan masalah bisnis
- Menggunakan data untuk memvalidasi asumsi bisnis
- Menyusun rekomendasi keputusan berdasarkan bukti, bukan opini
- Mengkomunikasikan hasil analisis secara ringkas dan tajam

## 📂 Sumber Data
**Dataset:** Brazilian E-Commerce Public Dataset (Olist)
**Link:** [Kaggle - Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Tabel utama yang digunakan:**
- `orders.csv` - data pesanan
- `order_items.csv` - item dalam setiap pesanan
- `payments.csv` - metode pembayaran
- `reviews.csv` - ulasan pelanggan

## 🧩 Tugas Utama
Tim mahasiswa harus:

### 1. **Menentukan Business Framing**
Pilih **satu** dari tiga framing berikut berdasarkan bukti awal dari data:
- **Framing 1:** Masalah utama adalah keterlambatan pengiriman
- **Framing 2:** Masalah utama adalah kualitas seller/produk (review buruk)
- **Framing 3:** Masalah utama adalah ongkir tinggi (melemahkan repeat order)

### 2. **Mengisi Decision Canvas Sederhana**
Jelaskan keputusan yang perlu diambil, siapa pengambil keputusan, dan data pendukung.

### 3. **Menyediakan Bukti Data Minimal**
Gunakan dataset yang sudah diolah untuk mendukung framing pilihan.

## 📊 Regulasi Analisis
1. **Bangun dataset level-order** dengan menggabungkan tabel: orders, order_items, payments, reviews
2. **Buat minimal 2 variabel turunan:**
   - **Delivery:** delivery duration, timeliness status (on-time vs late)
   - **Quality:** distribusi review score, konsentrasi seller/kategori dengan review rendah
   - **Freight:** freight ratio (biaya kirim / nilai belanja) atau kategori biaya kirim
3. **Analisis eksploratif dasar** (tren, perbandingan rata-rata, konsentrasi isu) — **tidak wajib membuat model prediksi**

## 📤 Luaran Tugas

### A. **Decision Memorandum** (maksimal 1 halaman)
Berisi:
- Pernyataan masalah (1-2 kalimat)
- Pemilihan framing + alasan singkat
- Rekomendasi keputusan bisnis untuk minggu ini
- Tiga alternatif tindakan (termasuk opsi "tidak melakukan apa-apa") + trade-off
- Satu metrik utama untuk mengukur keberhasilan
- Risiko jika salah pilih framing

### B. **Appendix Evidence Data** (maksimal 2 halaman/slide)
Berisi:
- Satu grafik baseline (misal: tren ketepatan waktu / rata-rata ulasan)
- Dua tabel komparatif yang mendukung framing
- Satu paragraf interpretasi: **"Apa bukti paling substansial yang mendasari pilihan framing?"**

## 🛠️ Teknologi yang Digunakan
- **Python 3.x** dengan library:
  - Pandas (manipulasi data)
  - NumPy (komputasi numerik)
  - Matplotlib/Seaborn (visualisasi)
  - Jupyter Notebook (analisis interaktif)
- **Git** untuk version control
- **GitHub** untuk kolaborasi dan penyimpanan

## 👥 Kelompok 1 Analisis Keputusan Bisnis
**Anggota:**
- [Nama Anggota 1]
- [Nama Anggota 2]
- [Nama Anggota 3]
- [Nama Anggota 4]

**Dosen Pengampu:** [Nama Dosen]

## 📅 Timeline
- **Minggu 1:** Eksplorasi data dan business framing
- **Minggu 2:** Analisis mendalam dan pembuatan variabel turunan
- **Minggu 3:** Penyusunan decision memorandum dan appendix evidence
- **Minggu 4:** Finalisasi dan presentasi hasil

## 🔗 Referensi
1. Brazilian E-Commerce Public Dataset by Olist
2. Business Framing Framework - Harvard Business Review
3. Data-Driven Decision Making - MIT Sloan Management Review

---
**Catatan:** Repository ini dibuat untuk mendukung pembelajaran Analisis Keputusan Bisnis dengan pendekatan berbasis data dan business framing yang tepat.