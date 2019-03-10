import requests
while True:
    UNP = input ('Введите УНП...')
    import json
    res = requests.get('http://egr.gov.by/egrn/API.jsp?NM='+UNP)
    dt = res.json()
    for data in dt:
        info_company = ('Наименование: \n'+data['VNM']+'\nзарегистрированное от '+data['DC']+'\nСтатус: '+data['VS'])
        print(info_company)
pass