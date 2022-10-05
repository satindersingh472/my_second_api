from dbhelpers import conn_exe_close
from flask import Flask, request
import json

app = Flask(__name__)

def get_display_results(statement,params_list):
    results = conn_exe_close(statement,params_list)
    if(type(results) == list):
        results_json = json.dumps(results, default=str)
        return results_json
    elif(type(results) == str):
        return results
    else:
        return 'Sorry, An error occured'


@app.get('/api/items')
def all_items_info():
    results_json  = get_display_results('call all_items_info()',[])
    return results_json

all_items_info()

@app.post('/api/items')
def add_new_item():
    name = request.json.get('name')
    description = request.json.get('description')
    in_stock_quantity = request.json.get('in_stock_quantity')
    results_json = get_display_results('call add_new_item(?,?,?)',[name,description,in_stock_quantity])
    return results_json

@app.patch('/api/items')
def update_quantity_item():
    id = request.json.get('id')
    add_quantity = request.json.get('add_quantity')
    results_json = get_display_results('call update_quantity_item(?,?)',[id,add_quantity])
    return results_json

@app.delete('/api/items')
def delete_item():
    id = request.json.get('id')
    results_json = get_display_results('call delete_item(?)',[id])
    return results_json


app.run(debug=True)
