import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_baseline_chart():
    print("Memproses dataset, mohon tunggu beberapa saat...")
    try:
        # Load dataset
        orders = pd.read_csv('olist_orders_dataset.csv')
        reviews = pd.read_csv('olist_order_reviews_dataset.csv')
        
        # Merge dataset
        df = orders.merge(reviews.groupby('order_id').agg({'review_score': 'mean'}).reset_index(), 
                          on='order_id', how='left')
        
        print("Data berhasil dimuat. Mengonversi tipe waktu...")
        
        # Konversi ke Datetime
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')
        df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], errors='coerce')
        df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'], errors='coerce')
        
        # Buang transaksi tanpa tanggal terima
        df = df.dropna(subset=['order_delivered_customer_date'])
        
        # Tentukan status Keterlambatan
        df['timeliness_status'] = np.where(df['order_delivered_customer_date'] > df['order_estimated_delivery_date'], 'Barang Terlambat', 'Tepat Waktu')
        
        # Ekstrak Tahun-Bulan (YYYY-MM) untuk sumbu X
        df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
        
        # Filter ke rentang tahun 2017 - 2018 (membuang bulan sepi)
        df_filtered = df[(df['order_purchase_timestamp'] >= '2017-01-01') & (df['order_purchase_timestamp'] < '2018-09-01')].copy()
        
        # Hitung Persentase Keterlambatan dan Rata-rata Skor
        monthly_stats = df_filtered.groupby('purchase_month').agg(
            late_rate=('timeliness_status', lambda x: (x == 'Barang Terlambat').mean() * 100),
            avg_review=('review_score', 'mean')
        ).reset_index()
        
        # === MEMBUAT VISUALISASI ===
        print("Membangun grafik...")
        sns.set_theme(style="whitegrid")
        fig, ax1 = plt.subplots(figsize=(14, 7))

        # Bar chart untuk Persentase Pesanan Terlambat
        ax1.bar(monthly_stats['purchase_month'], monthly_stats['late_rate'], color='salmon', alpha=0.7, label='Terlambat (%)')
        ax1.set_xlabel('Bulan Pemesanan', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Rasio Pesanan Terlambat (%)', color='salmon', fontsize=12, fontweight='bold')
        ax1.tick_params(axis='y', labelcolor='salmon')
        ax1.set_xticklabels(monthly_stats['purchase_month'], rotation=45, ha='right')

        # Line chart untuk Rata-rata Ulasan (Review Score 1-5)
        ax2 = ax1.twinx()  
        ax2.plot(monthly_stats['purchase_month'], monthly_stats['avg_review'], color='darkblue', marker='o', linewidth=2.5, markersize=8, label='Rata-Rata Kepuasan')
        ax2.set_ylabel('Skor Rata-Rata Ulasan (1-5)', color='darkblue', fontsize=12, fontweight='bold')
        ax2.tick_params(axis='y', labelcolor='darkblue')

        # Tambahkan judul dan Legend
        plt.title('Baseline: Tren Korelasi Tingkat Keterlambatan Pengiriman vs Skor Ulasan', fontsize=15, fontweight='bold', pad=20)
        fig.legend(loc='upper right', bbox_to_anchor=(0.90, 0.85), fontsize=11, frameon=True)
        
        # Modifikasi minor grid agar rapi
        ax1.grid(axis='y', linestyle='--', alpha=0.5)
        ax2.grid(False) # Hanya gunakan satu set garis kisi
        
        # Simpan grafik
        filename = 'Visualisasi_Tren_Baseline.png'
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\n[SUKSES] Grafik telah berhasil dibuat dan disimpan sebagai file gambar: '{filename}'")

    except Exception as e:
         print(f"Terjadi kesalahan: {e}\\nPastikan dataset .csv berada di dalam folder ini.")

if __name__ == "__main__":
    generate_baseline_chart()
