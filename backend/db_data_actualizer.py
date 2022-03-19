from audioop import add
from unittest import result
import requests
from dadata import Dadata
import db_worker


def initDdataToken():
    with open('dadata.token') as dadatatokenfile:
        token = dadatatokenfile.read()
    return Dadata(token)


def getInnFromName(name):
    dadata = initDdataToken()
    result = dadata.suggest("party", query=name, count=1)
    return result


def dataFromInn(inn):
    dadata = initDdataToken()
    result = dadata.find_by_id("party", query=inn, count=1)
    return result

# TODO: алгоритм обогощения данными поставщиков: если у поставщика поля пусты - обогощаем


def updateSuppliersData():
    # у которых есть только наименование но нет инн
    names_inn_less = db_worker.executeSQLQueryWithAnswer(
        'SELECT name FROM sc_suppliers WHERE inn is NULL')
    for name in names_inn_less:
        # getInnFromName(name)
        pass
    # у которых нет контактных данных
    inn_contacts_less = db_worker.executeSQLQueryWithAnswer(
        'SELECT inn FROM sc_suppliers WHERE contacts is NULL')
    for inn in inn_contacts_less:
        supplier_data = dataFromInn(inn[0])
        full_name = supplier_data[0]['unrestricted_value']
        status = supplier_data[0]['data']['state']['status']
        address = supplier_data[0]['data']['address']['unrestricted_value']
        created_at = supplier_data[0]['data']['state']['actuality_date']
        db_feedback = db_worker.executeSQLQuery(
            f'UPDATE sc_suppliers SET name=\'{full_name}\', status=\'{status}\', contacts=\'{address}\', created_at=\'{created_at}\' WHERE inn = {inn[0]};')

    pass


# TODO: алгоритм поиска поставщиков: если в поставщик/товар нет товара - ищем поставщиков

def updateSuppliersList():
    goods_ids = db_worker.executeSQLQueryWithAnswer(
        'SELECT label FROM sc_numenclature_items WHERE id NOT IN (SELECT numenclature_id FROM sc_numenclature_supplier)')
    
    


updateSuppliersList()