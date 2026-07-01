import streamlit as st

st.set_page_config(
    page_title="Town Moor Survey App",
    page_icon="📍",
    layout="centered"
)

st.title("📍 Town Moor Survey App")

st.write(
    """
Welcome to the Town Moor Survey App.

This application has been developed to help staff and students locate,
navigate to and recover survey control points on the Town Moor.
"""
)

st.divider()

point = st.text_input(
    "Enter Point ID",
    placeholder="Example: TM NEW 1"
)

if st.button("Find Point"):

    if point == "":
        st.warning("Please enter a Point ID.")

    else:
        st.success(f"You searched for: {point}")
