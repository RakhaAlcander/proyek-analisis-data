#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets from local paths
@st.cache_data
def load_data():
    day_df = pd.read_csv("dashboard/clean_data.csv")
    hour_df = pd.read_csv("dashboard/clean_data1.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Judul aplikasi
st.title('Analisis Data Penyewaan Sepeda')
st.markdown("""
    <div class="justified-text">
    Analisis ini memiliki tujuan untuk menjawab beberapa pertanyaan bisnis terkait peminjaman sepeda:
    <ol>
    <li>Bagaimana hubungan antara peminjaman, cuaca, dan holiday/weekday?</li>
    <li>Pada cuaca apa yang menyebabkan peminjaman sepeda menurun?</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# Menampilkan data pertama
st.subheader("Data sepeda bersih (day_df) preview:")
st.write(day_df)

# Menampilkan data kedua
st.subheader("Data sepeda bersih (hour_df) preview:")
st.write(hour_df)

############################# DAYYYYY ##################################

# Membuat plot rata rata peminjaman dengan status hari
st.subheader("Average Bike Rentals: Holidays vs Non-Holidays(weekdays and working day):")
avg_rentals = day_df.groupby('holiday')['cnt'].mean()
plt.figure(figsize=(8, 6))
avg_rentals.plot(kind='bar', edgecolor= 'black', color='green')
plt.xlabel('Holiday (0=No, 1=Yes)')
plt.ylabel('Avg Rentals')
plt.xticks(rotation=0)
st.pyplot(plt)

st.subheader("Insights:")
st.write("""Rata-rata peminjaman sepeda berdasarkan status hari menunjukkan bahwa terdapat 4527.104225 peminjaman per hari pada hari biasa (weekdays and workingdays) dan 3735 peminjaman per hari pada hari libur.
""")

# Membuat plot rata rata peminjaman dengan kondisi cuaca
st.subheader("Average Bike Rentals: by weather condition:")
avg_rentals_weather = day_df.groupby('weathersit')['cnt'].mean()
avg_rentals_weather.plot(kind='bar', color='green', edgecolor='black')
plt.xlabel('Weather Conditions')
plt.ylabel('Avg Rentals')
plt.xticks(rotation=0)
st.pyplot(plt)

st.subheader("Insights:")
st.write("""Rata-rata peminjaman sepeda berdasarkan kondisi cuaca menunjukkan bahwa terdapat 4876.786177 peminjaman saat cuaca cerah (1), 4035.862348 peminjaman saat cuaca berkabut dan mendung (2), 1803.285714 peminjaman saat hujan ringan dan salju (3)
""")

# Korelasi matriks
st.subheader("Correlation between 4 features (cnt, weathersit, holiday, weekday (day)):")
# Menghitung korelasi antar kolom yang relevan
correlation_matrix = day_df[['cnt', 'weathersit', 'holiday', 'weekday']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='RdPu', linewidths=0.5)
st.pyplot(plt)

st.subheader("Insights:")
st.write("""
Hubungan antara "cnt" dengan variabel lainnya:
- "weathersit": Korelasi negatif (-0.3) menunjukkan bahwa ketika cuaca memburuk (nilai "weathersit" lebih tinggi), jumlah sepeda sewaan cenderung berkurang.
- "holiday": Korelasi negatif (-0.068) menunjukkan sedikit kecenderungan penurunan jumlah sepeda sewaan pada hari libur.
- "weekday": Korelasi positif (0.067) menunjukkan sedikit kecenderungan peningkatan jumlah sepeda sewaan pada hari hari tertentu dalam seminggu.

Hubungan antara "weathersit" dengan variabel lainnya:
- "holiday": Korelasi negatif (-0.035) menunjukkan sedikit kecenderungan penurunan jumlah sepeda sewaan pada hari libur ketika cuaca memburuk.
- "weekday": Korelasi positif (0.031) menunjukkan sedikit kecenderungan peningkatan jumlah sepeda sewaan pada hari hari tertentu dalam seminggu ketika cuaca memburuk.

Hubungan antara "holiday" dengan "weekday":
- Korelasi negatif (-0.1) menunjukkan sedikit kecenderungan penurunan jumlah sepeda sewaan pada hari hari tertentu dalam seminggu yang juga merupakan hari libur.
""")


##################### HOURR #####################

# Plot pertama (misalnya, rata-rata peminjaman berdasarkan hari libur)
st.subheader("Average Bike Rentals: Holidays vs Non-Holidays (Weekdays and Working Days):")
avgs_rentals = hour_df.groupby('holiday')['cnt'].mean()

# Membuat figure untuk mengatur ukuran plot
plt.figure(figsize=(8, 6))

# Plot batang dengan warna dan edge
avgs_rentals.plot(kind='bar', edgecolor='black', color='green')
plt.xlabel('Holiday (0=No, 1=Yes)')
plt.ylabel('Avg Rentals')
plt.xticks(rotation=0)

# Tampilkan plot di Streamlit
st.pyplot(plt.gcf())  # gcf = Get Current Figure

# Menambahkan insight di bawah plot
st.subheader("Insights:")
st.write("""
Rata-rata peminjaman sepeda berdasarkan status hari menunjukkan bahwa terdapat 
173.257450 peminjaman per jam pada hari biasa (weekdays and workingdays) dan 154.712851 
peminjaman per hari pada hari libur.
""")

# Plot kedua: rata-rata peminjaman berdasarkan kondisi cuaca
st.subheader("Average Bike Rentals: by Weather Condition:")
avgs_rentals_weather = hour_df.groupby('weathersit')['cnt'].mean()

# Membuat figure baru untuk plot kedua
plt.figure(figsize=(8, 6))

# Plot batang untuk kondisi cuaca
avgs_rentals_weather.plot(kind='bar', edgecolor='black', color='green')
plt.xlabel('Weather Conditions')
plt.ylabel('Avg Rentals')
plt.xticks(rotation=0)

# Tampilkan plot di Streamlit
st.pyplot(plt.gcf())

# Menambahkan insight di bawah plot
st.subheader("Insights:")
st.write("""
Rata-rata peminjaman sepeda berdasarkan kondisi cuaca menunjukkan bahwa terdapat 
185.314247 peminjaman saat cuaca cerah (1), 162.626463 peminjaman saat cuaca berkabut dan mendung (2), 
106.050462 peminjaman saat hujan ringan dan salju (3), serta 74.333333 peminjaman saat hujan berat dan badai (4).
""")

# Korelasi matriks
st.subheader("Correlation between 4 features (cnt, weathersit, holiday, weekday (hour)):")
# Menghitung korelasi antar kolom yang relevan
correlation_matrix = hour_df[['cnt', 'weathersit', 'holiday', 'weekday']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='RdPu', linewidths=0.5)
st.pyplot(plt)


st.subheader("Insights:")
st.write("""
Korelasi Negatif antara cnt dan weathersit:
- Korelasi negatif (-0.14) menunjukkan bahwa ketika kondisi cuaca memburuk (nilai weathersit lebih tinggi), jumlah sepeda yang disewa cenderung menurun. Ini menunjukkan bahwa orang cenderung kurang menyewa sepeda pada hari hujan atau bersalju.

Korelasi Lemah antara cnt dengan holiday/weekday:
- Korelasi antara cnt dan holiday (-0.02) serta cnt dan weekday (0.023) keduanya sangat lemah. Ini menunjukkan bahwa apakah hari tersebut adalah hari libur atau hari dalam seminggu memiliki dampak minimal terhadap jumlah sepeda yang disewa.
""")


# kesimpulan
st.subheader("CONCLUSION:")
st.write("""
Conclution pertanyaan 1
Pengaruh Cuaca (weathersit)
- Pengaruh Dominan: Cuaca memiliki pengaruh paling signifikan terhadap jumlah sepeda yang disewa. Korelasi negatif yang kuat antara cnt dan weathersit menunjukkan bahwa semakin buruk kondisi cuaca, semakin sedikit orang yang menyewa sepeda.

Pengaruh Hari Libur (holiday) dan Hari dalam Seminggu (weekday)
- Pengaruh Lemah: Baik hari libur maupun hari dalam seminggu memiliki pengaruh yang sangat kecil terhadap jumlah sepeda yang disewa. Korelasi yang mendekati nol menunjukkan bahwa faktor-faktor ini tidak memberikan kontribusi signifikan dalam menjelaskan variasi jumlah penyewaan sepeda.
- Potensi Faktor Lain: Kemungkinan ada faktor lain yang lebih kuat mempengaruhi jumlah penyewaan sepeda pada hari libur atau hari kerja tertentu, seperti acara khusus, musim, atau tren jangka panjang.

Interaksi antara Variabel
- Interaksi yang lemah antara cuaca, hari libur, dan hari dalam seminggu. Ini berarti, pengaruh cuaca terhadap jumlah penyewaan sepeda tidak terlalu dipengaruhi oleh apakah hari tersebut adalah hari libur atau hari kerja.

         
Conclution pertanyaan 2
Secara umum, cuaca buruk merupakan faktor utama yang menyebabkan penurunan peminjaman sepeda. Kondisi cuaca yang ekstrim seperti hujan lebat, salju, atau badai (Kondisi Cuaca 3 dan 4) sangat mengurangi minat masyarakat untuk menggunakan sepeda. Hal ini disebabkan oleh beberapa faktor, antara lain:

- Keamanan: Jalanan yang licin atau banjir meningkatkan risiko kecelakaan.
- Kenyamanan: Cuaca buruk seperti hujan dan angin membuat bersepeda menjadi tidak nyaman.
- Visibilitas: Cuaca berkabut atau hujan deras dapat mengurangi visibilitas, sehingga bersepeda menjadi lebih berbahaya.
Selain cuaca ekstrim, cuaca yang kurang mendukung seperti berkabut atau berawan (Kondisi Cuaca 2) juga dapat mengurangi jumlah peminjaman sepeda. Hal ini mungkin disebabkan oleh faktor-faktor seperti visibilitas yang terbatas atau ketidaknyamanan cuaca. Sebaliknya, cuaca yang cerah atau sedikit berawan (Kondisi Cuaca 1) sangat mendukung aktivitas bersepeda. Cuaca yang baik mendorong masyarakat untuk lebih aktif menggunakan sepeda untuk transportasi atau rekreasi. Perlu mempertimbangkan faktor lain seperti adanya acara/event khusus di suatu area dapat meningkatkan atau menurunkan jumlah peminjaman sepeda.
""")


# In[ ]:




