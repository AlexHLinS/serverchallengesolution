import sqlite3
import parcer
import dummy_items
import json


def create_db_from_scratch():
    # Создает базу
    sqlite_connection = None
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def execute_sql_query(sql_request):
    # Выполняет SQL запрос без возврата результата, использется для добавления/удаления чего-либо
    sqlite_connection = None
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def execute_sql_query_with_answer(sql_request):
    # Выполняет SQL запрос с возвратом результата,
    # использется для получения чего-либо из базы
    result = None
    sqlite_connection = None
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return result


def put_dummy_values():
    # заполняем тестовыми значениями
    try:
        # таблица категорий номенклатуры
        for item in dummy_items.categories.keys():
            add_nomenclature_categories(dummy_items.categories[item])

        for item in dummy_items.num_items:
            add_nom_item(item[0], item[1])

        new_items = dummy_items.dummy_items

        for item in new_items:
            name, category, standart, options = parcer.universal_nomenclature_parcer_no_df(item)
            add_nom_item(name, category)

        for inn in dummy_items.suppliers.keys():
            add_supplier(inn, dummy_items.suppliers[inn])

        for pair in dummy_items.pair:
            execute_sql_query(
                f'''INSERT or IGNORE INTO sc_numenclature_supplier \
                (numenclature_id, supplier_inn) VALUES ({pair[0]}, \'{pair[1]}\');''')
    except Exception as e:
        print(f'Произошла ошибка при создании демо значений в таблицах: {e}')


def create_tables_from_scratch():
    try:
        # таблица категорий номенклатуры
        execute_sql_query('''CREATE TABLE sc_numenclature_categories (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT type UNIQUE NOT NULL);''')
        # таблица позиций номенклатуры
        execute_sql_query('''CREATE TABLE sc_numenclature_items (
                                    id INTEGER PRIMARY KEY,
                                    label TEXT  UNIQUE NOT NULL,
                                    activeSuppliers INTEGER,
                                    reliableSuppliers INTEGER,
                                    unverifiedSuppliers INTEGER,
                                    unreliableSupplier INTEGER,
                                    category_id INTEGER);''')
        # таблица связи постащик-номенклатура
        execute_sql_query('''CREATE TABLE sc_numenclature_supplier (
                                    numenclature_id INTEGER  NOT NULL,
                                    supplier_inn TEXT  NOT NULL);''')
        # таблица поставщиков
        execute_sql_query('''CREATE TABLE sc_suppliers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    inn TEXT UNIQUE NOT NULL,
                                    contacts TEXT,
                                    status INTEGER,
                                    capitalization INTEGER,
                                    created_at TEXT,
                                    debet INTEGER,
                                    credit INTEGER);''')
    except Exception as e:
        print(f'Произошла ошибка при создании структур таблицы: {e}')


###
# функции записи и извлечения данных из таблиц
###


def get_numenclature_category_name_from_id(category_id):
    # получает наименование категории по индитификатору
    # ввиду того что поле с ID ключевое и не повторяется,
    # в случае нахождения результата вып
    result = None
    sqlite_connection = None
    try:
        sql_request = str(
            'SELECT title FROM sc_numenclature_categories WHERE id=' + str(category_id))
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
        if result:
            return str(result[0][0])
    return result


def add_nomenclature_categories(cat_name):
    # добавляет запись в таблицу с категориями, если таковой там нет
    category_id = -1
    sqlite_connection = None
    try:
        # добавляем
        sql_request = str(
            'INSERT or IGNORE INTO sc_numenclature_categories (title) VALUES (\'' + str(cat_name) + '\')')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sql_request)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        cursor.close()
        # получаем присвоенный ключ
        sql_request = str(
            'SELECT id FROM sc_numenclature_categories WHERE title=\'' + str(cat_name) + '\'')
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return category_id


def add_supplier(supplier_inn, supplier_name):
    supplier_id = -1
    sqlite_connection = None
    try:
        # добавляем поставщика
        sql_request = str(
            'INSERT or IGNORE INTO sc_suppliers (name, inn) VALUES (\'' + str(supplier_name) + '\',\'' + str(
                supplier_inn) + '\')')
        sqlite_connection = sqlite3.connect('sqlite_sc.db')
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sql_request)
        sqlite_connection.commit()
        print(f"Запрос:\n{sql_request}\n к SQLite выполнен")
        cursor.close()

        # получаем присвоенный ID
        sql_request = str(
            'SELECT id FROM sc_suppliers WHERE inn=\'' + str(supplier_inn) + '\'')
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return supplier_id


def add_nom_item(item_name, category_name):
    sqlite_connection = None
    try:
        # добавляем категорию
        category_id = add_nomenclature_categories(category_name)
        # добавляем номенклатурную позицию
        sql_request = str(
            'INSERT or IGNORE INTO sc_numenclature_items (label, category_id) VALUES (\'' + str(
                item_name) + '\',\'' + str(category_id) + '\')')
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
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    pass


def get_all_categories():
    return execute_sql_query_with_answer('SELECT * FROM sc_numenclature_categories')


def get_all_items():
    return execute_sql_query_with_answer('SELECT * FROM sc_numenclature_items')


def get_suppliers_from_nomenclature_id(nomenclature_id):
    inns = execute_sql_query_with_answer(
        f'SELECT supplier_inn FROM sc_numenclature_supplier WHERE numenclature_id={nomenclature_id}')
    print(inns)
    result = []
    for inn in inns:
        try:
            suplier_data = execute_sql_query_with_answer(
                f'SELECT * FROM sc_suppliers WHERE inn={inn[0]}')[0]
            result.append({'name': suplier_data[1], 'inn': suplier_data[2], 'contacts': suplier_data[3],
                           'status': suplier_data[4],
                           'capitalization': suplier_data[5], 'created_at': suplier_data[6], 'debet': suplier_data[7],
                           'credit': suplier_data[8]})
        except Exception as e:
            print(f'Произошла ошибка: {e}')
            pass
    return result


def get_statistics_data():
    items_count = execute_sql_query_with_answer(
        'SELECT COUNT(label) FROM sc_numenclature_items')[0][0]
    urls_count = items_count
    direct_suppliers = None
    markeplaces = None
    trash_urls = None
    suppliers = execute_sql_query_with_answer('SELECT COUNT(name) FROM sc_suppliers')[0][0]
    suppliers_active = execute_sql_query_with_answer(
        'SELECT COUNT(id) FROM sc_suppliers WHERE status is \'ACTIVE\'')[0][0]
    result = {'items_count': items_count,
              'urls_count': urls_count,
              'direct_suppliers': direct_suppliers,
              'markeplaces': markeplaces,
              'trash_urls': trash_urls,
              'suppliers': suppliers,
              "suppliers_active": suppliers_active}
    return json.dumps(result, ensure_ascii=False)
