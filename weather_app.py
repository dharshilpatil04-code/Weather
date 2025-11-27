#Jackfruit Problem

import streamlit as st
import requests
import matplotlib.pyplot as plt

API_KEY="743ee0b6bd1bab2967c9557226f68831"

st.title("Weather Visualization Dashboard")

city = st.text_input("Enter city name", "Bengaluru")

if st.button("Show Weather Data"):
    
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()

    if "list" not in data:
        st.error("City not found or API Error. Try again.")
    else:
        temps=[]
        humidity=[]
        days=[]
        pressure=[]
        wind=[]
        min_temps=[]
        max_temps=[]
        conditions=[]

        for i in range(0,40,8):
            entry=data["list"][i]
            temps.append(entry["main"]["temp"])
            humidity.append(entry["main"]["humidity"])
            pressure.append(entry["main"]["pressure"])
            wind.append(entry["wind"]["speed"])
            min_temps.append(entry["main"]["temp_min"])
            max_temps.append(entry["main"]["temp_max"])
            conditions.append(entry["weather"][0]["main"])
            days.append(entry["dt_txt"][:10])

        # Temperature
        st.subheader("Temperature Trend")
        fig1, ax1 = plt.subplots()
        ax1.plot(days, temps, marker='o')
        st.pyplot(fig1)

        # Humidity
        st.subheader("Humidity Levels")
        fig2, ax2 = plt.subplots()
        ax2.bar(days, humidity)
        st.pyplot(fig2)

        # Pressure
        st.subheader("Pressure Levels")
        fig3, ax3 = plt.subplots()
        ax3.plot(days, pressure, marker='o')
        st.pyplot(fig3)

        # Wind Speed
        st.subheader("Wind Speed")
        fig4, ax4 = plt.subplots()
        ax4.bar(days, wind)
        st.pyplot(fig4)

        # Min-Max Temperature
        st.subheader("Min vs Max Temperature")
        fig5, ax5 = plt.subplots()
        ax5.plot(days, min_temps, marker='o', label="Min Temp")
        ax5.plot(days, max_temps, marker='o', label="Max Temp")
        ax5.legend()
        st.pyplot(fig5)

        # Pie Chart
        st.subheader("Weather Condition Distribution")
        fig6, ax6 = plt.subplots()
        unique = list(set(conditions))
        vals = [conditions.count(x) for x in unique]
        ax6.pie(vals, labels=unique, autopct="%1.1f%%")
        st.pyplot(fig6)
