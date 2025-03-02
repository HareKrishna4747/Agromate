import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# 🌍 Streamlit Config & Theme Toggle
st.set_page_config(page_title="🌦️ Weather & Pollution Dashboard", layout="wide")
if st.button("🏠 Go to Home"):
    st.switch_page("main.py")

# 🌎 Dashboard Title
st.title("🌎 Real-time Weather & Air Quality Dashboard")

# 📍 Location Selection
st.subheader("📍 Select Location")

# Default to "Detect Automatically"
location_option = st.radio("Location Input", ("Detect Automatically", "Enter Manually"), index=0)
location = {}

if location_option == "Detect Automatically":
    location = {"latitude": 21.2848, "longitude": 74.8444}
    st.success(f"✅ Detected Location: {location['latitude']}, {location['longitude']}")
elif location_option == "Enter Manually":
    latitude = st.number_input("🌍 Enter Latitude", value=37.7749, format="%.6f")
    longitude = st.number_input("🌍 Enter Longitude", value=-122.4194, format="%.6f")
    location = {"latitude": latitude, "longitude": longitude}

# 🔄 Shortcut Button to Homepage


st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌀 Fetch Weather & Pollution Data
def fetch_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,relative_humidity_2m,precipitation&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation&daily=temperature_2m_max,temperature_2m_min,relative_humidity_2m_max,relative_humidity_2m_min,wind_speed_10m_max,precipitation_sum"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except requests.RequestException:
        return None

def fetch_pollution(latitude, longitude):
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&current=pm2_5,pm10,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,european_aqi&hourly=pm2_5,pm10,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except requests.RequestException:
        return None

# ⚡ Fetch Data & Display
if location:
    latitude, longitude = location["latitude"], location["longitude"]
    weather_data = fetch_weather(latitude, longitude)
    pollution_data = fetch_pollution(latitude, longitude)

    if weather_data and pollution_data:
        # 🌡️ Extract Weather Data
        temp = weather_data.get("current", {}).get("temperature_2m", "N/A")
        wind = weather_data.get("current", {}).get("wind_speed_10m", "N/A")
        humidity = weather_data.get("current", {}).get("relative_humidity_2m", "N/A")
        rain = weather_data.get("current", {}).get("precipitation", "N/A")

        # 👨‍🌬️ Extract Pollution Data
        aqi = pollution_data.get("current", {}).get("european_aqi", "N/A")
        pm2_5 = pollution_data.get("current", {}).get("pm2_5", "N/A")
        pm10 = pollution_data.get("current", {}).get("pm10", "N/A")
        co = pollution_data.get("current", {}).get("carbon_monoxide", "N/A")
        no2 = pollution_data.get("current", {}).get("nitrogen_dioxide", "N/A")
        so2 = pollution_data.get("current", {}).get("sulphur_dioxide", "N/A")
        o3 = pollution_data.get("current", {}).get("ozone", "N/A")

        # 📊 Dashboard Layout
        st.subheader("🌍 Weather & Pollution Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌦️ Weather Data")
            st.metric("🌡️ Temperature", f"{temp}°C")
            st.metric("💨 Wind Speed", f"{wind} m/s")
            st.metric("💧 Humidity", f"{humidity}%")
            st.metric("🌧️ Rainfall", f"{rain} mm")
            st.map(pd.DataFrame([[latitude, longitude]], columns=["lat", "lon"]))

        with col2:
            st.subheader("👨‍🌬️ Air Pollution Data")
            st.metric("🟢 AQI", f"{aqi}")
            st.metric("🌫️ PM2.5", f"{pm2_5} µg/m³")
            st.metric("🌫️ PM10", f"{pm10} µg/m³")
            st.metric("🛢️ CO", f"{co} mg/m³")
            st.metric("🚗 NO2", f"{no2} µg/m³")
            st.metric("🌋 SO2", f"{so2} µg/m³")
            st.metric("🌀 Ozone", f"{o3} µg/m³")

        # 📈 Weather Trend Graphs
        hourly_data = pd.DataFrame(weather_data.get("hourly", {}))
        if "time" in hourly_data:
            hourly_data["time"] = pd.to_datetime(hourly_data["time"])
            hourly_data.set_index("time", inplace=True)

            for param in ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "precipitation"]:
                if param in hourly_data:
                    fig = px.line(hourly_data, x=hourly_data.index, y=param, title=f"📈 {param.replace('_', ' ').title()} Trend Over Time")
                    st.plotly_chart(fig)

        # 📉 Pollution Trend Graph
        df_trends = pd.DataFrame({
            "Parameter": ["PM2.5", "PM10", "CO", "NO2", "SO2", "O3"],
            "Value": [pm2_5, pm10, co, no2, so2, o3]
        })
        fig = px.bar(df_trends, x="Parameter", y="Value", color="Parameter", title="💀 Pollution Levels (Current)", text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
