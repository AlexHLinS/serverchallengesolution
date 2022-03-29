from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import json
import re
import pandas as pd
import requests

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           'connection': 'keep-alive',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'none',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1'}

PATH_TO_CHROME_DRIVER = 'chrome_driver/chromedriver'

def getTopFromYandex(request_str):
    # Получаем наменклатурную позицию и возвращаем лист пар: URL = описание
    result_url = []
    result_description = []
    result = []
    SEARCH_URL = "https://yandex.ru/search/direct?text="
    SEARCH_URL_POSTFIX = "&filters_docs=direct_cm"
    request_str = "купить "+request_str[1:]

    raw_result = requests.get(
        SEARCH_URL+request_str+SEARCH_URL_POSTFIX, headers=headers).text
    #driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    #driver.implicitly_wait(2)
    #driver.get(SEARCH_URL+request_str+SEARCH_URL_POSTFIX)
    #raw_result = driver.page_source

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

    #driver.close()
    return result



''''for item in ['* гайка М50']:#,'* болт М32','* манжета гост','* станок гост']:
    with open("~result.txt", "a") as result_file:
        result_file.write(json.dumps(getTopFromYandex(item),ensure_ascii=False))'''
        


def get_company_list_by_product_metalloprokat(product_name):
    # парсер www.metalloprokat.ru

    #TARGET_URL = 'https://www.metalloprokat.ru/company/?q='
    TARGET_URL = 'https://msk.pulscen.ru/search/price?q='

    sellers = dict()

    site_raw = requests.get(TARGET_URL+product_name, headers=headers).text
    #driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    #driver.implicitly_wait(2)
    #driver.get(TARGET_URL+product_name)
    #site_raw = driver.page_source
    parsed = bs(site_raw, features='lxml')
    
    comp_count = int(parsed.find_all('div', {'class': 'hcl-tip'})[0].contents[0].split()[5])

    if comp_count < 1:
        return sellers

    companies = parsed.find_all('span', {'class': 'cii-pseudo-link js-ykr-action js-ga-link js-catalogue-ecommerce js-encrypted-seo-link'})

    for company in companies:
        try:
            seller_name = company.contents[0]
            sellers[seller_name] = []
            #sellers[seller_name].append(company.find_all('a')[0]['href'])
        except:
            pass

    reviews = parsed.find_all(
        'li', {'class': 'links_comment item medium float-left clearfix'})
    for review in reviews:
        try:
            print(review.a['data-href'])
        except:
            pass

    inn = ''
    #driver.close()
    for seller in sellers:
        try:
            #raw_for_inn = requests.get(
            #    GET_INN_URL+seller+GET_INN_URL_POSFIX, headers=headers)
            #driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
            #driver.implicitly_wait(2)
            #driver.get(GET_INN_URL+seller+' ИНН')
            #raw_for_inn = driver.page_source
            #parsed = bs(raw_for_inn, features='lxml')
            #inn = parsed.find_all('div', {'class': 'serp-list serp-list_right_yes serp-list_complementary_yes'})[
            #0].find_all('div', {'class': 'KeyValue-ItemValue'})[0].text
            '''company = parsed.find_all('div', {'class': 'company-item'})[0]
            company_info = company.find_all(
                'div', {'class': 'company-item-info'})[1]
            inn = company_info.find_all('dd')[0].text'''
            #driver.close()
            pass
        except:
            pass
        sellers[seller].append(inn)

    return sellers
        
        
        
############## парсеры тектстовй информации строк и тп


def universalNomenclatureParcer(NomenclatureDataFrame):
    # Подготовка шаблонов для разбора строк:
    #   Шаблон для "стандартов":
    patGOST = re.compile(
        r'(ГОСТ\s?Р?\s?(?:ИСО)?\s?\d*[\/]?\d*\s?(?:DIN)?\s?\d*[\/]?\d*)')
    #   Шаблон для метрических параметров:
    patMetricSize = re.compile(r'[мМ]\d{1,}[хХ]?\d{1,}')
    #   Шаблон для текстового описания:
    patWords = re.compile(r'((?:[A-ZА-Я]{1,})?[а-яa-z]{2,})')

    
    def compileFromValues(values):
        # Собирает строки из списка элементов
        result = None
        if values.lastindex > 0:
            prev = ''
            if result:
                prev = result+' '
            result = prev + values[0]
        return result

    def clearFromNone(value):
        if value:
            return value[5:]
        else:
            return

    NomenclatureDataFrame['Стандарт'] = None

    # заполняем поле "Стандарт"
    for i in range(len(NomenclatureDataFrame)):
        gosts = re.finditer(patGOST, NomenclatureDataFrame['Наименование'][i])
        for gost in gosts:
            NomenclatureDataFrame['Стандарт'][i] = str(
                NomenclatureDataFrame['Стандарт'][i]) + ', '+compileFromValues(gost)
            NomenclatureDataFrame['Стандарт'][i] = clearFromNone(NomenclatureDataFrame['Стандарт'][i])
            if NomenclatureDataFrame['Стандарт'][i][0].isdigit() or NomenclatureDataFrame['Стандарт'][i][2] == " ":
                NomenclatureDataFrame['Стандарт'][i] = 'ГОСТ '+NomenclatureDataFrame['Стандарт'][i]


    # заполняем поле "Чистое наименование"
    NomenclatureDataFrame['Чистое наименование'] = None
    NomenclatureDataFrame['Характеристики'] = None
    for i in range(len(NomenclatureDataFrame)):
        # обрабатываем первый тип: "Наименование написано вот так"
        words = []
        try:
            words = re.finditer(patWords, str(NomenclatureDataFrame['Наименование'][i]).replace(
                NomenclatureDataFrame['Стандарт'][i], ""))
        except:
            pass
        # собираем строку
        for word in words:
            NomenclatureDataFrame['Чистое наименование'][i] = str(
                NomenclatureDataFrame['Чистое наименование'][i])+" " + compileFromValues(word)
        # если строка собралась, нормализируем её, удаляя лишний "мусор"
        if NomenclatureDataFrame['Чистое наименование'][i]:
            NomenclatureDataFrame['Чистое наименование'][i] = clearFromNone(
                NomenclatureDataFrame['Чистое наименование'][i])

            NomenclatureDataFrame['Характеристики'][i] = str(NomenclatureDataFrame['Наименование'][i][1:]).replace(
                NomenclatureDataFrame['Стандарт'][i], "").replace(NomenclatureDataFrame['Чистое наименование'][i], "")

        else:
            raw_str = NomenclatureDataFrame['Наименование'][i].split(';')
            NomenclatureDataFrame['Чистое наименование'][i] = raw_str[0][1:]
            try:
                for segment in raw_str[1].split(','):
                    if "СТАНДАРТ" not in segment:
                        NomenclatureDataFrame['Характеристики'][i] = str(NomenclatureDataFrame['Характеристики'][i])+' '+segment
            except:
                pass
            NomenclatureDataFrame['Характеристики'][i] = clearFromNone(NomenclatureDataFrame['Характеристики'][i])

    return NomenclatureDataFrame


def universalNomenclatureParcerNoDF(nomenclature_string):
    df = pd.DataFrame(data = [nomenclature_string], columns = ['Наименование'])
    result = universalNomenclatureParcer(df)
    name = str(result['Наименование'][0]).replace(r'[^a-zA-Zа-яёА-ЯЁ\s]','')
    standart = str(result['Стандарт'][0])
    category = str(result['Чистое наименование'][0])
    options = str(result['Характеристики'][0])    
    return name, category, standart, options
    
