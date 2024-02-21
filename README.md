Тестовое задание для отбора на вакансию https://hh.ru/vacancy/92715286?

Проект состоит из двух модулей:
  • main.py - главный файл, содержащий точку входа в приложение
  • parsing.py: модуль с функциями для парсинга номеров телефона на сайте

Зависимости:
  • requests
  • fake_useragent

Пример использования:
import parsing
hands_url = 'https://hands.ru/company/about/'
print(parsing.get_telephone_num(hands_url))

Вывод:
https://hands.ru/company/about/
200 OK
['84951370720']

Возвращаемое значение: ['84951370720']
