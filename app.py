import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
vehicle_df = pd.read_csv('../vehicles_us.csv')
st.header('Used Car Market')
types = vehicle_df['type'].unique()
st.write('Select Vehicle Type')
selected_types = []
for vehicle in types:
    if st.checkbox(vehicle):
        selected_types.append(vehicle)
if selected_types:
    filtered_df = vehicle_df[vehicle_df['type'].isin(selected_types)]
else:
    filtered_df = vehicle_df
pr_od_typ = px.scatter(filtered_df, x= 'price', y= 'odometer', color= 'type', title= 'Price vs Mileage by Vehicle Types')
st.write(pr_od_typ)

st.write(px.scatter(vehicle_df, x='price', y= 'days_listed', color = 'condition', title= 'Price vs Days Listed by Condition', labels= {'price':'Car Price', 'days_listed':'Days Listed'}))

st.write(px.histogram(vehicle_df, x= 'price', title= 'Distribution of Prices'))

st.write(px.histogram(vehicle_df, x= 'paint_color', title= 'Distribution of Paint Colors', labels= {'paint_color':'Paint Color'}))
