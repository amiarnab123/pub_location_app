import pandas as pd
import numpy as np
import streamlit as st

def app():
    df = pd.read_csv("C:/Users/ARNAB MANNA/Desktop/open_pubs.csv")
    df = df.dropna()
    df.columns = ['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
    st.title('Welcome to the Pub Location Application')
    ### Displaying the dataset
    st.subheader('Dataset')
    if st.button('Head'):
        st.write(df.head())
    if st.button('Tail') :
        st.write(df.tail())
    ### About the data
    st.subheader('About the data')
    option = st.selectbox(
    'select the function',
    ('shape', 'columns','describe','missing values'))
    if option == 'shape' :
        st.write(df.shape)
    if option == 'columns' :
        st.write(df.columns)
    if option == 'describe' :
        st.write(df.describe())
    if option == 'missing values' :
        st.write(df.isnull().sum())

