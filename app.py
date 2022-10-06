# import one function from dbhelpers to use
# connecting to database
# getting the result or runnung the stored procedure
# closing the connection
from dbhelpers import conn_exe_close
# import flask library
from flask import Flask, request
# import json to send results as a string
import json

app = Flask(__name__)

# to run the main statement from dbhelpers
# it will need the stored procedure and list of arguments
def get_display_results(statement,params_list):
    # execute the function imported from dbhelpers and store the result
    results = conn_exe_close(statement,params_list)
    # result will be stored in list form
    # if result is not there then it will show an error msg 
    if(type(results) == list):
        if(len(results) > 0):
            results_json = json.dumps(results, default=str)
            return results_json
        elif(len(results) == 0):
            return 'there are 0 results matched the data provided'
        # if not a list then probably error will be in a form of string
    elif(type(results) == str):
        return results
        # for further error handling will rely on else
    else:
        return 'Sorry, An error occured'

# it will get all the available items without any params
@app.get('/api/items')
def all_items_info():
    results_json  = get_display_results('call all_items_info()',[])
    return results_json

# it will post the new item to the items table in database
# it will take 3 arguments and put the values into the table
@app.post('/api/items')
def add_new_item():
    name = request.json.get('name')
    description = request.json.get('description')
    in_stock_quantity = request.json.get('in_stock_quantity')
    results_json = get_display_results('call add_new_item(?,?,?)',[name,description,in_stock_quantity])
    return results_json

# it will update the existing value for quantity of an item by taking id and value for quantity
@app.patch('/api/items')
def update_quantity_item():
    id = request.json.get('id')
    add_quantity = request.json.get('add_quantity')
    results_json = get_display_results('call update_quantity_item(?,?)',[id,add_quantity])
    return results_json

# it will delete the entire item from table by just taking id
@app.delete('/api/items')
def delete_item():
    id = request.json.get('id')
    results_json = get_display_results('call delete_item(?)',[id])
    if(results_json[0][0]):
        return 'Deleted successfully'

# it will get the specific employee from the table by just taking id as a param
@app.get('/api/employee')
def specific_employee():
    id = request.json.get('id')
    results_json = get_display_results('call specific_employee(?)',[id])
    return results_json

# it will add the employee and return the details of an employee 
#  will require 3 different data from the user
@app.post('/api/employee')
def add_employee():
    name = request.json.get('name')
    position = request.json.get('position')
    hourly_wage = request.json.get('hourly_wage')
    results_json = get_display_results('call add_employee(?,?,?)',[name,position,hourly_wage])
    return results_json

# will update the wage of an employee by just taking id and hourly new wage 
# and it will replace the original wage to a new wage
@app.patch('/api/employee')
def update_employee_wage():
    id = request.json.get('id')
    hourly_wage = request.json.get('hourly_wage')
    results_json = get_display_results('call update_employee_Wage(?,?)',[id,hourly_wage])
    return results_json

# it will delete the employee if an id of an employee is given as a data
@app.delete('/api/employee')
def delete_employee():
    id = request.json.get('id')
    results_json =  get_display_results('call delete_employee(?)',[id])
    if(results_json[0][0]):
        return 'Deleted successfully'


app.run(debug=True)
