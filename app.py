import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Town Moor Survey App",
    page_icon="📍",
    layout="centered"
)

@st.cache_data
def load_points():
    df = pd.read_csv("Town_Moor_Coordinates.csv", header=1)

    df.columns = [
        "Point ID",
        "Lat_DD",
        "Lat_MM",
        "Lat_SS",
        "Lon_DD",
        "Lon_MM",
        "Lon_SS",
        "Height"
    ]

    df["Point ID"] = df["Point ID"].astype(str).str.strip().str.upper()

    df["Latitude"] = df["Lat_DD"] + df["Lat_MM"] / 60 + df["Lat_SS"] / 3600

    df["Longitude"] = -(
        abs(df["Lon_DD"]) + df["Lon_MM"] / 60 + df["Lon_SS"] / 3600
    )

    return df

df = load_points()

st.title("📍 Town Moor Survey App")

st.write("Select a survey control point to view its location.")

point_id = st.selectbox(
    "Choose Point ID",
    sorted(df["Point ID"].tolist())
)

if st.button("Find Point"):

    result = df[df["Point ID"] == point_id]
    p = result.iloc[0]

    st.success(f"Point found: {p['Point ID']}")

    st.write(f"**Latitude:** {p['Latitude']:.8f}")
    st.write(f"**Longitude:** {p['Longitude']:.8f}")
    st.write(f"**Ellipsoidal height:** {p['Height']:.3f} m")

    maps_url = f"https://www.google.com/maps?q={p['Latitude']},{p['Longitude']}"
    st.link_button("📍 Open in Google Maps", maps_url)

    m = folium.Map(
        location=[p["Latitude"], p["Longitude"]],
        zoom_start=20,
        tiles=None
    )

    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri World Imagery",
        name="Satellite"
    ).add_to(m)

    folium.CircleMarker(
        location=[p["Latitude"], p["Longitude"]],
        radius=8,
        color="red",
        fill=True,
        fill_color="yellow",
        fill_opacity=1,
        weight=3,
        tooltip=p["Point ID"]
    ).add_to(m)

    html(m._repr_html_(), height=500)
