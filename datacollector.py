from numpy import result_type
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import json
import re
import pandas as pd


PATH_TO_CHROME_DRIVER = 'chrome_driver/chromedriver'

'''def getTopFromYandex(request_str):
    # Получаем наменклатурную позицию и возвращаем лист пар: URL = описание
    result_url = []
    result_description = []
    result = []
    SEARCH_URL = "https://yandex.ru/search/direct?text="
    SEARCH_URL_POSTFIX = "&filters_docs=direct_cm"
    request_str = "купить "+request_str[1:]

    #raw_result = requests.get(
    #    SEARCH_URL+request_str+SEARCH_URL_POSTFIX, headers=headers).text
    driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    driver.implicitly_wait(2)
    driver.get(SEARCH_URL+request_str+SEARCH_URL_POSTFIX)
    raw_result = driver.page_source

    parsed_result = bs(raw_result, features='lxml')

    cards = parsed_result.find_all('li', {'class': "serp-item desktop-card"})

    for card in cards:
        links = card.find_all('a', {'target': "_blank"})
        for link in links:
            result_url.append(link.get('href'))
        descriptions = card.find_all('span', {'role': 'text'})

        for description in descriptions:
            result_description.append(description.text)

    for _ in range(min(len(result_url), len(result_description))):
        result.append([result_url[_], result_description[_]])

    driver.close()
    return result


dummy_items = list()
dummy_items.append('* Манжета М50х70 ГОСТ 22704 ')
dummy_items.append('* Манжета М65х90 ГОСТ 22704 ')
dummy_items.append('* Манжета М220х250 ГОСТ 22704 ')
dummy_items.append('* Манжета М60х80 ГОСТ 22704 ')
dummy_items.append(
    '* Манжета резиновая армированная для валов 1.2-120х150х12-1 ГОСТ 8752 ')
dummy_items.append('* Пластина техническая 2Н-I-ТМКЩ-С-4 ГОСТ 7338 ')
dummy_items.append(
    '* Рукав всасывающий В-1-75-У рабочий вакуум 0,08МПа ГОСТ 5398 ')
dummy_items.append(
    '* Рукав с текстильным каркасом В(II)-16-25-38-ХЛ ГОСТ 18698 ')
dummy_items.append('* Пластина техническая 1Н-I-ТМКЩ-С-5 ГОСТ 7338 ')
dummy_items.append(
    '* Манжета резиновая армированная для валов 1.2-90х120х12-1 ГОСТ 8752 ')
dummy_items.append('* Манжета М140х170 ГОСТ 22704 ')
dummy_items.append(
    '* Манжета резиновая армированная для валов 1.2-180х220х15-1 ГОСТ 8752 ')
dummy_items.append(
    '* Манжета резиновая армированная для валов 1.2-190х230х15-1 ГОСТ 8752 ')
dummy_items.append('* Рукав газосварочный I-6,3-0,63-У ГОСТ 9356 ')
dummy_items.append(
    '* Рукав с текстильным каркасом ВГ(III)-10-25-38-У ГОСТ 18698 ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7796, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ M20Х80, КЛАСС ПРОЧНОСТИ 6.6, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append('* Болт головка шестигранная M16х120.88 ГОСТ Р ИСО 4014 ')
dummy_items.append('* Гайка шестигранная M30.6 покрытие цинковое ГОСТ 5915 ')
dummy_items.append(
    '* Гвоздь строительный круглый головка плоская 3х80 ГОСТ 4028 ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7817 DIN609, ОБОЗНАЧЕНИЕ M36-6GХ200, КЛАСС ПРОЧНОСТИ 10.9, МАТЕРИАЛ СТАЛЬ 40Х ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7796, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ 2М10-6GХ28, КЛАСС ПРОЧНОСТИ 5.6, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append(
    '* Болт головка шестигранная M10х35.66 покрытие цинковое ГОСТ 7796 ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7817 DIN609, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ 2.M30Х100, КЛАСС ПРОЧНОСТИ 5.8, МАТЕРИАЛ СТАЛЬ ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7798 ГОСТ7805, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ 3.M12Х25, КЛАСС ПРОЧНОСТИ 5.8, МАТЕРИАЛ СТАЛЬ ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7808, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ М24Х55, КЛАСС ПРОЧНОСТИ 5.6, МАТЕРИАЛ СТАЛЬ ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7817 DIN609, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ M24Х80, КЛАСС ПРОЧНОСТИ 6.6, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append('* Гайка шестигранная M24.8 ГОСТ 5916 ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ7796, ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ 3M16Х30, КЛАСС ПРОЧНОСТИ 5.8 ')
dummy_items.append(
    '* Гайка шестигранная M30.8.35 покрытие цинковое ГОСТ 15521 ')
dummy_items.append(
    '* ГАЙКА; ТИП ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ M20, СТАНДАРТ ГОСТ15521, КЛАСС ПРОЧНОСТИ 5, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append(
    '* ГАЙКА; ОБОЗНАЧЕНИЕ M10, СТАНДАРТ ГОСТ15521, КЛАСС ПРОЧНОСТИ 5, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append(
    '* ГАЙКА; ОБОЗНАЧЕНИЕ M16, СТАНДАРТ ГОСТ15521, КЛАСС ПРОЧНОСТИ 5, МАТЕРИАЛ СТАЛЬ ОЦИНКОВАННАЯ ')
dummy_items.append(
    '* ШАЙБА; ТИП ПЛОСКАЯ УМЕНЬШЕННАЯ, СТАНДАРТ ГОСТ10450 DIN433, ОБОЗНАЧЕНИЕ А24, МАТЕРИАЛ СТАЛЬ 20 ОЦИНКОВАННАЯ ')
dummy_items.append(
    '* Гайка шестигранная M20х1,5.5 покрытие цинковое, хроматированное ГОСТ  15521 ')
dummy_items.append('* Гайка шестигранная M12.5 покрытие цинковое ГОСТ 15521 ')
dummy_items.append(
    '* Гайка шестигранная M12.8.35 покрытие цинковое ГОСТ 15521 ')
dummy_items.append('* Шайба плоская 16.32 ГОСТ 6958 ')
dummy_items.append(
    '* ГАЙКА; ОБОЗНАЧЕНИЕ М24-6Н.8.35.0112, СТАНДАРТ ГОСТ15521, КЛАСС ПРОЧНОСТИ 8, МАТЕРИАЛ СТАЛЬ 35 ОЦИНКОВАННАЯ ')
dummy_items.append('* Гайка шестигранная M42х3.8 покрытие цинковое ГОСТ 5915 ')
dummy_items.append(
    '* БОЛТ; СТАНДАРТ ГОСТ Р ИСО4014 DIN931 (ГОСТ7798/7805), ГОЛОВКА ШЕСТИГРАННАЯ, ОБОЗНАЧЕНИЕ M16Х65, КЛАСС ПРОЧНОСТИ 8.8, МАТЕРИАЛ СТАЛЬ/ ОЦИНКОВАННАЯ ')




for item in dummy_items:
    with open("~result.txt", "a") as result_file:
        result_file.write(json.dumps(getTopFromYandex(item),ensure_ascii=False))
        
'''

res = list()
with open("~result.txt", "r") as result_file:
    res = result_file.read()
    
for element in res.split('\"'):
    print(element)