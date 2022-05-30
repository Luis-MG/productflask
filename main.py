from flask import Flask, render_template, request, json
from product import product

prod = product()


app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():

    return render_template('main.html', title='Home')


@app.route('/all', methods=['GET', 'POST'])
def show_products():
    data = prod.list_products()
    return {'data': data}


@app.route('/product/')
@app.route('/product/<id>')
def detail(id=None):

    if id == None:
        return "<b>Producto no encontrado</b>"
    else:
        product = next(
            (product for product in prod.list_products() if product['id'] == int(id)), False)
        if product is False:
            return "<b>Producto no encontrado</b>"
        else:
            return render_template('detail.html', title='Details', detail=product)


@app.route('/add/')
def add():
    increment_code = int(prod.list_products()[-1]['id']) + 1
    return render_template('add.html', title='Add', code=increment_code)


@app.route('/add/commit', methods=['GET', 'POST'])
def commit_add():
    data_json = request.get_json()
    id = int(data_json['id'])
    nombre = data_json['nombre']
    marca = data_json['marca']
    precio = float(data_json['precio'])
    prod.add_product(id, nombre, marca, precio)
    return {'response': 'saved', 'code': 200}


@app.route('/buscar/')
@app.route('/buscar/<patron>')
def buscar(patron=''):
    data = prod.search_pattern(patron)
    return {'data': data}


@app.route('/del/')
@app.route('/del/<id>')
def delete(id=None):
    if id == None:
        return "<b>Producto no encontrado</b>"
    else:
        product = next(
            (product for product in prod.list_products() if product['id'] == int(id)), False)
        if product is False:
            return "<b>Producto no encontrado</b>"
        else:
            prod.del_product(id)
            return {'response': 'deleted', 'code': 200}


app.run(host="0.0.0.0", port=5000, debug=True)
