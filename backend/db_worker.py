import sqlite3

import dummy_items

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


def executeSQLQueryWithAnswer(sql_request):
    # Выполняет SQL запрос с возвратом результата,
    # использется для получения чего-либо из базы
    result = None
    try:
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        sqlite_create_table_query = sql_request
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        result = cursor.fetchall()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        print(f'Результат запроса: {result}')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return result


def putDummyValues():
    # заполняем тестовыми значениями
    try:
        # таблица категорий номенклатуры
        for item in dummy_items.categories.keys():
            addNumenclatureCategories(dummy_items.categories[item])
        for item in dummy_items.num_items:
            addNumItem(item[0], item[1])
        for inn in dummy_items.suppliers.keys():
            addSupplier(inn, dummy_items.suppliers[inn])
        for pair in dummy_items.pair:
            executeSQLQuery(
                f'''INSERT or IGNORE INTO sc_numenclature_supplier (numenclature_id, supplier_inn) VALUES ({pair[0]}, \'{pair[1]}\');''')
    except:
        print('Произошла ошибка при создании демо значений в таблицах')


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
        # таблица связи постащик-номенклатура
        executeSQLQuery('''CREATE TABLE sc_numenclature_supplier (
                                    numenclature_id INTEGER  NOT NULL,
                                    supplier_inn TEXT  NOT NULL);''')
        # таблица поставщиков
        executeSQLQuery('''CREATE TABLE sc_suppliers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    inn TEXT UNIQUE NOT NULL,
                                    contacts TEXT,
                                    status INTEGER,
                                    capitalization INTEGER,
                                    created_at TEXT,
                                    debet INTEGER,
                                    credit INTEGER);''')
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
        sql_request = str(
            'SELECT title FROM sc_numenclature_categories WHERE id='+str(id))
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
    category_id = -1
    try:
        # добавляем
        sql_request = str(
            'INSERT or IGNORE INTO sc_numenclature_categories (title) VALUES (\''+str(cat_name)+'\')')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sql_request)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        cursor.close()
        # получаем присвоенный ключ
        sql_request = str(
            'SELECT id FROM sc_numenclature_categories WHERE title=\''+str(cat_name)+'\'')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        sqlite_create_table_query = sql_request
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        category_id = int(cursor.fetchall()[0][0])
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        print(f'Присвоенный ID {category_id}')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return category_id


def addSupplier(supplier_inn, supplier_name):
    supplier_id = -1
    try:
        # добавляем поставщика
        sql_request = str(
            'INSERT or IGNORE INTO sc_suppliers (name, inn) VALUES (\''+str(supplier_name)+'\',\''+str(supplier_inn)+'\')')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sql_request)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        cursor.close()

        # получаем присвоенный ID
        sql_request = str(
            'SELECT id FROM sc_suppliers WHERE inn=\''+str(supplier_inn)+'\'')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        sqlite_create_table_query = sql_request
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        supplier_id = int(cursor.fetchall()[0][0])
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        print(f'Присвоенный ID {supplier_id}')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return supplier_id


def addNumItem(item_name, category_name):
    try:
        # добавляем категорию
        category_id = addNumenclatureCategories(category_name)
        # добавляем номенклатурную позицию
        sql_request = str(
            'INSERT or IGNORE INTO sc_numenclature_items (label, category_id) VALUES (\''+str(item_name)+'\',\''+str(category_id)+'\')')
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


def getAllCategories():
    return executeSQLQueryWithAnswer('SELECT * FROM sc_numenclature_categories')


def getAllItems():
    return executeSQLQueryWithAnswer('SELECT * FROM sc_numenclature_items')


def getSuppliersFromNomenclatureId(nomenclatureId):
    inns = executeSQLQueryWithAnswer(
        f'SELECT supplier_inn FROM sc_numenclature_supplier WHERE numenclature_id={nomenclatureId}')
    print(inns)
    result = []
    for inn in inns:
        suplier_data = executeSQLQueryWithAnswer(
            f'SELECT * FROM sc_suppliers WHERE inn={inn[0]}')[0]
        result.append({'name': suplier_data[1], 'inn': suplier_data[2], 'contacts': suplier_data[3], 'status': suplier_data[4],
                       'capitalization': suplier_data[5], 'created_at': suplier_data[6], 'debet': suplier_data[7], 'credit': suplier_data[8]})
    return result
