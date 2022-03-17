import json

def getStartScreenData():
    test_json_text = {'categories':[{'id':0,'title':"Название категории - Манжеты",'items':[{'id':0,'label':"Манжета М50х70 ГОСТ 22704",'activeSuppliers':11,'reliableSuppliers':3,'unverifiedSuppliers':6,'unreliableSupplier':2,},{'id':1,'label':"Манжета М50х70 ГОСТ 22706",'activeSuppliers':6,'reliableSuppliers':1,'unverifiedSuppliers':3,'unreliableSupplier':2,}]},{'id':1,'title':"Название категории - Болты",'items':[{'id':3,'label':"Болт М50х70 ГОСТ 61204",'activeSuppliers':5,'reliableSuppliers':1,'unverifiedSuppliers':2,'unreliableSupplier':2}]}]}
    return json.dumps(test_json_text)

def getNomenclatureFromId(id):
    test_json_text = {'id':0,'label':"Манжета М50х70 ГОСТ 22704",'activeSuppliers':11,'reliableSuppliers':3,'unverifiedSuppliers':6,'unreliableSupplier':2}
    return json.dumps(test_json_text)

def getItemByName(itemName):
    test_json_text = {itemName:""}
    return json.dumps(test_json_text)


