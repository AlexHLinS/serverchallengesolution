# serverchallengesolution

Pre selection solving task

https://russianhackers.notion.site/3-19969e7826384c9da9915f8e8298915a#2845327c68994bf9aba31cd4f3f69769

# Life demo (развернуто на Raspberry pi)

http://93.157.254.203:7778/

>>>>>>> 8117b6dd787012351d768094b94e103966fe8547
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>

# Презентация нашего решения

[Открыть PDF](presentation/Ezee_case_3_var5.pdf)


# В настоящее время система развернута на Raspberry Pi, поэтому некоторые компоненты не доступны онлайн, они работают на локальной машине, просто клонировать


### Реализация сбора (парсинга) данных

В связи с повсеместным распостранением систем защиты от автоматизированного сбора данных, для взаимодействия с поисковыми системами и торговыми площадками используется фреймворк Selenium, позволяющий как существенно повысить качество сбора информации, так и исключить риск DDoS атаки в случае какого-либо сбоя (см. юридические риски презентации).

К сожалению, апаратные возможности Raspberry Pi, а также ограниченное время, не позволили в полной мере реализовать функцианал сетевого сбора первичных данных  (номенклатура - наименование поставщика), однако функционал обогощения данных с уровня "только наименования юридического лица" до подноценного масштабируемого набора, позволяющего обеспечить функционал предлагаемых ML моделей, доступен в полном объеме.


### Ранжирование поставщиков с помощью глубокого обучения

В директории `company_ranker` находится jupyter блокнот с обучением ML алгоритма по ранжированию данных. Строится и обучается lgbm модель.

### Классификация сайтов

В директории `marketplace_manufacturer_classification` находится jupyter блокнот с классификацией сайтов на "Маркетплейс"-"Сайт" и "Производитель"-"Перекуп". Строится и обучается BERT модели с классификационной надстройкой.



### Структура

В связи со спецификой мероприятия, репозиторий содержит ряд избыточных модулей, которые не нужны при комплектации финального релиза. Для удобства навигации предлагаем следующую дорожную карту:

* директория **backend** - реализация связки backend+frontend продукта:

  * **chrome_driver** директория с драйвером Selenuim для работы с браузером Chrome
  * **static** - статические данные frontend'a
  * **templates** - контент frontend'a
  * **create_db_from_scratch.py** - скрипт генерации базы данных SQLlite с функционалом заполнения базовыми демонстрационными данными, которые в последствии обогощаются алгоритмами
  * **dummy_items.py** - демонстрационные данные для базы данных SQLlite и скрипта create_db_from_scratch.py
  * **db_worker.py** - модуль реализующий методы работы с базой данных
  * **parcer.py** - модуль содержащий алгоритмы парсинга (web, строки и т.п.)
  * **supplier_search.py** - логика по обработке данных поставщиков
  * **db_data_actualizer.py** - модуль который запускается по распиисанию и в фоновом режиме производит обогощение данных
  * **server.py** - основной исполняемый файл web приложения
* **chrome_driver** директория с драйвером Selenuim для работы с браузером Chrome, необходимый для работы Jypiter Notebook'ов
* **company_ranker** - содержит Jypiter Notebook c реализацией ML модели ранжирования компаний, а также данные полученные в результате её обучения
* **marketplace_manufacturer_classification** - содержит Jypiter Notebook c реализацией ML модели ранжирования сайтов на категории "поставщик/агрегатор/мусор", а также данные полученные в результате её обучения.
* **task3** данные полученные от организаторов хакатона, а также их производные, изготовленные в процессе проверки гипотез
* **Ezee_task3_solution.ipynb** - Jypiter Notebook с концепциями и гипотезами, на основании которой ведется разработка системы
* **Ezee_task3_solution.py** - отладочный вариант в виде скрипта
* **metaDataAnalyse.ipynb** - Jypiter Notebook с концепциями и гипотезами сбора метаданных
* **проверка_гипотиз_парсинг.ipynb** - Jypiter Notebook с концепциями и гипотезами обогощения данных

Остальные файлы несут второстепенный смысл, но могут быть использованы как рабочие черновики.

В настоящий момент команда прилагает все усилия для реализации максимального функционала до начала презентации.
