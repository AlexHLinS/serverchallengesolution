from flask import Flask, render_template, jsonify, request
import supplier_search

app = Flask(__name__)

@app.route('/')
# Возвращаем стартовую страницу
def main():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def getItems():
    if request.method == 'GET':
        # Выдача списка позиций для таблицы на стартовм экране
        return jsonify(supplier_search.getStartScreenData())
    if request.method == 'POST':
        # Поиск конкретной позиции
        item_name = request.POST.get('search')
        return jsonify(supplier_search.getItemByName(item_name))

@app.route('/api/suppliers',methods=['GET'])
# Выдача информации по конкретной позиции
def getItem():
    item = request.args.get('item')
    print(item)
    return jsonify(supplier_search.getNomenclatureFromId(item))




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