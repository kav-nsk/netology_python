import requests

def translate_it(params):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    response = requests.get(url, params).json()
    return ' '.join(response.get('text', []))

def dialog():
    print('Для выхода из программы введите -1')
    pathInpFile = input('Введите путь к файлу текста который нужно перевести: ')
    pathOutFile = input('Введите путь к файлу c результатами: ')
    fromLang = input('С какого языка выполнить перевод (de, es, fr)? ')
    toLang = input('На какой язык перевести (ru по умолчанию) ')
    if toLang == '': toLang = 'ru'
    output = [pathInpFile, pathOutFile, fromLang, toLang]
    if '-1' in output: return -1
    else: return output

key = 'trnsl.1.1.20181204T022829Z.6d7fcaca429bc040.4ec4e6b7c8c4ec3381ca1b024a06c3e3bb199217'
print('Программа "Переводчик файлов"')
print('Переведено сервисом «Яндекс.Переводчик» http://translate.yandex.ru/')
p = dialog()
while p != -1:
    inpFile = open(p[0])
    outFile = open(p[1], 'w')
    params = dict(key=key, lang=p[2] + '-' + p[3], text=inpFile.read())
    translateText = translate_it(params)
    outFile.write(translateText)
    outFile.close()
    p = dialog()
