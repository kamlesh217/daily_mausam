from django.shortcuts import render
from pprint import pprint
import requests
from django.contrib import messages

def index(request):
    city="Delhi"
    base_url=f"http://api.weatherapi.com/v1/current.json?key=0fe078910dba45019cd62234220404&q={city}&aqi=yes"
    weather_data=requests.get(base_url).json()
    context={
    "city":weather_data['location']['name'],
    "time_zone":weather_data['location']['tz_id'],
    'country':weather_data['location']['country'],
    'latitude':weather_data['location']['lat'],
    'longitude':weather_data['location']['lon'],
    'feel_like':weather_data['current']['feelslike_c'],
    'temp':weather_data['current']['temp_c'],
    'humidity':weather_data['current']['humidity'],
    'speed':weather_data['current']['wind_kph'],
    'cloud':weather_data['current']['cloud'],
    "localtime":weather_data['location']['localtime'],
    }
    if request.method=='POST':
        city=request.POST['location']
        base_url=f"http://api.weatherapi.com/v1/current.json?key=0fe078910dba45019cd62234220404&q={city}&aqi=yes"
        weather_data=requests.get(base_url).json()
        if requests.get(base_url).status_code()==400:
            messages.success(request, 'Enter Another Area Name')
            city="ahmedabad"
            return render(request, 'dashboard.html',context)
        else:
            context={
            "city":weather_data['location']['name'],
            "time_zone":weather_data['location']['tz_id'],
            'country':weather_data['location']['country'],
            'latitude':weather_data['location']['lat'],
            'longitude':weather_data['location']['lon'],
            'feel_like':weather_data['current']['feelslike_c'],
            'temp':weather_data['current']['temp_c'],
            'humidity':weather_data['current']['humidity'],
            'speed':weather_data['current']['wind_kph'],
            'cloud':weather_data['current']['cloud'],
            "localtime":weather_data['location']['localtime'],
            }
        return render(request, 'dashboard.html',context)
    return render(request, 'dashboard.html',context)



