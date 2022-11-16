import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "59d0def3cb08927692cbc6416900eab4"
position = [300, 430, 555, 690, 825]

#List of cities
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]

def countryfunc(us_list, country):
    for cities in us_list:
        image = Image.open("post.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = "Latest Weather Forecast"
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 77)
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=30)
        today = date.today()
        content = date.today().strftime("%A - %B %d, %Y")
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 145)
        draw.text((x, y), content, color, font=font)


    index = 0
    for city in cities:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)


        # Example json response return
        '''{'coord': {'lon': -71.06, 'lat': 42.36}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 
        'main': {'temp': 298.88, 'feels_like': 302.56, 'temp_min': 298.15, 'temp_max': 299.82, 'pressure': 1010, 'humidity': 85}, 'visibility': 10000, 
        'wind': {'speed': 2.24, 'deg': 151, 'gust': 4.47}, 'rain': {'1h': 0.25}, 'clouds': {'all': 82}, 'dt': 1596407271, 'sys': {'type': 3, 'id': 2005683, 
        'country': 'US', 'sunrise': 1596361095, 'sunset': 1596412955}, 'timezone': -14400, 'id': 4930956, 'name': 'Boston', 'cod': 200}'''


        #city
        font = ImageFont.truetype("Inter.ttf", size=50)
        color = "rgb(0, 0, 0)"
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        #temp
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["temp"]) + "\u00b0"
        color = "rgb(255, 255, 255)"
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        #humidity
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["humidity"]) + "%"
        color = "rgb(255, 255, 255)"
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)



        index += 1
    image.save(country + "cities_pd5.png")

countryfunc([us_list], "us")