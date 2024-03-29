import db_worker
import parcer
import server
import tools

is_run_independently = False


# загрузка токена для работы с API сервиса dadata, должен находится
# в соответствующем файле
def init_ddata_token():
    return tools.get_param_from_file_environ(None, 'dadata.token', 'dadata_token')


# функция возвращает ИНН организации по совпадению
# наименования, https://github.com/hflabs/dadata-py#suggest-company 
# возвращается первая компания в выдаче
def get_inn_from_name(name):
    dadata = init_ddata_token()
    result = None
    if dadata:
        result = dadata.suggest("party", name)
        try:
            result = result[0]['data']['inn']
        except KeyError:
            pass
    return result


# функция возвращает информацию об организации по её ИНН
# https://github.com/hflabs/dadata-py#find-company-by-inn
def data_from_inn(inn):
    dadata = init_ddata_token()
    result = dadata.find_by_id("party", query=inn, count=1)
    return result


# функция обогощения данных, запускается периодически на базу
# производит оценку наличия отсутсвия записей для конкретного
# поставщика в базе, если что-то отсутвует - дополняет данные
def update_suppliers_data():
    global is_run_independently
    if not is_run_independently:
        server.is_new_item_added = True
    # содержится только наименование
    names_inn_less = db_worker.execute_sql_query_with_answer(
        'SELECT name FROM sc_suppliers WHERE inn is NULL')
    for name in names_inn_less:
        get_inn_from_name(name)
        pass  # заглушка на период отладки

    # содержится наименование и ИНН, но нет контактных данных
    inn_contacts_less = db_worker.execute_sql_query_with_answer(
        'SELECT inn FROM sc_suppliers WHERE contacts is NULL')
    for inn in inn_contacts_less:
        if inn[0] == 'None':
            continue
        supplier_data = data_from_inn(inn[0])
        full_name = supplier_data[0]['unrestricted_value']
        status = supplier_data[0]['data']['state']['status']
        address = supplier_data[0]['data']['address']['unrestricted_value']
        created_at = supplier_data[0]['data']['state']['actuality_date']
        db_feedback = db_worker.execute_sql_query(
            f'UPDATE sc_suppliers SET name=\'{full_name}\',\
             status=\'{status}\', contacts=\'{address}\',\
              created_at=\'{created_at}\' WHERE inn = {inn[0]};')

    pass  # заглушка на период отладки


def update_suppliers_list():
    # получаем индитификаторы товаров из базы
    # поставщик по которым еще не найден
    goods_ids = db_worker.execute_sql_query_with_answer(
        'SELECT label FROM sc_numenclature_items\
         WHERE id NOT IN (SELECT numenclature_id FROM sc_numenclature_supplier)')

    # производим поиск поставщиков и добавляем их наименования в базу
    results = []
    for good_id in goods_ids:
        # список поставщиков
        results = list(parcer.get_company_list_by_product_metalloprokat(good_id[0]).keys())
        # получаем id товара, поставщиков которого нашли ранее
        try:
            item_id = db_worker.execute_sql_query_with_answer(
                f'SELECT id FROM sc_numenclature_items WHERE label = \'{good_id[0]}\'')
        except Exception as e:
            print(f'Ошибка: {e}')
            continue
        # заносим пары [id товара:ИНН поставщика] в базу
        for result in results:
            # получаем ИНН из наименования поставщика
            inn = get_inn_from_name(result)
            if inn is None:
                continue
            # добавляем его в базу
            sid = db_worker.add_supplier(inn, result)
            db_worker.execute_sql_query(
                f'''INSERT or IGNORE INTO sc_numenclature_supplier \
                (numenclature_id, supplier_inn) VALUES ({item_id[0][0]}, \'{inn}\');''')

    if not is_run_independently:
        server.is_new_item_added = False
    pass  # заглушка на период отладки


def main():
    global is_run_independently
    is_run_independently = True
    update_suppliers_list()
    update_suppliers_data()
    pass


if __name__ == "__main__":
    main()
