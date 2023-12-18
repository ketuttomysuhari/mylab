from base64 import b64encode
import geopandas as gpd
import folium
import pandas as pd
from folium.plugins import HeatMap, MeasureControl
import streamlit as st
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

from PIL import Image



# Contoh data sebaran penduduk di daerah Rohingya
population_data = [
    {'nama_tempat': 'Indonesia', 'latitude': 5.1956842, 'longitude': 97.1020099, 'population': 1684000},
    {'nama_tempat': 'Bangladesh', 'latitude': 21.4291642, 'longitude': 91.9599342, 'population':800000},
    {'nama_tempat': 'Saudi Arabia', 'latitude': 25.9643539, 'longitude': 43.3780246, 'population': 470000},
    {'nama_tempat': 'Pakistan', 'latitude': 24.8818273, 'longitude': 66.9936215, 'population': 500000},
    {'nama_tempat': 'Malaysia', 'latitude': 3.8387148, 'longitude': 102.8716889, 'population': 200000},
    {'nama_tempat': 'India', 'latitude': 13.0457, 'longitude': 76.1781744, 'population': 50000},
    {'nama_tempat': 'Uni Emirat Arab', 'latitude': 23.6169512, 'longitude': 52.3756706, 'population': 50000},
    {'nama_tempat': 'Australia', 'latitude': -33.6685268, 'longitude': 150.6901334, 'population': 5000},
    {'nama_tempat': 'Thailand', 'latitude': 6.8728212, 'longitude': 99.6896285, 'population': 5000},
    {'nama_tempat': 'Amerika Serikat', 'latitude': 40.6614132, 'longitude': -74.4908226, 'population': 5000},
    {'nama_tempat': 'Uni Eropa', 'latitude': 52.8436753, 'longitude': -9.3946297, 'population': 3000},
    {'nama_tempat': 'Yordania', 'latitude': 31.8314564, 'longitude': 34.7646919, 'population': 1300},
    {'nama_tempat': 'Kanada', 'latitude': 43.4548504, 'longitude': -80.9821836, 'population': 1100},
    {'nama_tempat': 'Jepang', 'latitude': 33.53083, 'longitude': 128.565298, 'population': 560},
    {'nama_tempat': 'Sri Lanka', 'latitude': 21.4291642, 'longitude': 91.9599342, 'population': 650},
    {'nama_tempat': 'Nepal', 'latitude': 27.7482213, 'longitude': 85.3476739, 'population': 800},
    {'nama_tempat': 'Myanmar', 'latitude': 19.3511393, 'longitude': 88.7750701, 'population': 600000},
    # Tambahkan data sebaran penduduk lainnya sesuai kebutuhan
]

# Tampilkan peta dengan Folium
m = folium.Map(location=[population_data[0]['latitude'], population_data[0]['longitude']], zoom_start=2.5, control_scale=True)

# Tambahkan overlay gambar
folium.raster_layers.ImageOverlay(
    image="https://upload.wikimedia.org/wikipedia/commons/f/f4/Mercator_projection_SW.jpg",
    name="I am a jpeg",
    bounds=[[-82, -180], [82, 180]],
    opacity=1,
    interactive=False,
    cross_origin=False,
    zindex=1,
    alt="Wikipedia File:Mercator projection SW.jpg",
    attr="Overlay Image Attribution: Wikipedia File:Mercator projection SW.jpg",
).add_to(m)

# Tambahkan HeatMap berdasarkan data sebaran penduduk
heat_data = [(point['latitude'], point['longitude'], point['population']) for point in population_data]
HeatMap(heat_data, radius=15).add_to(m)

# Tambahkan legenda jumlah penduduk
legend_html = """
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; width: 100px; height: 90px; 
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white;
     ">
     &nbsp; Jumlah Penduduk <br>
     &nbsp; < 1000 &nbsp; <i style="background: #FF0000"></i><br>
     &nbsp; 1000-2000 &nbsp; <i style="background: #FFA500"></i><br>
     </div>
     """
m.get_root().html.add_child(folium.Element(legend_html))

# Tambahkan skala menggunakan MeasureControl
m.add_child(MeasureControl(primary_length_unit='kilometers'))

# Tambahkan popup koordinat
m.add_child(folium.LatLngPopup())


# Tampilkan tabel informasi
df = pd.DataFrame(population_data)
# Tambahkan kolom total populasi
df['total_populasi'] = df['population'].sum()

# Temukan negara dengan jumlah terbanyak dan terendah
negara_terbanyak = df.loc[df['population'].idxmax()]['nama_tempat']
negara_terendah = df.loc[df['population'].idxmin()]['nama_tempat']

st.title("Model Invasi Bangsa Rohingya")

# Streamlit App
title_html = """
    <div style="font-size: 2em; font-weight: bold;"></div>
    <div style="font-size: 1.2em; margin-bottom: 0px; margin-top: -20px;">Ketut Tomy Suhari<sup>1</sup><sup>,</sup><sup>2</sup></div>
    <div style="font-size: 1em; margin-bottom: 0px;"><sup>1</sup>Program Studi Teknik Geodesi dan Geomatika, FITB, Institut Teknologi Bandung</div>
    <div style="font-size: 1em; margin-bottom: 20px;"><sup>1</sup>Program Studi Teknik Geodesi, FTSP, Institut Teknologi Nasional Malang</div>
"""

st.markdown(title_html, unsafe_allow_html=True)

# Tampilkan peta Folium di Streamlit
folium_static(m, width=700, height=600)

st.subheader("Pendahuluan")

st.write("Konflik di sekitar bangsa Rohingya telah menyebabkan sebaran populasi yang kompleks di berbagai negara. Pemahaman mendalam tentang distribusi ini penting untuk merumuskan kebijakan dan menangani dampak kemanusiaan. Dalam konteks ini, kami menyajikan model visualisasi yang menyajikan data sebaran penduduk Rohingya di beberapa negara. Sebaran penduduk Rohingya di berbagai negara dapat bervariasi dan bisa tergantung pada waktu dan sumber data. Oleh karena itu, visualisasi ini tidak dimaksudkan sebagai representasi yang akurat, tetapi sebagai contoh demonstratif untuk tujuan ilustratif. Visualisasi ini dibangun untuk memberikan gambaran umum tentang sebaran populasi Rohingya dengan menggunakan teknologi pemrograman Python dan pustaka-pustaka terkait. Data yang digunakan dalam model ini diperoleh sebagai asumsi berdasarkan informasi yang terdapat di [Wikipedia](https://en.wikipedia.org/wiki/Rohingya_people).")
# Tambahkan path gambar flowchart
rohingya = "./data/rohingya.jpeg"
# Tampilkan flowchart
st.image(rohingya, use_column_width=True)

st.subheader("Metodologi")
st.write("Visualisasi ini dibangun dengan menggunakan pustaka-pustaka seperti Folium, Geopandas, dan Streamlit di lingkungan bahasa pemrograman Python. Data sebaran penduduk Rohingya diberikan dalam bentuk tabel, yang kemudian diplot ke peta interaktif menggunakan Folium. Selain itu, kami menampilkan diagram batang, diagram pie, dan tabel informasi untuk memberikan wawasan yang holistik.")

st.subheader("Pembahasan")
st.write("Peta interaktif menyajikan distribusi penduduk Rohingya di berbagai negara. HeatMap menyoroti area dengan tingkat populasi yang lebih tinggi. Overlay gambar dan legenda memberikan konteks tambahan tentang visualisasi. Diagram batang memberikan pemahaman yang cepat tentang jumlah penduduk di setiap negara, sementara diagram pie mengilustrasikan persentase populasi relatif. Tabel informasi menyajikan data yang lebih terstruktur. Dalam bagian hasil, total populasi Rohingya di seluruh wilayah ditampilkan bersama dengan negara-negara yang memiliki jumlah penduduk terbanyak dan terendah. Diagram batang dan pie memberikan perspektif yang berbeda, memudahkan pemahaman distribusi populasi. Peta juga memvisualisasikan hubungan antar kota dengan menggunakan polyline. Ini membantu dalam memahami konektivitas geografis antara berbagai lokasi penduduk Rohingya. Pengguna dapat berinteraksi dengan peta, mengukur jarak, dan melihat popup dengan informasi koordinat.")

col1a, col2a = st.columns(2)
with col1a:
    # Tampilkan peta Folium di Streamlit
    folium_static(m, width=350, height=300)



with col2a:
    st.metric(label="Total Populasi Rohingya", value=df['total_populasi'].values[0])
    st.metric(label="Negara dengan Jumlah Terbanyak", value=negara_terbanyak)
    st.metric(label="Negara dengan Jumlah Terendah", value=negara_terendah)


# Kolom yang akan ditampilkan di tabel
table_columns = ['nama_tempat', 'latitude', 'longitude', 'population']
# Buat tabel dengan kolom yang telah ditentukan
df_sorted = df.sort_values(by='population')


col11, col12 = st.columns(2)

with col11:

    fig, ax = plt.subplots()
    bar_labels = df_sorted['nama_tempat']
    bar_values = df_sorted['population']

    bars = ax.bar(bar_labels, bar_values, color='blue')

    ax.set_ylabel('Populasi')
    ax.set_title('Populasi Rohingya di Berbagai Lokasi')
    ax.set_xticklabels(bar_labels, rotation=45, ha='right')

    # Tampilkan nilai di atas setiap batang
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{round(yval):,}', ha='center', va='bottom', fontsize=6, color='black')

    # Tampilkan diagram batang di Streamlit
    st.pyplot(fig)

# ...
with col12:
    # Urutkan DataFrame berdasarkan populasi dari kecil ke besar
    df_sorted = df.sort_values(by='population')

    # Hitung persentase populasi setiap negara
    df_sorted['population_percentage'] = df_sorted['population'] / df['total_populasi'] * 100

    # Tampilkan nilai persentase di sekitar diagram pie
    labels = [f"{point['nama_tempat']} - {point['population_percentage']:.2f}%" for index, point in df_sorted.iterrows()]

    # Atur ukuran gambar diagram pie
    fig, ax = plt.subplots()
    pie = ax.pie(df_sorted['population'], labels=None, autopct='%1.1f%%', startangle=90, counterclock=False, colors=plt.cm.Paired.colors)
    ax.set_title('Persentase Populasi Rohingya Berdasarkan Negara')

    # Tambahkan legenda
    ax.legend(pie[0], labels, bbox_to_anchor=(1, 0.5), loc="center left", fontsize=8, title="Negara")

    # Tampilkan diagram pie di Streamlit
    st.pyplot(fig, clear_figure=True)

# Tampilkan tabel informasi di Streamlit
st.write("### Tabel Informasi Persebaran Rohingya")
table = st.table(df[table_columns])



# Loop on every pair of cities to add the connection
for startIndex, startRow in df.iterrows():
    for endIndex in range(startIndex, len(df.index)):
        endRow = df.iloc[endIndex]
        folium.PolyLine([(startRow['latitude'], startRow['longitude']), (endRow['latitude'], endRow['longitude'])], color='#69b3a2', weight=1).add_to(m)

# Add city names
for i, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['nama_tempat']).add_to(m)

# Tampilkan peta Folium di Streamlit
folium_static(m, width=800, height=600)

st.subheader("Kesimpulan")
st.write("Model visualisasi ini memberikan pandangan yang mendalam tentang distribusi populasi Rohingya di berbagai negara. Pemaparan data melalui peta interaktif, diagram, dan tabel memberikan kejelasan yang dibutuhkan untuk merancang kebijakan dan menangani dampak kemanusiaan. Dengan menggunakan teknologi terkini, informasi ini disajikan secara nyaman dan dapat diakses, memberikan kontribusi pada pemahaman yang lebih baik tentang kompleksitas situasi ini.")
