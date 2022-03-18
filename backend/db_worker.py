import sqlite3

# функции создания и выполнения запросов не предусматривающих извлечение данных


def createDBFromScratch():
    # Создает базу
    try:
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def executeSQLQuery(sql_request):
    # Выполняет SQL запрос без возврата результата, использется для добавления/удаления чего-либо
    try:
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        sqlite_create_table_query = sql_request

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def createTablesFromScratch():
    try:
        # таблица категорий номенклатуры
        executeSQLQuery('''CREATE TABLE sc_numenclature_categories (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT type UNIQUE NOT NULL);''')
        # таблица позиций номенклатуры
        executeSQLQuery('''CREATE TABLE sc_numenclature_items (
                                    id INTEGER PRIMARY KEY,
                                    label TEXT  UNIQUE NOT NULL,
                                    activeSuppliers INTEGER,
                                    reliableSuppliers INTEGER,
                                    unverifiedSuppliers INTEGER,
                                    unreliableSupplier INTEGER,
                                    category_id INTEGER);''')

    except:
        print('Произошла ошибка при создании структур таблицы')

###
# функции записи и извлечения данных из таблиц
###


def getNumenclatureCategoryNameFromId(id):
    # получает наименование категории по индитификатору
    # ввиду того что поле с ID ключевое и не повторяется,
    # в случае нахождения результата вып
    try:
        result = None
        sql_request = str('SELECT title FROM sc_numenclature_categories WHERE id='+str(id))
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        sqlite_create_table_query = sql_request

        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        result = cursor.fetchall()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        print(f'Результат {result}')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
        if result:
            return str(result[0][0])
        else:
            return
    pass


def addNumenclatureCategories(cat_name):
    # добавляет запись в таблицу с категориями, если таковой там нет
    try:
        sql_request = str(
            'INSERT or IGNORE INTO sc_numenclature_categories (title) VALUES (\''+str(cat_name)+'\')')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sql_request)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    pass

