print ('Помощь: 0 - Австралия; 1 - Болгария; 2 - Украина; 4 - США; 5 - ЕС; 6 - Польша; \n7 - Иран; 9 - Япония; 10 - Канада; 11- КНР; 13 - Молдавия; 14 - Новая зеландия; \n16 - РФ; 21 - Турция; 22 - Англия; 23 - Чехия') 
import requests
while True:
    i = int(input('Введите номер валюты для получения данных о курсе: '))
    response = requests.get ('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')
    data = response.json()
    print ('Курс белорусского рубля к ')
    print (data[i]['Cur_Name']+'на сегодня составляет:')
    print (data[i]['Cur_OfficialRate'])