import streamlit as st
import requests
import matplotlib.pyplot as plt

API_KEY = "743ee0b6bd1bab2967c9557226f68831"

st.title("🌤️ Weather Visualization Dashboard")

city = st.text_input("Enter City Name", "Bengaluru")

if st.button("Show Weather Data"):
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "list" not in data:
        st.error("City not found or API Error. Try again.")
    else:
        temps = []
        humidity = []
        days = []
        pressure = []
        wind = []
        min_temps = []
        max_temps = []
        conditions = []

        for i in range(0, 40, 8):
            entry = data["list"][i]
            temps.append(entry["main"]["temp"])
            humidity.append(entry["main"]["humidity"])
            pressure.append(entry["main"]["pressure"])
            wind.append(entry["wind"]["speed"])
            min_temps.append(entry["main"]["temp_min"])
            max_temps.append(entry["main"]["temp_max"])
            conditions.append(entry["weather"][0]["main"])
            days.append(entry["dt_txt"][:10])

        # Simple summary
        st.subheader("📌 Today’s Weather Summary")
        st.write(f"**Temperature:** {temps[0]}°C")
        st.write(f"**Humidity:** {humidity[0]}%")
        st.write(f"**Pressure:** {pressure[0]} hPa")
        st.write(f"**Wind Speed:** {wind[0]} m/s")

        st.write("---")

        # Temperature graph
        st.subheader("🌡️ Temperature Trend")
        fig1, ax1 = plt.subplots()
        ax1.plot(days, temps, marker='o', color='orange')
        ax1.set_xlabel("Days")
        ax1.set_ylabel("Temperature (°C)")
        ax1.grid(True)
        st.pyplot(fig1)

        st.write("---")

        # Humidity graph
        st.subheader("💧 Humidity Levels")
        fig2, ax2 = plt.subplots()
        ax2.bar(days, humidity, color='skyblue')
        ax2.set_xlabel("Days")
        ax2.set_ylabel("Humidity (%)")
        st.pyplot(fig2)

        st.write("---")

        # Pressure graph
        st.subheader("🌬️ Pressure Levels")
        fig3, ax3 = plt.subplots()
        ax3.plot(days, pressure, marker='o', color='green')
        ax3.set_xlabel("Days")
        ax3.set_ylabel("Pressure (hPa)")
        ax3.grid(True)
        st.pyplot(fig3)

        st.write("---")

        # Wind speed graph
        st.subheader("🍃 Wind Speed")
        fig4, ax4 = plt.subplots()
        ax4.bar(days, wind, color='gray')
        ax4.set_xlabel("Days")
        ax4.set_ylabel("Wind Speed (m/s)")
        st.pyplot(fig4)

        st.write("---")

        # Min-Max graph
        st.subheader("🌡️ Min vs Max Temperature")
        fig5, ax5 = plt.subplots()
        ax5.plot(days, min_temps, marker='o', label="Min Temp", color='blue')
        ax5.plot(days, max_temps, marker='o', label="Max Temp", color='red')
        ax5.legend()
        ax5.set_xlabel("Days")
        ax5.set_ylabel("Temperature (°C)")
        ax5.grid(True)
        st.pyplot(fig5)

        st.write("---")

        # Pie chart
        st.subheader("🌦️ Weather Condition Distribution")
        fig6, ax6 = plt.subplots()
        unique = list(set(conditions))
        vals = [conditions.count(x) for x in unique]
        ax6.pie(vals, labels=unique, autopct="%1.1f%%")
        st.pyplot(fig6)
