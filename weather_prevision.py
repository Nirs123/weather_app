import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
now = datetime.now()
class weather:
    def __init__(self,city):
        tmp = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={os.getenv('WEATHER_TOKEN')}&contentType=json")
        self.data = json.loads(tmp.text)

    def twenty_four_hours_prevision(self):
        tfh_temp,tfh_wind,tfh_icon = [],[],[]
        current_hour = int(now.strftime("%H"))
        j = current_hour
        k = 0
        for i in range(current_hour,current_hour + 26):
            if j <= 23:
                tfh_temp.append(self.data["days"][k]["hours"][j]["temp"])
                tfh_icon.append(self.data["days"][k]["hours"][j]["icon"])
                tfh_wind.append(self.data["days"][k]["hours"][j]["windspeed"])
                j += 1
            else:
                j = 0
                k += 1
        return tfh_temp,tfh_icon,tfh_wind

    def seven_days_prevision(self):
        sd_temp,sd_wind,sd_icon = [],[],[]
        k = 0
        for i in range(k,7):
            sd_temp.append(self.data["days"][k]["temp"])
            sd_icon.append(self.data["days"][k]["icon"])
            sd_wind.append(self.data["days"][k]["windspeed"])
            k += 1
        return sd_temp,sd_icon,sd_wind

    def fourteen_days_prevision(self):
        fd_temp,fd_wind,fd_icon = [],[],[] 
        k = 0
        for i in range(k,14):
            fd_temp.append(self.data["days"][k]["temp"])
            fd_icon.append(self.data["days"][k]["icon"])
            fd_wind.append(self.data["days"][k]["windspeed"])
            k += 1
        return fd_temp,fd_icon,fd_wind