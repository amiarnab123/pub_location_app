import streamlit as st
from multiapp import MultiApp
from apps import Home, Pub_locations, nearest_pub # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home",Home.app)
app.add_app("Pub Locations",Pub_locations.app)
app.add_app("Nearest Pub Locations",nearest_pub.app)
# The main app
app.run()