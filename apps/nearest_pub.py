import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

def app():
    df = pd.read_csv("C:/Users/ARNAB MANNA/Desktop/open_pubs.csv")
    df = df.dropna()
    df.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude',
                  'local_authority']

    # Calculate the Euclidean distance between two points
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    # Function to calculate K closest points
    def kClosest(points, target, K):
        pts = []
        n = len(points)
        d = []

        for i in range(n):
            d.append({"first": distance(points[i][0], points[i][1], target[0], target[1]),"second": i})

        d = sorted(d, key=lambda l: l["first"])


        for i in range(K):
            pt = []
            pt.append(points[d[i]["second"]][0])
            pt.append(points[d[i]["second"]][1])
            pts.append(pt)


        # Calling DataFrame constructor on list
        df_nearest_loc = pd.DataFrame(pts, columns=['latitude', 'longitude'])
        st.header('**Lets find the nearest pub locations**')

        st.markdown('**Here are Nearest five Pubs based on user enter  Latitude and longitude**')
        st.map(df_nearest_loc)



    # Driver code
    df_lat_log = df[['latitude', 'longitude']]
    points = df_lat_log.values.tolist()

    lat = st.sidebar.slider('Your Latitude', 50.00000, 100.00000)
    log = st.sidebar.slider('Your Longitude', -3.000000, 3.000000)

    target = [lat, log]
    K = 5
    kClosest(points, target, K)
