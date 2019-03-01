class AnthropomorphicRobot ():
    Name = 'Меня зовут Bender ver. 3.7.'
    Age = 1500
    Office_position = 'Робот "Межгалактического экспресса"'
    def set(self, Name, Age, Office_position):
        self.Name = Name
log = open('log.txt', 'w')
token = '657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc'
log.write("import telebot\n")
log.write("'ЛЕТОПИСИ БЕНДЕРА v.2.7'\n\n")
Bender = AnthropomorphicRobot ()
bender_hello = 'Я робот из Футурамы. Ты можешь пообщаться со мной.\nНо я ещё на стадии разработки.\nМеня создаёт великий Творец Александр IV. '
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
except Exception as e:
    pass
Name = 'Меня зовут Bender ver. 3.7.\n'
Dream = '010100111111100010111010100 2! ААА.... Мне приснился страшный сон, там была ДВОЙКА...\n '
print (Dream, Name, bender_hello)
your_name = (input("А как тебя зовут? ")) 
print (your_name+', принеси мне пива. Давай бухать.\n')
log.write(Dream+Name+'\n'+bender_hello+'\n'+your_name)
bear_yes = ['Давай', 'Да', 'Буду', 'Yeas', 'yes', 'да', 'давай', 'буду', 'можно', 'конечно', 'возможно', 'погнали']
bear_no = ['Не охото', 'нет', 'не', 'не охото', 'Нет', 'не буду', 'отвали', 'Не', 'no', 'none', 'ноу']
bear_deal = 'к тебе дело'
bear_benderself = 'расскажи о себе'
bear_solution = input("Будешь? ")
if bear_solution in bear_yes:
    print(your_name+', Я знал, что ты отличный собутыльник.\n')
    club_yes = ['Я за', 'Погнали', 'погнали','Давай', 'Да', 'Буду', 'Yeas', 'yes', 'да', 'давай', 'буду', 'можно', 'конечно']
    club_no = ['Не охото', 'нет', 'не охото', 'Нет', 'не', 'не хочу', 'в другой раз', 'Не', 'No', 'no', 'none']
    club_solution = input("Пойдем в клуб? ")
    if club_solution in club_yes:
        print(your_name+', А ты мне уже нравишься!')
        import webbrowser
        music_jazz = 'джаз'
        music_blues = 'блюз'
        music_rock = 'рок'
        music_folk = ['рок', 'фолк-рок', 'рок-баллады', 'русский рок', 'панк-рок']
        music_classic = ['классика', 'классику', 'оперу', 'церковное']
        music_shansone = 'шансон'
        music_solution = input("Какое послушаем музло? ")
        if music_solution == music_jazz:
            print('Круто!')
            webbrowser.open('https://www.youtube.com/watch?v=EpaweZfY2NI')
        if music_solution == music_blues:
            print('Я люблю черный блюз. Балабэбэбэбэб - ээ   -  ее')
            webbrowser.open('https://www.youtube.com/watch?v=X8ibJpcvurk')
        if music_solution == music_rock:
            print('Цой жив!')
            webbrowser.open('https://www.youtube.com/watch?v=6C2ti3x9OAA')
        if music_solution == music_folk:
            print('Да ты гонишь!!')
            webbrowser.open('https://www.youtube.com/watch?v=LjphKWJ90Ls')
        if music_solution == music_classic:
            print('Это же полная нудятина')
            webbrowser.open('https://www.youtube.com/watch?v=bKAdlyDcas4&start_radio=1&list=RDbKAdlyDcas4')
        if music_solution == music_shansone:
            print('А ты был когда-нибудь в тюрьме для роботов?')
            webbrowser.open('https://www.youtube.com/watch?v=I7DFRWGjQTs')
    if club_solution in club_no:
        print('Ну давай останемся тут и посмотри телик...')
        film_solution = input("Какое тебе нравится кино? ")
        print(film_solution+your_name+'может и отличное кино, но я врубаю ФУТУРАМУ')
        import webbrowser
        webbrowser.open('https://www.youtube.com/results?search_query=футурама+1+1')
    else:
            print('Я всего лишь робот. И пока творец не научил меня понимать человека настолько хорошо. ')
    log.write('Будешь?\n'+bear_solution+'\n'+club_solution+'\n'+music_solution)
if bear_solution in bear_no:
    print('Хватит ломаться. Чего тут ржаветь, как старые тостеры. ')
    funny_yes = ['Ну, давай', 'погнали','Давай', 'Да', 'Буду', 'Yeas', 'yes', 'да', 'давай', 'буду', 'можно', 'конечно']
    funny_no = ['Не охото', 'нет', 'не охото', 'Нет', 'не хочу', 'не', 'no', 'No', 'none']
    funny_solution = input("Может все таки повеселимся? ")
    if funny_solution in funny_yes:
        print(your_name+', а ты мне уже нравишься!')
        club_yes = ['Погнали', 'погнали','Давай', 'Да', 'Буду', 'Yeas', 'yes', 'да', 'давай', 'буду', 'можно', 'конечно']
    club_no = ['Не охото', 'нет', 'не охото', 'Нет', 'не', 'не хочу', 'в другой раз']
    club_solution = input("Пойдем в клуб? ")
    if club_solution in club_yes:
        print(your_name+', А ты мне уже нравишься!')
        music_jazz = 'джаз'
        music_blues = 'блюз'
        music_rock = 'рок'
        music_folk = ['рок', 'фолк-рок', 'рок-баллады', 'русский рок', 'панк-рок']
        music_classic = ['классика', 'классику', 'оперу', 'церковное']
        music_shansone = 'шансон'
        music_solution = input("Какое послушаем музло? ")
        import webbrowser
        if music_solution == music_jazz:
            print('Круто!')
            webbrowser.open('https://www.youtube.com/watch?v=EpaweZfY2NI')
        if music_solution == music_blues:
            print('Я люблю черный блюз. Балабэбэбэбэб - ээ   -  ее')
            webbrowser.open('https://www.youtube.com/watch?v=X8ibJpcvurk')
        if music_solution == music_rock:
            print('Цой жив!')
            webbrowser.open('https://www.youtube.com/watch?v=6C2ti3x9OAA')
        if music_solution == music_folk:
            print('Да ты гонишь!!')
            webbrowser.open('https://www.youtube.com/watch?v=LjphKWJ90Ls')
        if music_solution == music_classic:
            print('Это же полная нудятина')
            webbrowser.open('https://www.youtube.com/watch?v=bKAdlyDcas4&start_radio=1&list=RDbKAdlyDcas4')
        if music_solution == music_shansone:
            print('А ты был когда-нибудь в тюрьме для роботов?')
            webbrowser.open('https://www.youtube.com/watch?v=I7DFRWGjQTs')
        log.write(music_solution)
        import bender
    if funny_solution in funny_no:
        print('Ну давай останемся тут и посмотри телик...')
        film_solution = input("Какое тебе нравится кино? ")
        print(film_solution+your_name+'может и отличное кино,\n но я врубаю ФУТУРАМУ')
        log.write('Будешь?\n'+bear_solution+'\n'+funny_solution+'\n'+club_solution+'\n'+music_solution)
        import webbrowser
        webbrowser.open('https://www.youtube.com/results?search_query=футурама+1+1')
if bear_deal in bear_solution:
    print(your_name+', Сейчас порешаем все вопросы.')
    deal_calculator = ['посчитай мне', 'посчитай', 'калькулятор']
    deal_palindrome = ['палиндром', 'обратно также?']
    deal_solution = input("Какая стоит задача? ")
    if deal_solution in deal_calculator:
        from calculator import Calculator
        print("\nОбращайся, если будет скучно. Не будь в печали. \nНастоящие роботы не устают от веселья!!")
        log.write(deal_solution)
        import bender
if bear_benderself in bear_solution:
    benderself_solution = input("Что тебе интересно? ")
    benderself_age = ['сколько тебе лет', 'возраст', 'Сколько тебе лет?']
    benderself_office = ['должность', 'кем ты работаешь?']
    benderself_name = ['как тебя зовут']
    benderself_abilities = []
    benderself_help = []
    benderself_parents = []
    benderself_opportunities = []
    if benderself_solution in benderself_age:
        print(Bender.Age)
    if benderself_solution in benderself_office:
        print(Bender.Office_position)
    if benderself_solution in benderself_name:
        print(Bender.Name)
    else:
        import bender    
    log.write('\nЧто тебе интересно?\n'+benderself_solution)
log.write("\nОбращайся, если будет скучно. Не будь в печали.\nНастоящие роботы не устают от веселья!!")
log.close()
import os
os.startfile('FACE.png')

# Token Телеги 657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc
## получить обновления Бендера https://api.telegram.org/bot657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc/getUpdates
## Для ответов от лица Бендера используй команду https://api.telegram.org/bot657185336:AAHkeN6wa4TeNXlmIWp5P0JzdgmUk4N4MZc/sendMessage?chat_id=251325174&text=Я%20робот%20бендер%20из%20футурамы