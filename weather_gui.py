#Weather Forecast
import tkinter, requests
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

#Define Window
root = tkinter.Tk()
root.title("Weather Forecast")
#root.iconbitmap("weather.ico")
root.geometry("400x400")
root.resizable(0,0)

#Define fonts and colors
sky_color = "#fc42b2"
grass_color = "#42053d"
output_color = "#dabbfa"
input_color = "#eda6eb"
large_font = ("Arial", 14)
small_font = ("Arial", 10)

#Define Functions
def search():
    """Use the openweather API to look up current weather conditions for city and/or zip"""
    global response

    #Get API response
    #URL and API key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = "8e2972b7e4af80e839b62cb18d41f8ed"

    #Search by the appropriate query...city or zip
    if search_method.get() == 1:
        querystring = {"q":city_entry.get(), "appid":api_key, "units":"imperial"}
    elif search_method.get() == 2:
        querystring = {"zip": city_entry.get(), "appid": api_key, "units": "imperial"}

    #Call API
    response = requests.request("GET", url, params=querystring)
    response = response.json()

    #Example json response return
    '''{'coord': {'lon': -71.06, 'lat': 42.36}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 
    'main': {'temp': 298.88, 'feels_like': 302.56, 'temp_min': 298.15, 'temp_max': 299.82, 'pressure': 1010, 'humidity': 85}, 'visibility': 10000, 
    'wind': {'speed': 2.24, 'deg': 151, 'gust': 4.47}, 'rain': {'1h': 0.25}, 'clouds': {'all': 82}, 'dt': 1596407271, 'sys': {'type': 3, 'id': 2005683, 
    'country': 'US', 'sunrise': 1596361095, 'sunset': 1596412955}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}'''

    get_weather()
    get_icon()

def get_weather():
    """Grab information from API response and update our labels"""
    #Gather data to be used from the API call
    city_name = response["name"]
    city_lat = str(response["coord"]["lat"])
    city_lon = str(response["coord"]["lon"])

    main_weather = response["weather"][0]["main"]
    description = response["weather"][0]["description"]

    temp = str(response["main"]["temp"])
    feels_like = str(response["main"]["feels_like"])
    temp_min = str(response["main"]["temp_min"])
    temp_max = str(response["main"]["temp_max"])
    humidity = str(response["main"]["humidity"])

    #Update output labels
    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather: " + main_weather + ", " + description, font=small_font, bg=output_color)
    temp_label.config(text="Temperature: " + temp + " F", font=small_font, bg=output_color)
    feels_label.config(text="Feels Like: " + feels_like + " F", font=small_font, bg=output_color)
    temp_min_label.config(text="Min Temperature: " + temp_min + " F", font=small_font, bg=output_color)
    temp_max_label.config(text="Max Temperature: " + temp_max + " F", font=small_font, bg=output_color)
    humidity_label.config(text="Humidity: " + humidity, font=small_font, bg=output_color)

def get_icon():
    """Get the appropriate weather icon from API response"""
    global img

    #Get the icon from the API response
    icon_id = response["weather"][0]["icon"]

    #Get the icon from the correct website
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    #Make the request at the url to download the icon
    icon_response = requests.get(url, stream=True)

    #Turn into a form that tkinter/python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

    #Update label
    photo_label.config(image=img)

#Define Layout
#Create Frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

#Output Frame Layout
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Input Frame Layout
#Create input frame buttons and layout
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text="Submit", font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text="Search by city name", variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Search by zip code", variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=15, padx=10)
search_zip.grid(row=1, column=1, padx=10, pady=15)

#Run the windows main loop
root.mainloop()
