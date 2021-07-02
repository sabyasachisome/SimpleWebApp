from flask import Flask, request, jsonify

app= Flask(__name__)

stores= [
    {
        'name': 'beautiful store',
        'items': [
            {
        'name': 'flowers',
        'price': 100
        }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 120
            }
        ]
    }
]
    
@app.route('/')
def home():
    return 'hey'

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name==store['name']:
            return store['name']
    return 'Store name not found'

@app.route('/store/<string:name>/items')
def get_store_items(name):
    for store in stores:
        if name==store['name']:
            return jsonify(store['items'])
    return 'Store name not found'

@app.route('/store', methods=['POST'])
def create_store():
    req_data= request.get_json()
    new_store={
        'name':req_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    for store in stores:
        if name==store['name']:
            req_data= request.get_json()
            print(req_data) 
            new_item= {
                'name':req_data['name'],
                'price': req_data['price']
            }
            store['name'].append(new_item)
            return jsonify(new_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
