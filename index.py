from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Online!'

@app.route('/pads', methods=['POST'])
def add_pad():
    return 'id'

@app.route('/pads', methods=['GET'])
def list_pads():
    return jsonify(list())

@app.route('/pads/<id>', methods=['GET'])
def get_pad(pad_id):
    return jsonify(dict())

@app.route('/pads/<id>', methods=['PUT'])
def update_pad(pad_id):
    return jsonify(dict())

@app.route('/pads/<id>', methods=['DELETE'])
def remove_pad(pad_id):
    return 'Success'


if __name__ == '__main__':
    app.debug = True
    app.run()
