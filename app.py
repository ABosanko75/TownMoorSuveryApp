import streamlit as st

st.set_page_config(
    page_title="Town Moor Survey App",
    page_icon="📍",
    layout="centered"
)

POINTS = {
    "TM NEW 1": {
        "lat": 54.98384177,
        "lon": -1.61922471,
        "height": 115.446,
    },
    "TM NEW 2": {
        "lat": 54.98383113,
        "lon": -1.61862891,
        "height": 114.772,
    },
}

st.title("📍 Town Moor Survey App")

point_id = st.text_input(
    "Enter Point ID",
    placeholder="Example: TM NEW 1"
).strip().upper()

if st.button("Find Point"):
    if point_id in POINTS:
        p = POINTS[point_id]

        st.success(f"Point found: {point_id}")

        st.write(f"**Latitude:** {p['lat']}")
        st.write(f"**Longitude:** {p['lon']}")
        st.write(f"**Ellipsoidal height:** {p['height']} m")

        maps_url = f"https://www.google.com/maps?q={p['lat']},{p['lon']}"
        st.link_button("📍 Open in Google Maps", maps_url)

    elif point_id == "":
        st.warning("Please enter a Point ID.")

    else:
        st.error("Point not found. Check the Point ID.")
