import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Trolleybus Cost Model", layout="centered")

st.title("Operational Cost Modeling")
st.markdown("Interactive simulation of operational costs for Mexico City's Trolleybus Line 2 using vector calculus and spatial data.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/coordinates.csv")
    
    df['p'] = 0  
    df['h'] = 0  
    df.loc[df['Estación (Nodo i)'].str.contains('Velódromo', na=False), 'p'] = 1 
    df.loc[df['Estación (Nodo i)'].str.contains('Ciudad Deportiva|5 de Febrero', na=False), 'h'] = 1 
    
    df['lat'] = df['y (Latitud)']
    df['lon'] = df['x (Longitud)']
    
    return df

df = load_data()

st.sidebar.header("Model Parameters")
st.sidebar.markdown("Adjust the variables to run a sensitivity analysis on the operational cost.")

c0 = st.sidebar.slider("Base Cost (MXN/km)", min_value=10.0, max_value=30.0, value=17.73, step=0.1)
alpha = st.sidebar.slider("Topography Penalty (α)", min_value=0.0, max_value=1.0, value=0.20, step=0.05)
beta = st.sidebar.slider("Infrastructure Penalty (β)", min_value=0.0, max_value=0.1, value=0.005, step=0.001)

def calculate_haversine_distance(lon1, lat1, lon2, lat2):
    R = 6371.0 
    lon1_rad, lat1_rad = math.radians(lon1), math.radians(lat1)
    lon2_rad, lat2_rad = math.radians(lon2), math.radians(lat2)
    
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

total_route_cost = 0.0

for i in range(len(df) - 1):
    lon1, lat1 = df.loc[i, "lon"], df.loc[i, "lat"]
    lon2, lat2 = df.loc[i+1, "lon"], df.loc[i+1, "lat"]
    
    p_segment = df.loc[i, "p"]
    h_segment = df.loc[i, "h"]
    
    ds = calculate_haversine_distance(lon1, lat1, lon2, lat2)
    
    cost_density = c0 * (1 + (alpha * p_segment) + (beta * h_segment))
    subtotal = cost_density * ds
    
    total_route_cost += subtotal

st.metric(label="Estimated Total Cost per Trip (MXN)", value=f"${total_route_cost:.2f}")

st.markdown("### Route Map")
st.map(df)