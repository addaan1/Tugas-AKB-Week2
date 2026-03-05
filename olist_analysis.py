import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_olist():
    # Load data (Pastikan file CSV Olist dari Kaggle sudah diekstrak di folder ini)
    try:
        orders = pd.read_csv('olist_orders_dataset.csv')
        items = pd.read_csv('olist_order_items_dataset.csv')
        payments = pd.read_csv('olist_order_payments_dataset.csv')
        reviews = pd.read_csv('olist_order_reviews_dataset.csv')
    except FileNotFoundError:
        print("Dataset Olist tidak ditemukan. Pastikan file CSV Olist berada di folder yang sama dengan script ini.")
        return

    print("Data berhasil dimuat. Mulai melakukan analisis...\n")

    # 1. Merge dataset untuk membuat data pada Level-Order
    # Agregasi data items, payments, dan reviews per order_id
    order_items = items.groupby('order_id').agg({'price': 'sum', 'freight_value': 'sum'}).reset_index()
    order_payments = payments.groupby('order_id').agg({'payment_value': 'sum'}).reset_index()
    order_reviews = reviews.groupby('order_id').agg({'review_score': 'mean'}).reset_index() # Rata-rata review per order

    # Proses join (menggabungkan tabel-tabel relevan)
    df = orders.merge(order_items, on='order_id', how='left')
    df = df.merge(order_payments, on='order_id', how='left')
    df = df.merge(order_reviews, on='order_id', how='left')

    # Konversi string kolom tanggal menjadi format Datetime
    date_cols = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Hapus pesanan yang belum/tidak memiliki tanggal diterima pelanggan
    df = df.dropna(subset=['order_delivered_customer_date'])

    # 2. Membuat 2 Variabel Turunan Sesuai Persyaratan (Framing 1)
    # Variabel 1: Delivery Duration (Durasi Pengiriman dalam jumlah hari)
    df['delivery_duration'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

    # Variabel 2: Timeliness Status (Ketepatan Waktu: On-Time vs Late)
    df['timeliness_status'] = np.where(df['order_delivered_customer_date'] > df['order_estimated_delivery_date'], 'Late', 'On-Time')

    # 3. Analisis Eksploratif Pembenaran Pemilihan Frame
    print("=== TINGKAT KETEPATAN PENGIRIMAN ===")
    status_counts = df['timeliness_status'].value_counts(normalize=True) * 100
    print(status_counts.round(2).astype(str) + '%')

    print("\n=== RATA-RATA SKOR ULASAN BERDASARKAN KETEPATAN ===")
    avg_score = df.groupby('timeliness_status')['review_score'].mean()
    print(avg_score.round(2))

    print("\n=== PROPORSI ULASAN 1 BINTANG (SANGAT BURUK) BERDASARKAN KETEPATAN ===")
    # Identifikasi ulasan dengan Bintang 1
    df['is_1_star'] = (df['review_score'] <= 1.0)
    bintang1_prop = (df.groupby('timeliness_status')['is_1_star'].mean() * 100)
    print(bintang1_prop.round(2).astype(str) + '%')

    # Visualisasi Baseline: Tren Ketepatan Waktu (Late Delivery Rate per Bulan)
    df['purchase_month'] = df['order_purchase_timestamp'].dt.to_period('M')
    # Hitung rata-rata keterlambatan per bulan
    trend = df.groupby('purchase_month')['timeliness_status'].apply(lambda x: (x == 'Late').mean() * 100)
    
    plt.figure(figsize=(10, 5))
    trend.plot(kind='bar', color='coral', edgecolor='black')
    plt.title('Tingkat Keterlambatan Pengiriman (Late Delivery Rate %) - Olist')
    plt.xlabel('Bulan Pemesanan')
    plt.ylabel('Persentase Terlambat (%)')
    plt.tight_layout()
    plt.savefig('baseline_trend.png')
    print("\n[+] Berhasil menyimpan visualisasi baseline grafik dengan nama 'baseline_trend.png'")

if __name__ == "__main__":
    analyze_olist()
