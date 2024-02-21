import requests as req
import re
from fake_useragent import UserAgent


def formatting_number(tel: str) -> str:
    if len(tel) == 7:
        return f'8495{tel[1:]}'
    else:
        return f'8{tel[1:]}'


def find_tel_numbers(text: str) -> list[str]:
    """
    Извлекает и форматирует номера телефона из текста.
    Параметры:
    - text (str): Текст, в котором осуществляется поиск номеров телефона.
    Возвращает:
    - List[str]: Список отформатированных номеров телефона.
    """
    res = []
    # поиск последовательности цифр, перед которыми не стоит буква, цифра и "."
    # и начинающихся с цифры 7 или 8, длинною не менее 7 знаков
    potential_numbers = re.findall(r"(?<![\.\w])[7|8][0-9 ()-]{7,}", text)
    for num in potential_numbers:
        tel = re.sub(r'\D', '', num)
        if (len(tel) == 8 or len(tel) == 11) and (tel not in res):
            res.append(tel)
    for i in range(len(res)):
        res[i] = formatting_number(res[i])
    return res


def get_telephone_num(url: str) -> list[str]:
    """
    Получает и форматирует номера телефона с веб-страницы.
    Параметры:
    - url (str): URL веб-страницы, с которой нужно извлечь номера телефона.
    Возвращает:
    - List[str]: Список отформатированных номеров телефона.
    """
    headers = {
        'User-Agent': UserAgent().random
    }
    print(url)
    try:
        res = req.get(url, headers=headers)
        print(res.status_code, res.reason)
    except req.exceptions.RequestException as e:
        print("Something went wrong during the request:", e)
        return []

    telephons = find_tel_numbers(res.text)
    return telephons
