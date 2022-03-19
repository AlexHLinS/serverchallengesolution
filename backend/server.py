from flask import Flask, render_template, jsonify, request, send_from_directory
import supplier_search
import db_data_actualizer

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS_HEADER = {'Access-Control-Allow-Origin': '*'}


@app.route('/')
# Возвращаем стартовую страницу
def main()
    db_data_actualizer.updateSuppliersList()
    return render_template('index.html')


@app.route('/api/items', methods=['GET'])
def getItems():
    # Выдача списка позиций для таблицы на стартовм экране
    response = supplier_search.getStartScreenData()
    return response, 200, CORS_HEADER
        
@app.route('/api/item', methods=['GET'])
def getNewItem():
    # Поиск конкретной позиции и добавление её на экран
    item_name = request.args.get('search')
    print(f'looking for {item_name}')
    response = supplier_search.getItemByName(item_name)
    return response, 200, CORS_HEADER

@app.route("/manifest.json")
def manifest():
    return send_from_directory('templates', 'manifest.json')


@app.route("/logo192.png")
def logo192():
    return send_from_directory('templates', 'logo192.png')


@app.route('/api/suppliers', methods=['GET'])
# Выдача информации по конкретной позиции
def getItem():
    item = request.args.get('item')
    print(item)
    response = supplier_search.getSuppliersListFromNomenclatureId(item)
    return response, 200, CORS_HEADER


@app.route('/test_status')
# Тест-заглушка
def test_status():
    return "app started!"


if __name__ == '__main__':
    port = 0
    try:
        # для тестового запуска настройки порта в port.token
        with open('backend/port.token', 'r') as portinfofile:
            port = int(portinfofile.read())
    except:
        # на проде 5000 порт
        port = 5000
    print(port)
    app.run(host='0.0.0.0', port=port)
