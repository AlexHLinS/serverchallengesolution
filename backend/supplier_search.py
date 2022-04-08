import json
import db_worker
import parcer


def get_start_screen_data():
    # получаем все категории
    cat = db_worker.get_all_categories()
    # получаем все позиции номенклатуры
    raw = db_worker.get_all_items()

    result = list()
    for element in cat:
        result.append({'id': element[0], 'items': [], 'title': element[1]})

    items = dict()
    for data in raw:
        s = {'id': data[0], 'label': data[1], 'activeSuppliers': data[2],
             'reliableSuppliers': data[3], 'unverifiedSuppliers': data[4], 'unreliableSupplier': data[5]}
        if items.get(data[6]):
            tmp = list(items[data[6]])
            tmp.append(s)
            if s['id']:
                continue
            items[data[6]] = tmp
        else:
            items[data[6]] = s

    for i in range(len(result)):
        result[i]['items'].append(items[result[i]['id']])
    return json.dumps({'categories': result}, ensure_ascii=False)


def get_nomenclature_from_id(nomenclature_id):
    test_json_text = {'id': nomenclature_id, 'label': "Манжета М50х70 ГОСТ 22704", 'activeSuppliers': 11,
                      'reliableSuppliers': 3, 'unverifiedSuppliers': 6, 'unreliableSupplier': 2}
    return json.dumps(test_json_text, ensure_ascii=False)


def get_item_by_name(item_name):
    # распаршиваем наименование
    name, category, standart, options = parcer.universal_nomenclature_parcer_no_df(item_name)
    db_worker.add_nom_item(name, category)
    return get_start_screen_data()


def get_suppliers_list_from_nomenclature_id(nomenclature_id):
    test_json_text = db_worker.get_suppliers_from_nomenclature_id(nomenclature_id)
    return json.dumps(test_json_text, ensure_ascii=False)
