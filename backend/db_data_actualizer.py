from dadata import Dadata
import db_worker
import parcer
import server

is_run_independently = False

# загрузка токена для работы с API сервиса dadata, должен находится
# в соответствующем файле
def initDdataToken():
    with open('dadata.token') as dadatatokenfile:
        token = dadatatokenfile.read()
    return Dadata(token)


# функция возвращает ИНН организации по совпадению
# наименования, https://github.com/hflabs/dadata-py#suggest-company 
# возвращается первая компания в выдаче
def getInnFromName(name):
    dadata = initDdataToken()
    result = dadata.suggest("party", name)
    try:
        result = result[0]['data']['inn']
    except:
        result = None
    return result


# функция возвращает информацию об организации по её ИНН
# https://github.com/hflabs/dadata-py#find-company-by-inn
def dataFromInn(inn):
    dadata = initDdataToken()
    result = dadata.find_by_id("party", query=inn, count=1)
    return result


# функция обогощения данных, запускается периодически на базу
# производит оценку наличия отсутсвия записей для конкретного
# поставщика в базе, если что-то отсутвует - дополняет данные
def updateSuppliersData():
    global is_run_independently
    if not is_run_independently:
        server.is_new_item_added = True
    # содержится только наименование
    names_inn_less = db_worker.executeSQLQueryWithAnswer(
        'SELECT name FROM sc_suppliers WHERE inn is NULL')
    for name in names_inn_less:
        getInnFromName(name)
        pass  # заглушка на период отладки

    # содержится наименование и ИНН, но нет контактных данных
    inn_contacts_less = db_worker.executeSQLQueryWithAnswer(
        'SELECT inn FROM sc_suppliers WHERE contacts is NULL')
    for inn in inn_contacts_less:
        if inn[0] == 'None':
            continue
        supplier_data = dataFromInn(inn[0])
        full_name = supplier_data[0]['unrestricted_value']
        status = supplier_data[0]['data']['state']['status']
        address = supplier_data[0]['data']['address']['unrestricted_value']
        created_at = supplier_data[0]['data']['state']['actuality_date']
        db_feedback = db_worker.executeSQLQuery(
            f'UPDATE sc_suppliers SET name=\'{full_name}\', status=\'{status}\', contacts=\'{address}\', created_at=\'{created_at}\' WHERE inn = {inn[0]};')

    pass  # заглушка на период отладки


def updateSuppliersList():
    # получаем индитификаторы товаров из базы
    # поставщик по которым еще не найден
    goods_ids = db_worker.executeSQLQueryWithAnswer(
        'SELECT label FROM sc_numenclature_items WHERE id NOT IN (SELECT numenclature_id FROM sc_numenclature_supplier)')

    # производим поиск поставщиков и добавляем их наименования в базу
    results = []
    for id in goods_ids:
        # список поставщиков
        results = list(parcer.get_company_list_by_product_metalloprokat(id[0]).keys())
        # получаем id товара, поставщиков которого нашли ранее
        try:
            item_id = db_worker.executeSQLQueryWithAnswer(
                f'SELECT id FROM sc_numenclature_items WHERE label = \'{id[0]}\'')
        except:
            continue
        # заносим пары [id товара:ИНН поставщика] в базу
        for result in results:
            # получаем ИНН из наименования поставщика
            inn = getInnFromName(result)
            if inn == None:
                continue
            # добавляем его в базу
            sid = db_worker.addSupplier(inn, result)
            db_worker.executeSQLQuery(
                f'''INSERT or IGNORE INTO sc_numenclature_supplier \
                (numenclature_id, supplier_inn) VALUES ({item_id[0][0]}, \'{inn}\');''')

    if not is_run_independently:
        server.is_new_item_added = False
    pass  # заглушка на период отладки


def main():
    global is_run_independently
    is_run_independently = True
    updateSuppliersList()
    updateSuppliersData()
    pass


if __name__ == "__main__":
    main()
