import os
import streamlit as st
import pydeck as pdk
import laspy
import numpy as np
import plotly.express as px
import pyvista as pv
import pandas as pd

from base64 import b64encode
import geopandas as gpd
import folium
import pandas as pd
from folium.plugins import HeatMap, MeasureControl
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from io import BytesIO

from PIL import Image

# Page layout
st.set_page_config(page_title="Ketut Tomy Suhari", page_icon="🏯", layout="wide")

 if st.button("Kembali", key="back_button"):
        st.balloons()  # Efek tambahan saat tombol diklik
        st.write("Anda telah kembali!")
        # Redirect ke halaman web saat tombol diklik
        st.markdown("[Buka halaman](https://ketuttomysuhari.github.io/)")

# Header
st.header("Om Swastyastu")
st.subheader("Selamat Datang di Halaman Lab Project")

col1, col2 = st.columns(2)
with col1:
    # Introduction Section
    st.image("./img/tomy.png", width=400, use_column_width=False)
with col2:
    st.title("Head of Photogrammetry Lab, Institut Teknologi Nasional Malang")
    st.info("Lecturer from Geodesy Engineering Institut Teknologi Nasional Malang ")

    st.markdown("### About Me")
    st.write(
        "**Name:** Dr (Cand). Ir. Ketut Tomy Suhari, S.T., M.T., IPP.;\n"
        "**Profession:** Cadastral Surveyor and Lecturer;\n"
        "**Nationality:** Indonesia;\n"
        "**Location:** Bali, Indonesia;\n"
        "**Telp:** (+62) 812-3682-8055;\n"
        "**Email:** ksuhari@lecturer.itn.ac.id")
    
    st.write("""
    Throughout my academic journey, my passion for research in cultural heritage and large-scale mapping has remained a constant source of inspiration and fascination...
    """)

st.markdown("### My Lab Activity")

# Projects Section

st.markdown("### Projects")

col1a, col2a = st.columns(2)
with col1a:
    st.write("Tanggal pembuatan adalah 17 Desember 2023")
    st.info("Informasi lebih lanjut silakan klik page ⛵ Rohingnya ")
with col2a:
    st.image("./img/rohingya-model.png", use_column_width=True)
    

# Contact Section

st.markdown("### Contact Me")
st.write("Feel free to reach out to me using the contact information below:")
st.info(
    "**Address:** 1st Floor, Department of Geodesy Engineering, Faculty of Civil Engineering and Planning, Institut Teknologi Nasional Malang, Indonesia\n"
    "**Email:** ksuhari@lecturer.itn.ac.id\n"
    "**Phone:** +62-812-3682-8055"
)

