#from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

import pandas as pd


PATH_TO_CHROME_DRIVER = ChromeDriverManager().install()


def get_company_list_by_product_metalloprokat(product_name):
    # парсер www.metalloprokat.ru

    #TARGET_URL = 'https://www.metalloprokat.ru/company/?q='
    TARGET_URL = 'https://msk.pulscen.ru/search/price?q='

    sellers = dict()

    #site_raw = requests.get(TARGET_URL+product_name, headers=headers).text
    driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER, chrome_options=chrome_options)
    driver.implicitly_wait(2)
    driver.get(TARGET_URL+product_name)
    site_raw = driver.page_source
    parsed = bs(site_raw, features='lxml')

    comp_count = int(parsed.find_all(
        'div', {'class': 'hcl-tip'})[0].contents[0].split()[5])

    if comp_count < 1:
        return sellers

    companies = parsed.find_all('span', {
                                'class': 'cii-pseudo-link js-ykr-action js-ga-link js-catalogue-ecommerce js-encrypted-seo-link'})

    for company in companies:
        try:
            seller_name = company.contents[0]
            sellers[seller_name] = []
            # sellers[seller_name].append(company.find_all('a')[0]['href'])
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
    driver.close()
    for seller in sellers:
        try:
            # raw_for_inn = requests.get(
            #    GET_INN_URL+seller+GET_INN_URL_POSFIX, headers=headers)
            driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER, chrome_options=chrome_options)
            driver.implicitly_wait(2)
            driver.get(GET_INN_URL+seller+' ИНН')
            raw_for_inn = driver.page_source
            parsed = bs(raw_for_inn, features='lxml')
            inn = parsed.find_all('div', {'class': 'serp-list serp-list_right_yes serp-list_complementary_yes'})[
                0].find_all('div', {'class': 'KeyValue-ItemValue'})[0].text
            '''company = parsed.find_all('div', {'class': 'company-item'})[0]
            company_info = company.find_all(
                'div', {'class': 'company-item-info'})[1]
            inn = company_info.find_all('dd')[0].text'''
            driver.close()
        except:
            pass
        sellers[seller].append(inn)

    return sellers


def get_company_list_by_product(product_name):
    # базовый метод для парсинга в который добавляем спец парсеры
    sellers = get_company_list_by_product_metalloprokat(product_name)
    result = pd.DataFrame(columns=['Товар', 'Поставщик', 'ИНН'])
    for seller in sellers.keys():
        new_line = {'Товар': product_name,
                    'Поставщик': seller, 'ИНН': sellers[seller]}
        result = result.append(new_line, ignore_index=True)
    return result


# display = Display(visible=0, size=(1600, 1200))
# display.start()
print(get_company_list_by_product(
    '* Гвоздь строительный круглый головка плоская 3х80 ГОСТ 4028'))
# display.stop()
