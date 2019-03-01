import requests
s_city = "Минск(РБ)"
city_id = 625144
appid = "bc05da5146139fabcfcdbd7c2c66a7d6"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print ("Сегодня в городе:", s_city)
    print("состояние облачности:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    cloudiness = (data['weather'][0]['description']+'\nсредняя температура составит около')
    wheather = ('Сегодня в городе: '+s_city+cloudiness+'\n')
    response = requests.get('https://api.telegram.org/bot657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc/sendMessage?chat_id=251325174&text=Бендер докладывает прогноз погоды на сегодня:\n'+wheather)
    temperature= (data['main']['temp'])
    response = requests.get('https://api.telegram.org/bot657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc/sendMessage?chat_id=251325174&text='+temperature)
    input('Нажмите "ENTER" для выхода')
except Exception as e:
    pass
    