import requests
from flask import Flask, render_template, request
app = Flask(__name__)
cities = ['London']

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        #new_city = request.form.get('city')
        city = request.form.get('city')
        cities.append(city)
#http://api.openweathermap.org/data/2.5/weather?q=paris&units=imperial&appid=ba55f7979e7823f5404600a5d1f983eb
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ba55f7979e7823f5404600a5d1f983eb'
    #city = 'London'
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        weather = {
                    'city' : city,
                    'temperature' : r['main']['temp'],
                    'description' : r['weather'][0]['description'],
                    'icon' : r['weather'][0]['icon']
                    }

        print(weather, r)
        weather_data.append(weather)

    return render_template('index2.html', weather_data=weather_data)
    #return render_template('index.html', weather = weather)

if __name__ == '__main__':
    app.run(debug=True)
