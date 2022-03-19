import json
import db_worker
import parcer

def getStartScreenData():
    # получаем все категории
    cat = db_worker.getAllCategories()
    # получаем все позиции номенклатуры
    raw = db_worker.getAllItems()
    
    result = list()
    for element in cat:
        result.append({'id':element[0], 'items':[], 'title':element[1]})
    
    items = dict()
    for data in raw:
        s = {'id': data[0], 'label': data[1], 'activeSuppliers': data[2],
                      'reliableSuppliers': data[3], 'unverifiedSuppliers': data[4], 'unreliableSupplier': data[5]}
        if items.get(data[6]):
            tmp = []
            tmp = items[data[6]]
            tmp.append(s)
            items[data[6]] = tmp
        else:
            items[data[6]] = s
        
    for i in range(len(result)):
        result[i]['items'].append(items[result[i]['id']])
    return json.dumps({'categories':result}, ensure_ascii=False)


def getNomenclatureFromId(id):
    
    test_json_text = {'id': id, 'label': "Манжета М50х70 ГОСТ 22704", 'activeSuppliers': 11,
                      'reliableSuppliers': 3, 'unverifiedSuppliers': 6, 'unreliableSupplier': 2}
    return json.dumps(test_json_text, ensure_ascii=False)


def getItemByName(itemName):
    # получаем запрос и обновляем данные 
    
    # распаршиваем наименование
    name, category, standart, options =  parcer.universalNomenclatureParcerNoDF(itemName)
    db_worker.addNumItem(name, category)
    return getStartScreenData()

def getSuppliersListFromNomenclatureId(nomenclatureId):
    test_json_text = db_worker.getSuppliersFromNomenclatureId(nomenclatureId)
    return json.dumps(test_json_text, ensure_ascii=False)