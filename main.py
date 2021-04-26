import requests
s_city = "Chernihiv,UA"
appid = ""
city_id = 0
city = []
try:
    x = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = x.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]

    city = cities

    city_id = data['list'][1]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:
    x = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ua', 'APPID': appid})
    data = x.json()
    print()
    print("Город:", city[1])
    print("Погода на улице:", data['weather'][0]['description'])
    print("Температура сейчас:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура:", data['main']['temp_max'])
except  Exception as e:
    print("Exception (weather):", e)
    pass