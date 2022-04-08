import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as Bs

tmplNonDigLetRem = re.compile(r'[^a-zA-Zа-яёА-ЯЁ\s]')

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept': "text/html,application/xhtml+xml,application/xml;\
    q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'}

PATH_TO_CHROME_DRIVER = 'chrome_driver/chromedriver'


def get_top_from_yandex(request_str):
    # Получаем наменклатурную позицию и возвращаем лист пар: URL = описание
    result_url = []
    result_description = []
    result = []
    search_url = "https://yandex.ru/search/direct?text="
    search_url_postfix = "&filters_docs=direct_cm"
    request_str = "купить " + request_str[1:]

    raw_result = requests.get(
        search_url + request_str + search_url_postfix, headers=headers).text
    # driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    # driver.implicitly_wait(2)
    # driver.get(search_url+request_str+search_url_postfix)
    # raw_result = driver.page_source

    parsed_result = Bs(raw_result, features='lxml')

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

    # driver.close()
    return result


''''for item in ['* гайка М50']:#,'* болт М32','* манжета гост','* станок гост']:
    with open("~result.txt", "a") as result_file:
        result_file.write(json.dumps(getTopFromYandex(item),ensure_ascii=False))'''


def get_company_list_by_product_metalloprokat(product_name):
    # парсер www.metalloprokat.ru

    # target_url = 'https://www.metalloprokat.ru/company/?q='
    target_url = 'https://msk.pulscen.ru/search/price?q='

    sellers = dict()

    site_raw = requests.get(target_url + product_name, headers=headers).text
    # driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    # driver.implicitly_wait(2)
    # driver.get(target_url+product_name)
    # site_raw = driver.page_source
    parsed = Bs(site_raw, features='lxml')

    comp_count = int(parsed.find_all('div', {'class': 'hcl-tip'})[0].contents[0].split()[5])

    if comp_count < 1:
        return sellers

    companies = parsed.find_all('span', {
        'class': 'cii-pseudo-link js-ykr-action js-ga-link js-catalogue-ecommerce js-encrypted-seo-link'})

    for company in companies:
        try:
            seller_name = company.contents[0]
            sellers[seller_name] = []
            # sellers[seller_name].append(company.find_all('a')[0]['href'])
        except Exception as e:
            print(f'Ошибка: {e}')

    reviews = parsed.find_all(
        'li', {'class': 'links_comment item medium float-left clearfix'})
    for review in reviews:
        try:
            print(review.a['data-href'])
        except Exception as e:
            print(f'Ошибка: {e}')

    inn = ''
    # driver.close()
    for seller in sellers:
        try:
            # raw_for_inn = requests.get(
            #    GET_INN_URL+seller+GET_INN_URL_POSFIX, headers=headers)
            # driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
            # driver.implicitly_wait(2)
            # driver.get(GET_INN_URL+seller+' ИНН')
            # raw_for_inn = driver.page_source
            # parsed = bs(raw_for_inn, features='lxml')
            # inn = parsed.find_all('div', {'class': 'serp-list serp-list_right_yes serp-list_complementary_yes'})[
            # 0].find_all('div', {'class': 'KeyValue-ItemValue'})[0].text
            '''company = parsed.find_all('div', {'class': 'company-item'})[0]
            company_info = company.find_all(
                'div', {'class': 'company-item-info'})[1]
            inn = company_info.find_all('dd')[0].text'''
            # driver.close()
            pass
        except Exception as e:
            print(f'Ошибка: {e}')
        sellers[seller].append(inn)

    return sellers


# >>>>>>>>> парсеры тектстовй информации строк и тп


def universal_nomenclature_parcer(nomenclature_data_frame):
    # Подготовка шаблонов для разбора строк:
    #   Шаблон для "стандартов":
    pat_gost = re.compile(
        r'(ГОСТ\s?Р?\s?(?:ИСО)?\s?\d*[/]?\d*\s?(?:DIN)?\s?\d*[/]?\d*)')
    #   Шаблон для метрических параметров:
    # pat_metric_size = re.compile(r'[мМ]\d{1,}[хХ]?\d{1,}')
    #   Шаблон для текстового описания:
    pat_words = re.compile(r'((?:[A-ZА-ЯЁ]+)?[а-яa-z]{2,})')

    def compile_from_values(values):
        # Собирает строки из списка элементов
        result = None
        if values.lastindex > 0:
            prev = ''
            if result:
                prev = str(result) + ' '
            result = prev + values[0]
        return result

    def clear_from_none(value):
        if value:
            return value[5:]
        else:
            return

    nomenclature_data_frame['Стандарт'] = None

    # заполняем поле "Стандарт"
    for i in range(len(nomenclature_data_frame)):
        gosts = re.finditer(pat_gost, nomenclature_data_frame['Наименование'][i])
        for gost in gosts:
            nomenclature_data_frame['Стандарт'][i] = str(
                nomenclature_data_frame['Стандарт'][i]) + ', ' + compile_from_values(gost)
            nomenclature_data_frame['Стандарт'][i] = clear_from_none(nomenclature_data_frame['Стандарт'][i])
            if nomenclature_data_frame['Стандарт'][i][0].isdigit() or nomenclature_data_frame['Стандарт'][i][2] == " ":
                nomenclature_data_frame['Стандарт'][i] = 'ГОСТ ' + nomenclature_data_frame['Стандарт'][i]

    # заполняем поле "Чистое наименование"
    nomenclature_data_frame['Чистое наименование'] = None
    nomenclature_data_frame['Характеристики'] = None
    for i in range(len(nomenclature_data_frame)):
        # обрабатываем первый тип: "Наименование написано вот так"
        words = []
        try:
            words = re.finditer(pat_words, str(nomenclature_data_frame['Наименование'][i]).replace(
                nomenclature_data_frame['Стандарт'][i], ""))
        except Exception as e:
            print(f'Ошибка: {e}')
        # собираем строку
        for word in words:
            nomenclature_data_frame['Чистое наименование'][i] = str(
                nomenclature_data_frame['Чистое наименование'][i]) + " " + compile_from_values(word)
        # если строка собралась, нормализируем её, удаляя лишний "мусор"
        if nomenclature_data_frame['Чистое наименование'][i]:
            nomenclature_data_frame['Чистое наименование'][i] = clear_from_none(
                nomenclature_data_frame['Чистое наименование'][i])

            nomenclature_data_frame['Характеристики'][i] = str(nomenclature_data_frame['Наименование'][i][1:]).replace(
                nomenclature_data_frame['Стандарт'][i], "").replace(nomenclature_data_frame['Чистое наименование'][i],
                                                                    "")

        else:
            raw_str = nomenclature_data_frame['Наименование'][i].split(';')
            nomenclature_data_frame['Чистое наименование'][i] = raw_str[0][1:]
            try:
                for segment in raw_str[1].split(','):
                    if "СТАНДАРТ" not in segment:
                        nomenclature_data_frame['Характеристики'][i] = str(
                            nomenclature_data_frame['Характеристики'][i]) + ' ' + segment
            except Exception as e:
                print(f'Ошибка: {e}')
            nomenclature_data_frame['Характеристики'][i] = clear_from_none(nomenclature_data_frame['Характеристики'][i])

    return nomenclature_data_frame


def universal_nomenclature_parcer_no_df(nomenclature_string):
    df = pd.DataFrame(data=[nomenclature_string], columns=['Наименование'])
    result = universal_nomenclature_parcer(df)
    name = str(result['Наименование'][0])
    re.sub(tmplNonDigLetRem, '', name)
    standart = str(result['Стандарт'][0])
    category = str(result['Чистое наименование'][0])
    options = str(result['Характеристики'][0])
    return name, category, standart, options
