import tkinter as tk
import json
import requests

root = tk.Tk()
root.title("Weather app")
root.geometry("400x320")

quality_colors = {
    "Good": "00e400",
    "Moderate": "ffff00",
    "Unhealthy for Sensitive Groups": "ff7e00",
    "Unhealthy": "ff0000",
    "Very Unhealthy": "8f3f97",
    "Hazardous": "7e0023",
}

try:

    def find_zip(zip_code):
        api_request = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=5&API_KEY=AB02EC2A-DFF6-4147-8E0C-370A33D013DF"
        )
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        str_data = f"{city}, {quality}, {category}"

        for color, hex_code in quality_colors.items():
            print(color)
            if color == category:
                weather_color = f"#{hex_code}"
                break

        print(api)
        label_json = tk.Label(
            root, text=str_data, font="Roboto 18", background=weather_color
        )
        label_json.pack()

        root.configure(background=weather_color)

    field_zip = tk.Entry(root)
    field_zip.pack()

    button_zip = tk.Button(
        root, text="Search", command=lambda: find_zip(field_zip.get())
    )
    button_zip.pack()

except Exception as e:
    api = "Error..."

root.mainloop()
