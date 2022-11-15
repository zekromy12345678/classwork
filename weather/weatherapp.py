import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = ""
position = [300, 430, 555, 690, 825]

#List of cities
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]

def countryfunc(city_list, country):
    for cities in city_list:
        image = Image.open("post.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = "Latest Weather Forecast"
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 77)
        draw.text((x,y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=30)
        today = date.today()
        content = date.today().strftime("%A - %B %d, %Y")
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 145)
        draw.text((x, y), content, color, font=font)


#countryfunc([us_list], "us")