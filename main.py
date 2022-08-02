import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
now = datetime.now()

def main(city):
    tmp = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={os.getenv('WEATHER_TOKEN')}&contentType=json")
    json_data = json.loads(tmp.text)
    return json_data

def twenty_four_hours(data):
    tfh_temp,tfh_wind,tfh_icon = [],[],[]
    current_hour = int(now.strftime("%H"))
    j = current_hour
    k = 0
    for i in range(current_hour,current_hour + 26):
        if j <= 23:
            tfh_temp.append(data["days"][k]["hours"][j]["temp"])
            tfh_icon.append(data["days"][k]["hours"][j]["icon"])
            tfh_wind.append(data["days"][k]["hours"][j]["windspeed"])
            j += 1
        else:
            j = 0
            k += 1
    return tfh_temp,tfh_icon,tfh_wind

def seven_days(data):
    sd_temp,sd_wind,sd_icon = [],[],[]
    k = 0
    for i in range(k,7):
        sd_temp.append(data["days"][k]["temp"])
        sd_icon.append(data["days"][k]["icon"])
        sd_wind.append(data["days"][k]["windspeed"])
        k += 1
    return sd_temp,sd_icon,sd_wind

def fourteen_days(data):
    fd_temp,fd_wind,fd_icon = [],[],[] 
    k = 0
    for i in range(k,14):
        fd_temp.append(data["days"][k]["temp"])
        fd_icon.append(data["days"][k]["icon"])
        fd_wind.append(data["days"][k]["windspeed"])
        k += 1
    return fd_temp,fd_icon,fd_wind