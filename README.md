# IT-WebAppDevelopment-WeatherVisual
Web Application built using Flask (Python), HTML, and CSS.

Accessed through a Virtual Server on http://127.0.0.1:8080/

Allows user to enter in any city and receive a future forecast related to:
- Temperature (Average/High/Low)
- Feels Like
- Humidity
- Windspeed
- UV Index and Meaning
- Weather Condition

# Data
Data was collected using Visual Crossings' Weather Data Services API
Link: https://www.visualcrossing.com/weather/weather-data-services

# Data Query Example
{
 "queryCost": 1,
 "latitude": 48.2026,
 "longitude": 16.3684,
 "resolvedAddress": "Wien, Österreich",
 "address": "Vienna",
 "timezone": "Europe/Vienna",
 "tzoffset": 2,
 "description": "Similar temperatures continuing with a chance of rain Saturday & Sunday.",
 "days": [
  {
   "datetime": "2022-07-17",
   "datetimeEpoch": 1658008800,
   "tempmax": 26.1,
   "tempmin": 13,
   "temp": 20.7,
   "feelslikemax": 26.1,
   "feelslikemin": 13,
   "feelslike": 20.7,
   "dew": 7.4,
   "humidity": 44.8,
   "precip": 0,
   "precipprob": 0,
   "precipcover": 0,
   "preciptype": null,
   "snow": 0,
   "snowdepth": 0,
   "windgust": 26.6,
   "windspeed": 14.8,
   "winddir": 228.8,
   "pressure": 1025.1,
   "cloudcover": 23.5,
   "visibility": 15.3,
   "solarradiation": 341,
   "solarenergy": 29.5,
   "uvindex": 9,
   "severerisk": 10,
   "sunrise": "05:11:50",
   "sunriseEpoch": 1658027510,
   "sunset": "20:49:00",
   "sunsetEpoch": 1658083740,
   "moonphase": 0.6,
   "conditions": "Partially cloudy",
   "description": "Partly cloudy throughout the day.",
   "icon": "partly-cloudy-day",
   "stations": [
    "LOWW",
    "D4277",
    "remote"
   ],
   "source": "comb",
   "hours": [
    {
     "datetime": "12:00:00",
     "datetimeEpoch": 1658052000,
     "temp": 23,
     "feelslike": 23,
     "humidity": 33.3,
     "dew": 6,
     "precip": 0,
     "precipprob": 0,
     "snow": 0,
     "snowdepth": 0,
     "preciptype": null,
     "windgust": 17.6,
     "windspeed": 11.2,
     "winddir": 330,
     "pressure": 1026,
     "visibility": 10,
     "cloudcover": 0,
     "solarradiation": 817,
     "solarenergy": 2.9,
     "uvindex": 8,
     "severerisk": 10,
     "conditions": "Clear",
     "icon": "clear-day",
     "stations": [
      "LOWW",
      "D4277"
     ],
     "source": "obs"
    },
    {
     "datetime": "13:00:00",
     "datetimeEpoch": 1658055600,
     "temp": 24,
     "feelslike": 24,
     "humidity": 31.35,
     "dew": 6,
     "precip": 0,
     "precipprob": 0,
     "snow": 0,
     "snowdepth": 0,
     "preciptype": null,
     "windgust": 24.8,
     "windspeed": 9.4,
     "winddir": 335.3,
     "pressure": 1026,
     "visibility": 10,
     "cloudcover": 19.2,
     "solarradiation": 880,
     "solarenergy": 3.2,
     "uvindex": 9,
     "severerisk": 10,
     "conditions": "Clear",
     "icon": "clear-day",
     "stations": [
      "LOWW",
      "D4277"
     ],
     "source": "obs"
    }
   ]
  }
 ],
 "alerts": [],
 "stations": {
  "LOWW": {
   "distance": 17568,
   "latitude": 48.12,
   "longitude": 16.57,
   "useCount": 0,
   "id": "LOWW",
   "name": "LOWW",
   "quality": 50,
   "contribution": 0
  },
  "AV723": {
   "distance": 2905,
   "latitude": 48.225,
   "longitude": 16.348,
   "useCount": 0,
   "id": "AV723",
   "name": "OE1TRI Vienna AT",
   "quality": 0,
   "contribution": 0
  },
  "LOAV": {
   "distance": 26907,
   "latitude": 47.97,
   "longitude": 16.27,
   "useCount": 0,
   "id": "LOAV",
   "name": "LOAV",
   "quality": 21,
   "contribution": 0
  },
  "D4277": {
   "distance": 9109,
   "latitude": 48.123,
   "longitude": 16.394,
   "useCount": 0,
   "id": "D4277",
   "name": "DW4277 Leopoldsdorf AT",
   "quality": 0,
   "contribution": 0
  }
 },
 "currentConditions": {
  "datetime": "15:40:05",
  "datetimeEpoch": 1658065205,
  "temp": 28.7,
  "feelslike": 27.5,
  "humidity": 26.9,
  "dew": 7.8,
  "precip": 0,
  "precipprob": null,
  "snow": 0,
  "snowdepth": 0,
  "preciptype": null,
  "windgust": null,
  "windspeed": 16.6,
  "winddir": 340,
  "pressure": 1025,
  "visibility": 10,
  "cloudcover": 3.6,
  "solarradiation": 754,
  "solarenergy": 2.7,
  "uvindex": 8,
  "conditions": "Clear",
  "icon": "clear-day",
  "stations": [
   "LOWW",
   "AV723",
   "LOAV"
  ],
  "sunrise": "05:11:50",
  "sunriseEpoch": 1658027510,
  "sunset": "20:49:00",
  "sunsetEpoch": 1658083740,
  "moonphase": 0.6
 }
}
