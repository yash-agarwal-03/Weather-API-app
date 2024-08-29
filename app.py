from flask import Flask, render_template,request,flash
import requests
import os
app=Flask(__name__)

api_key='32def3db4fdf50e4f0476d13907b132f'
api_keyforecast='9da8cd4fe452f2145d82b02c899552a6'
app.secret_key = os.urandom(24)
print(f"Your secret key - {app.secret_key}")

@app.route('/', methods=['GET','POST'])
def index():
    if request.method== 'POST':
        city_name=request.form['city_name']
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}'
        
        response=requests.get(url.format(city_name)).json()
        print(response)
        if response.get('cod') != 200:
            error='Place not found. Try Again'
            return render_template('index.html',error=error)
        else:
            error=f"Here's the weather info for {city_name.upper()}"
            return callIndex(response,city_name,error=error)
    else:
        return render_template('index.html',error='Welcome to the Weather App')

def callIndex(response,city_name,error):
    city_name=city_name.upper()
    temp=response['main']['temp']
    mintemp=response['main']['temp_min']
    maxtemp=response['main']['temp_max']
    humidity=response['main']['humidity']
    windspeed=response['wind']['speed']
    weather=response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    return render_template('index.html',error=error,temp=temp,min_temp=mintemp,max_temp=maxtemp,weather=weather,humdt=humidity,windS=windspeed,icon=icon,city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)