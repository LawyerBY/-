import requests
import json

while True:
    print("Выберите тип поиска:")
    print("1. Поиск по УНП")
    print("2. Поиск по наименованию компании")
    choice = input("Введите 1 или 2 (или 'q' для выхода): ").strip()
    if choice.lower() == 'q':
        break

    if choice == '1':
        query = input("Введите УНП: ").strip()
    elif choice == '2':
        query = input("Введите наименование компании: ").strip()
    else:
        print("Неверный выбор. Попробуйте еще раз.\n")
        continue

    # Формируем URL для запроса. Параметр 'NM' используется для поиска.
    url = "http://egr.gov.by/egrn/API.jsp?NM=" + query

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности ответа

        dt = response.json()

        if not dt:
            print("Данные не найдены.\n")
        else:
            for idx, data in enumerate(dt, start=1):
                print("\nРезультат", idx)
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except json.JSONDecodeError:
        print("Ошибка обработки JSON. Возможно, сервер вернул некорректный ответ.")

    print("\n")
