import tkinter as tk
import requests

API_KEY = "5e168dbbaab0aabe5f19210f65aa9696"

def get_weather():
    city = entry_city.get().strip()
    if city == "":
        label_result.config(text="Please enter a city name.")
        return
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("error"):
            label_result.config(text=f"Error: {data['error'].get('info', 'City not found.')}")
            return
        
        weather = data["current"]["weather_descriptions"][0]
        temp = data["current"]["temperature"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_speed"]
        
        result_text = (f"Weather: {weather}\n"
                       f"Temperature: {temp} °C\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} km/h")
        
        label_result.config(text=result_text)
    except Exception as e:
        label_result.config(text="Error retrieving data.")

root = tk.Tk()
root.title("Weather App (Weatherstack)")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_city = tk.Entry(frame, width=30)
entry_city.pack(side=tk.LEFT, padx=(0,10))

button_get = tk.Button(frame, text="Get Weather", command=get_weather)
button_get.pack(side=tk.LEFT)

label_result = tk.Label(root, text="", font=('Arial', 14), justify=tk.LEFT)
label_result.pack(pady=10)

root.mainloop()
