from tkinter import *
from unicodedata import category
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('Learn to Code')
root.geometry("400x400")


def ziplookup():
    '''zip.get()
    zipLabel =Label(root, text=zip.get())
    zipLabel.grid(row=1,column=0, columnspan=2)'''

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=D1ADE63D-1422-4932-AC7E-6244B12909AD")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for sensitive group":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + "Air Quality" + str(quality) +
                        " " + category, font=("Helvetica", 20), background="green")
        myLabel.pack()  # grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.pack()

zipbutton = Button(root, text="Lookup Zipcode", command=ziplookup)
zipbutton.pack()


root.mainloop()
