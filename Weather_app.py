from cProfile import label
from tkinter import *   # Importing Tkinter library
import requests        # Importing requests library
import json        # Importing json library
import datetime        # Importing datetime library
import time
import threading
root = Tk()   # Creating a root window
root.title("Weather App")   # Title name
root.geometry("500x500")   # Screen Size
root.configure(background='white')    # Background color of Window

# Creating Functions 
lab = Label(root)
lab.pack()
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=30.551&lon=73.391&appid=94e563d7ef8e826858cdfbc6165868a2')
data = json.loads(response.content)
date_time = datetime.datetime.now()

def clock():   # Creating clock function
    time = datetime.datetime.now().strftime("%H:%M:%S")
    lab.config(text=time, font=("Helvetica", 20), bg="white")
    
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

def date():
    date_time = datetime.datetime.now()
    Label(root, text=date_time.strftime("%d/%m/%Y"), font=("Helvetica", 20), bg="white").pack()

def temperature():
    temperature = data['main']['temp']
    temp = temperature - 273.15
    temp = round(temp)
    Label(root, text="Temperature: " + str(temp) + " °C", font=("Helvetica", 20), bg="white").pack()


def humidity():
    humidity = data['main']['humidity']
    Label(root, text="Humidity: " + str(humidity) + " %", font=("Helvetica", 20), bg="white").pack()

def city():
    city = data['name']
    Label(root, text="City: " + str(city), font=("Helvetica", 20), bg="white").pack()

def country():
    country = data['sys']['country']
    Label(root, text="Country: " + str(country[0]), font=("Helvetica", 20), bg="white").pack()

def weather():
    weather = data['weather'][0]['main']
    Label(root, text="Weather: " + str(weather), font=("Helvetica", 20), bg="white").pack()


# Calling Functions
clock()
date()
weather()
temperature()
humidity()
city()
country()

root.mainloop()


