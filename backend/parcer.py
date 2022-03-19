from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import json

PATH_TO_CHROME_DRIVER = 'chrome_driver/chromedriver'

def getTopFromYandex(request_str):
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



'''for item in ['* гайка М50']:#,'* болт М32','* манжета гост','* станок гост']:
    with open("~result.txt", "a") as result_file:
        result_file.write(json.dumps(getTopFromYandex(item),ensure_ascii=False))'''