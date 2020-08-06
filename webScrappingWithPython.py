print("Assalaamu alaikkum")
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://mausam.imd.gov.in/')

soup =  BeautifulSoup(page.content,'html.parser')
#print(soup)  ## This line will give all the html view page source content

#print(soup.find_all('a'))

metro_cities_weather = soup.find(id = 'today') ## Note id only accessable not class in html

#south_metro = soup.find()

#print(metro_cities_weather)
complete_items = metro_cities_weather.find_all(class_="capitals clearfix")
items = metro_cities_weather.find_all(class_= "capital")
#items_with_space = metro_cities_weather.find_all(class_="capital ")
#items_last = metro_cities_weather.find_all(class_ = "capital last")
#print(complete_items)
#print(items)
#print(items_with_space)
#print(items_last)
#print(items[0].find(class_ = 'now').get_text())
#print(items[0].find(class_ = 'wind').get_text())
#print(items[0].find(class_ = 'minmax').get_text())

temp_level = [item.find(class_= 'now').get_text() for item in items]
wind_level = [item.find(class_= 'wind').get_text() for item in items]
rain_forecating = [item.find(class_= 'minmax').get_text() for item in items]
print(temp_level)
print(wind_level)
print(rain_forecating)

weather_stuff = pd.DataFrame(
    {
        'temprature_level' : temp_level,
        'windflow_level' : wind_level,
        'rain': rain_forecating,

    })

print(weather_stuff)

weather_stuff.to_csv("weather1.csv")
