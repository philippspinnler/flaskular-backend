from flask import Flask, abort, request, jsonify
from app.data import product_mock, product_category_mock
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/products", methods=['GET'])
def products():
    category = request.args.get('category')
    if category:
        return jsonify({'products': product_mock.objects(category=category)})
    return jsonify({'products': product_mock.objects()})

@app.route("/products/<code>", methods=['GET'])
def product(code):
    product = product_mock.objects(code=code)
    if product is None:
        abort(404)
    return jsonify(product)

@app.route("/productcategories", methods=['GET'])
def productcategories():
    return jsonify({'productcategories': product_category_mock.objects()})

@app.route("/productcategories/<id>", methods=['GET'])
def productcategory(id):
    product_category = product_category_mock.objects(id=id)
    if product_category is None:
        abort(404)
    return jsonify(product_category)

if __name__ == "__main__":
    app.run()
