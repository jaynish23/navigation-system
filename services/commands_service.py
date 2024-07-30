import datetime
import os
from services.weather_service import WeatherService as ws
import object_detection as od



class commands:

    def __init__(self):
        self.commands = {
            'time': self.get_time,
            'help': self.get_help,
            'day': self.get_day,
            'date': self.get_date,
            'weather': self.get_weather,
            'start': self.start_navigation,
            'stop': self.stop_navigation,
            'errors': self.errors
        }
        self.wetherObj = ws()

    def get_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        str = f"The current time is {current_time}"
        return str

    def get_help(self):
        str = "Available commands "
        for x in self.commands:
            str = str + ' ' + x
        return str

    def get_day(self):
        day = datetime.datetime.today().strftime("%A")
        str = f"Today is {day}"
        return str

    def get_date(self):
        date = datetime.datetime.now().date()
        str = f"Today's Date is {date}"
        return str

    def get_weather(self):
        weatherdata = self.wetherObj.get_weather_data()
        return weatherdata
    
    def start_navigation(self):
        with open('state.txt', 'w') as file:
            file.write('true')
        return 'Starting Navigation'


    def stop_navigation(self):
        with open('state.txt', 'w') as file:
            file.write('false')
        return 'Exiting Navigation'
    
    def errors(self, value):
        if value == 1: return "error1"
        elif value == 2: return "error2"
        else: return "error3"
