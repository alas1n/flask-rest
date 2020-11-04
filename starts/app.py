from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "My store Store",
        "items": [
            {
                "name": "item 1",
                "price": 500
            },
            {
                "name": "item 2",
                "price": 600
            },
            {
                "name": "item 3",
                "price": 200
            }
        ]
    },
    {
        "name": "My store Store2",
        "items": [
            {
                "name": "item 21",
                "price": 2500
            },
            {
                "name": "item 22",
                "price": 2600
            },
            {
                "name": "item 23",
                "price": 2200
            }
        ]
    },
    {
        "name": "My store Store3",
        "items": [
            {
                "name": "item 31",
                "price": 3500
            },
            {
                "name": "item 32",
                "price": 3600
            },
            {
                "name": "item 33",
                "price": 3200
            }
        ]
    },
    {
        "name": "My store Store4",
        "items": [
            {
                "name": "item 41",
                "price": 4500
            },
            {
                "name": "item 42",
                "price": 4600
            },
            {
                "name": "item 43",
                "price": 4200
            }
        ]
    }

]


# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name}
# "http://127.0.0.1:5000/store/some_name"

@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})

# POST /store/<string:name>/item {name:, price:}


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price'],
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "there is no store"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_itmes_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "there is no item nor store"})


@app.route('/')  # 'https://www.google.com/'
def home():
    return render_template('index.html')


app.run(port=5000)
