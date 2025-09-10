import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def run():

    # judul
    st.title("Prediksi Uber Drive Booking Cancel")

    # load gambar
    image_url = "https://ottocar.co.uk/wp-content/uploads/2025/06/shutterstock_1497227390-1024x678-QaE42RbG_2000-CZWqGpct_2000.jpeg.webp"
    st.image(image_url)
    st.caption("Sumber: google images")

    # tulisan 
    st.write("# Latar Belakang")

    st.write("""Dalam dataset, terdapat banyak kasus pembatalan baik oleh customer maupun driver, dengan alasan yang beragam (misalnya lokasi sulit dijangkau, waktu tunggu terlalu lama, perubahan rencana customer). Dengan memanfaatkan data historis booking, perusahaan bisa membangun model untuk memprediksi kemungkinan pembatalan.
Jika prediksi ini akurat, sistem dapat:
- Memberikan peringatan dini ke driver/customer.
- Menawarkan solusi preventif (misalnya armada alternatif, voucher diskon, atau prioritas driver).
- Mengurangi kerugian finansial sekaligus meningkatkan pengalaman pelanggan.

 """)
    
    st.write("# Dataset")
    st.write(''' 
            Data booking uber didapat dari [kaggle.com](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard/data)
''')
    data = pd.read_csv('src/dataset.csv')
    st.dataframe(data)

    # visualisasi
    st.write('# Exploratory Data Analysis')

    df_eda = data.copy()

    # tandai booking yang berstatus "No Driver Found"
    df_eda["is_no_driver_found"] = df_eda["Booking Status"].apply(
        lambda x: 1 if x == "No Driver Found" else 0
    )

    st.write('## Top 10 Pickup Location dengan Booking Status = No Driver Found Tertinggi')

    # cancel-rate khusus status "No Driver Found" per pickup
    pickup_ndf_rate = df_eda.groupby("Pickup Location")["is_no_driver_found"].mean()

    # ambil 10 pickup tertinggi
    top10_pickup_ndf = pickup_ndf_rate.sort_values(ascending=False).head(10)

    # --- Pickup ---
    fig = plt.figure(figsize=(10,6))
    top10_pickup_ndf.sort_values().plot(kind="barh", color="tomato")
    plt.xlabel("Proporsi No Driver Found")
    plt.title("Top 10 Pickup Location dengan Proporsi 'No Driver Found' Tertinggi")
    plt.show()
    st.pyplot(fig)

    # insight
    st.write('''
    Demikian hasil 10 lokasi teratas yang paling banyak mengalami "No Driver Found"
    dengan demikian, disarankan kepada Manajemen operasional Uber untuk menambah armada di 10 lokasi pickup tersebut karena disana kekurangan driver. 
''')
    
    # visualisasi plotly
    st.write('## Top 10 Pickup Locations dengan Cancel Rate Tertinggi')

    # tandai booking yang berstatus selain "Completed"
    df_eda["is_cancel"] = df_eda["Booking Status"].apply(
        lambda x: 1 if (x == 'Cancelled by Driver') or (x == 'Cancelled by Customer') else 0
    )

    pickup_cancel_rate = df_eda.groupby("Pickup Location")["is_cancel"].mean()
    top10_pickup = pickup_cancel_rate.sort_values(ascending=False).head(10)

    fig =  plt.figure(figsize=(10,6))
    top10_pickup.sort_values().plot(kind="barh", color="salmon")
    plt.xlabel("Cancel Rate")
    plt.title("Top 10 Pickup Locations dengan Cancel Rate Tertinggi")
    plt.show()
    st.pyplot(fig)

    st.write('''
             Demikian hasil 10 lokasi teratas yang paling banyak mengalami Booking Cancel dengan demikian, disarankan kepada Manajemen operasional Uber untuk menambah armada di 10 lokasi pickup tersebut karena disana kekurangan driver.
             ''')

    # form untuk menampilkan visualisasi pilihan
    st.write('## Persentase Pembatalan per Vehicle Type')
    
    cancel_rate = df_eda.groupby("Vehicle Type")["is_cancel"].mean().sort_values(ascending=False)

    fig = plt.figure(figsize=(8,5))
    sns.barplot(x=cancel_rate.index, y=cancel_rate.values, palette="viridis")

    # Tambahkan label persentase di atas bar
    for i, v in enumerate(cancel_rate.values):
        plt.text(i, v + 0.005, f"{v*100:.2f}%", ha="center", va="bottom", fontsize=9)

    plt.ylabel("Cancel Rate")
    plt.xlabel("Vehicle Type")
    plt.title("Persentase Pembatalan per Vehicle Type")
    plt.xticks(rotation=30)
    plt.ylim(0, cancel_rate.max() + 0.05)
    plt.show()

    st.pyplot(fig)
    
    st.write('''
    ***Rekomendasi Bisnis***

    - Fokus pada faktor lain

    Karena vehicle type bukan faktor signifikan, analisis perlu difokuskan ke variabel lain yang lebih berpengaruh terhadap cancel (misalnya: jam booking, pickup/drop location, waktu tunggu pengemudi, atau harga perjalanan).

    - Pantau konsistensi cancel rate

    Walaupun perbedaan kecil, Go Sedan terlihat sedikit lebih tinggi cancel rate-nya dibandingkan jenis lain. Perlu dipantau apakah ada faktor spesifik (misalnya jumlah driver Go Sedan lebih sedikit, waktu tunggu lebih lama, atau harga relatif lebih tinggi) yang memicu pembatalan.

    - Strategi mitigasi pembatalan

    Karena cancel rate relatif seragam, strategi untuk menurunkan cancel bisa dibuat global dan tidak perlu terlalu dibedakan per vehicle type. Misalnya:

        - Meningkatkan estimasi waktu kedatangan (ETA) yang lebih akurat
        - Memberikan insentif kepada driver untuk cepat menerima order
        - Menawarkan diskon kecil atau cashback untuk pelanggan agar tidak mudah cancel.
''')
    
    st.write('## Persentase Pembatalan per Vehicle Type')

    df_eda["is_not_completed"] = np.where(df_eda["Booking Status"] == "Completed", 0, 1)

    not_completed_rate = (
        df_eda.groupby("Vehicle Type")["is_not_completed"]
        .mean()
        .sort_values(ascending=False)
    )

    fig = plt.figure(figsize=(8, 5))
    sns.barplot(
        x=not_completed_rate.index,
        y=not_completed_rate.values,
        palette="viridis"
    )
    plt.title("Persentase Booking Tidak Selesai per Vehicle Type")
    plt.ylabel("Not Completed Rate")
    plt.xlabel("Vehicle Type")
    plt.xticks(rotation=30)
    plt.ylim(0, 1)
    plt.show()

    st.pyplot(fig)

    st.write('''
        1. Fokus Analisa ke Faktor Lain

        Karena Vehicle Type tidak berpengaruh signifikan, lebih baik alihkan fokus ke variabel lain yang mungkin lebih kuat hubungannya dengan pembatalan, seperti:
        - Waktu booking (jam sibuk vs non-sibuk)
        - Pickup location (akses sulit, kemacetan, supply driver rendah)

        2. Optimasi Supply dan Demand

        - Tingkat pembatalan seragam across vehicle types → kemungkinan besar dipengaruhi oleh ketersediaan driver atau mismatch supply-demand.
        - Lakukan monitoring real-time driver availability per area, bukan per tipe kendaraan.

        3. Komunikasi ke Pengguna

        - Karena tidak ada perbedaan berarti antar kendaraan, jangan batasi atau rekomendasikan kendaraan tertentu untuk mengurangi cancel.
        - Lebih efektif memberikan informasi estimasi waktu tunggu / ketersediaan agar pelanggan bisa membuat keputusan yang lebih realistis.
    ''')

    st.write('## Cancel Rate pada setiap Book Hour ')

    df_eda["Book_Hour"] = pd.to_datetime(df_eda["Time"], format="%H:%M:%S").dt.hour
    
    cancel_rate_by_hour = (
        df_eda.groupby("Book_Hour")["is_cancel"]
        .agg(["mean", "count"])
        .rename(columns={"mean": "Cancel_Rate", "count": "Total_Bookings"})
    )

    fig, ax1 = plt.subplots(figsize=(12,6))

    # Plot cancel rate (line chart)
    sns.lineplot(data=cancel_rate_by_hour, x=cancel_rate_by_hour.index, y="Cancel_Rate", marker="o", color="red", ax=ax1)
    ax1.set_ylabel("Cancel Rate", color="red")
    ax1.set_xlabel("Book Hour (0-23)")
    st.pyplot(fig)

    st.write('''
        1. Fokus pada Jam Sibuk (High Volume Hours)
            - Walaupun Cancel Rate seragam, dampak finansial terbesar ada di jam dengan volume tinggi (07:00 – 20:00).
            - Perlu strategi driver supply balancing di jam-jam tersebut untuk mengurangi jumlah absolut pembatalan.

        2. Driver Allocation & Incentives
            - Tambah insentif driver untuk shift sore – malam (17:00 – 20:00), ketika demand tinggi.
            - Perbanyak notifikasi untuk standby driver sebelum jam puncak.

        3. Customer Experience Monitoring
            - Karena cancelation tidak dipengaruhi jam tertentu, faktor lain (misalnya lokasi penjemputan, tipe kendaraan, atau jarak perjalanan) mungkin lebih dominan.
    ''')


if __name__ == "__main__":
    run()