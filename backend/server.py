from flask import Flask, render_template, request, send_from_directory
import supplier_search
import db_data_actualizer
import db_worker
import tools

is_new_item_added = False  # тригер необходимости обновления данных в базе

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # избавляемся от ASCII кодов вместо кирилицы

# Для возможности использования "из вне"
CORS_HEADER = {'Access-Control-Allow-Origin': '*'}


@app.route('/')
# Возвращаем стартовую страницу
def main():
    return render_template('index.html')


@app.route('/api/item', methods=['GET'])
# Поиск конкретной позиции и добавление её на экран
def get_new_item():
    item_name = request.args.get('search')
    print(f'looking for {item_name}')
    response = supplier_search.getItemByName(item_name)
    return response, 200, CORS_HEADER


@app.route('/api/items', methods=['GET'])
# Выдача списка позиций для таблицы на стартовм экране
def get_items():
    response = supplier_search.getStartScreenData()
    return response, 200, CORS_HEADER


@app.route('/api/statistics', methods=['GET'])
# Статистические данные
def get_statistics():
    response = db_worker.getStatisticsData()
    return response, 200, CORS_HEADER


@app.route('/api/suppliers', methods=['GET'])
# Выдача информации по конкретной позиции
def get_item():
    item = request.args.get('item')
    print(item)
    response = supplier_search.getSuppliersListFromNomenclatureId(item)
    return response, 200, CORS_HEADER


@app.route('/api/update_db')
# Запрос на обновление данных в базе
def update_db():
    if is_new_item_added:
        db_data_actualizer.updateSuppliersData()
        db_data_actualizer.updateSuppliersList()
    return render_template('index.html')


################################
# Выдача файлов для фронтА:
@app.route("/asset-manifest.json")
def get_front_asset_manifest():
    return send_from_directory('templates', 'asset-manifest.json')


@app.route("/favicon.ico")
def get_front_favicon():
    return send_from_directory('templates', 'favicon.ico')


@app.route("/logo192.png")
def get_front_logo192():
    return send_from_directory('templates', 'logo192.png')


@app.route("/logo512.png")
def get_front_logo512():
    return send_from_directory('templates', 'logo512.png')


@app.route("/manifest.json")
def get_front_manifest():
    return send_from_directory('templates', 'manifest.json')


@app.route("/robots.txt")
def get_front_robots():
    return send_from_directory('templates', 'robots.txt')


@app.route('/test_status')
# Тест-заглушка
def test_status():
    return "app is runing!"


################################

if __name__ == '__main__':
    if tools.get_file_existing_status('sqlite_sc.db'):
        pass
    else:
        # TODO: implement empty db creations
        print('db not found')
    # trying to get port
    port = int(tools.get_param_from_file_environ(5000, 'port.token', 'server_web_app_port'))

    app.run(host='0.0.0.0', port=port)
