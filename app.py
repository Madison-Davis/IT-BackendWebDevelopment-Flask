# Imports
from flask import Flask, render_template, request
import os, requests
import cgi

app = Flask(__name__)
form = cgi.FieldStorage()
searchterm =  form.getvalue('cityName')

@app.route("/")
def inputHTML():
    return render_template("input.html")

@app.route('/cityWeather', methods=['POST'])
def handle_data():
    cityName = str(request.form['cityName'])
    URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + cityName + "?unitGroup=metric&key=GNRV9JMBK2UXZ9ZMDVFHGFVFP&contentType=json"
    response = requests.get(URL)
    responseJSON = response.json()
    # Get 5 Days, 10 Variables per Day
    headings = ("Date", "High Temp", "Low Temp", "Average Temp", "Feels Like", "Humidity", "Windspeed", "UV Index", "UV Index Meaning", "Conditions")
    data = []
    for index in range(0,5):
        singleDay = []
        singleDay.append(responseJSON["days"][index]["datetime"])
        singleDay.append(responseJSON["days"][index]["tempmax"]) # C
        singleDay.append(responseJSON["days"][index]["tempmin"]) # C
        singleDay.append(responseJSON["days"][index]["temp"]) # C
        singleDay.append(responseJSON["days"][index]["feelslike"]) # C
        singleDay.append(responseJSON["days"][index]["humidity"]) # %
        singleDay.append(responseJSON["days"][index]["windspeed"]) # kmph
        UVIndex = responseJSON["days"][index]["uvindex"]
        singleDay.append(UVIndex)
        if UVIndex < 3:
            singleDay.append("Low UV Index")
        elif 3 <= UVIndex < 6:
            singleDay.append("Medium UV Index")
        elif 6 <= UVIndex < 8: 
            singleDay.append("High UV Index")
        elif 8 <= UVIndex < 11:
            singleDay.append("Very High UV Index")
        else:
            singleDay.append("Extreme UV Index")
        singleDay.append(responseJSON["days"][index]["hours"][0]["conditions"])
        data.append(singleDay)
    return render_template("table.html", headings = headings, data = data, cityName = cityName)

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug = True)