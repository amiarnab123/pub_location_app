import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.write("Showing the Pub Locations")
    df = pd.read_csv("C:/Users/ARNAB MANNA/Desktop/open_pubs.csv")
    df = df.dropna()
    df.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude',
                  'local_authority']
    st.header("Locations of all the Pubs in UK:")
    st.caption("Search for all the pubs present at a specific location of UK")
    locs = st.radio("Through which you want to find Pub locations", ('Local Authority', 'Postal Code'))
    if locs == 'Local Authority':
        loc_authority = st.selectbox('Select a Local Authority', list(df['local_authority'].unique()))
        button_click = st.button('Search')
        if button_click == True:
            authority = df[df['local_authority'] == loc_authority]
            st.write("Number of Pubs under the selected Local Authority:", len(authority))
            locations = authority[['latitude', 'longitude']]
            st.map(locations)
    else:
        pst_code = st.selectbox('Select a Postal Code', list(df['postcode'].unique()))
        button_click = st.button('Search')
        if button_click == True:
            code = df[df['postcode'] == pst_code]
            st.write("Number of Pubs under the selected Postal Code:", len(code))
            locations = code[['latitude', 'longitude']]
            st.map(locations)