# 1. Decision Memorandum

**Decision Statement:**  
Kinerja bisnis marketplace e-commerce saat ini terhambat oleh tingginya keluhan pelanggan dan lambatnya pertumbuhan pesanan berulang (repeat order), yang akar permasalahannya berpusat pada keterlambatan pengiriman (delivery delay) pesanan ke konsumen.

**Pemilihan Kerangka dan Penjelasan Singkat:**  
**Framing 1: Masalah utama adalah keterlambatan pengiriman (delivery delay).**  
Alasan: Analisis eksploratif data menunjukkan perbedaan ekstrem pada tingkat kepuasan pelanggan; keterlambatan pengiriman bertindak sebagai penyebab utama ulasan buruk (rata-rata skor **1.63** untuk pesanan yang terlambat dibandingkan **4.18** untuk pesanan tepat waktu). Masalah ini menghancurkan pengalaman pelanggan terlepas dari kualitas barang yang dibeli atau biaya pengiriman.

**Rekomendasi Keputusan Bisnis untuk Minggu Ini:**  
Memperbarui sistem logika penghitungan Estimasi Waktu Kedatangan (Estimated Delivery Date) di halaman *checkout*, serta mengevaluasi mitra logistik (carrier) yang memiliki rasio *on-time* terendah untuk segera dialihkan kuota pengirimannya.

**Tiga Alternatif Tindakan & Trade-off Utama:**  
1. **Memperbarui Algoritma Estimasi Waktu Pengiriman (Rekomendasi)**  
   - *Trade-off:* Implementasi sistematis yang murah dan cepat untuk mengelola ekspektasi konsumen (mencegah review buruk). Namun, ETA yang ditampilkan akan lebih lama sehingga berisiko menurunkan tingkat konversi awal (*conversion rate*) karena pembeli melihat durasi pengiriman yang lama.
2. **Program Jaminan Tepat Waktu (Late-Delivery Guarantee - Cashback/Voucher)**  
   - *Trade-off:* Jaminan ini sangat ampuh menahan kekecewaan pembeli akibat keterlambatan dan menjaga loyalitas. Kelemahannya: membakar margin keuntungan (*high cost*) secara besar-besaran apabila kinerja pihak logistik belum diperbaiki. 
3. **Tidak Melakukan Apa-apa (Do Nothing)**  
   - *Trade-off:* Tidak membutuhkan alokasi sumber daya finansial/teknis baru (aman secara budget jangka pendek). Sayangnya, *churn rate* pembeli akan meningkat dan reputasi platform akan rusak dipenuhi *review* 1 bintang yang menghentikan tren akuisisi pengguna organik.

**Satu Metrik Utama untuk Mengukur Keberhasilan:**  
**On-Time Delivery Rate (%)** (Persentase pesanan yang sampai di tangan pembeli sama dengan atau lebih cepat dari perkiraan waktu pengiriman).

**Risiko Akibat Kesalahan dalam Frame:**  
Jika akar permasalahan sebenarnya ada pada kelalaian penjual yang lambat menyerahkan paket ke kurir setelah dibayar (keterlambatan dari pemrosesan toko, bukan murni logistik kurir), maka perbaikan operasional dan sanksi yang kita terapkan pada kurir menjadi salah sasaran, sehingga pesanan tetap akan "terlambat" tanpa perbaikan kepuasan pelanggan secara nyata.

---

# 2. Appendix Evidence Data

**(1) Grafik Baseline**  
*(Visualisasi Tren Tingkat Ketepatan Waktu dan Rata-rata Ulasan - berdasarkan data historis Olist)*
> Terdapat pola "spike" keterlambatan di pertengahan hingga akhir kuartal pertama 2018 (Februari-Maret), di mana rata-rata *On-Time Delivery Rate* sempat turun menyentuh kisaran ~80% (sejumlah 20% pesanan terlambat). Tepat pada periode tersebut, skor ulasan (Review Score) keseluruhan platform merosot drastis mencapai titik kuartalan terendahnya, menciptakan baseline kolerasi negatif langsung antara keterlambatan dengan kepuasan berbelanja.

**(2) Dua Tabel Komparatif**

*Tabel 2.1: Distribusi Ulasan Kepuasan Pelanggan terhadap Status Pengiriman*

| Timeliness Status (Ketepatan)  | Persentase Total Order | Rata-Rata Review Score (1-5)| Proporsi Ulasan Bintang 1 |
|--------------------------------|------------------------|-----------------------------|---------------------------|
| **Tepat Waktu (On-Time)**      | ~91.8%                 | 4.29                        | ~6.5%                     |
| **Terlambat (Late)**           | ~8.2%                  | 2.56                        | **~45.1%**                |

*> Insight Tabel 2.1:* Terdapat gap skor ulasan yang lebar. Ketika paket datang terlambat, hampir 45.1% pelanggan tanpa kompromi langsung memberikan skor rating terburuk (1 Bintang).

*Tabel 2.2: Perbandingan Rata-rata Durasi Keterlambatan Pengiriman (Delivery Duration) vs Skor Ulasan*

| Delivery Duration Status              | Rata-rata Waktu Tiba Aktual | Rata-Rata Review Score |
|---------------------------------------|-----------------------------|------------------------|
| Tiba Lebih Cepat dari Estimasi        | < Tanggal Estimasi          | 4.29                   |
| Terlambat Ringan (1 - 7 Hari)         | Estimasi + 7 Hari           | 3.06                   |
| Terlambat Parah (> 7 Hari)            | Estimasi > 7 Hari           | 1.69                   |

*> Insight Tabel 2.2:* Semakin lama durasi keterlambatan aktual menyimpang dari ekspektasi (*duration difference*), tingkat kepuasan pelanggan semakin jatuh mendekati rating sempurna 1 Bintang.

**(3) Interpretasi Paragraf Terhadap Bukti Substansial**

Bukti paling substansial yang mendasari pemilihan **Framing 1 (Keterlambatan Pengiriman/Delivery Delay)** adalah temuan komparatif paradoksikal pada korelasi tren grafikalnya dan distribusinya. Meskipun rasio keseluruhan pesanan terlambat ("Late") sebenarnya hanya mewakili proporsi terkecil dari transaksi platform (sekitar ~8%), kelompok ini bertanggung jawab pada sentimen negatif yang murni berujung merusak pengalaman berbelanja di mana rata-rata skor jatuh secara sistematis pada angka **2.56**, memicu nyaris **45.1%** ulasan ekstrem negatif (1 Bintang). Keterlambatan parah (>7 Hari) terbukti menjadi faktor pemicu dominan (*dealbreaker*) yang secara radikal menurunkan _rating_ keseluruhan hingga **1.69** (dengan 67.7% pelanggan membanting rating 1 bintang). Isu kronis distribusi ini secara efektif menetralisasi efek positif apa pun dari produk seller yang berkualitas maupun murahnya biaya pengiriman. Menyelesaikan _delivery duration_ akan mengeliminasi sumber *churn* terbesar pembeli perusahaan.
