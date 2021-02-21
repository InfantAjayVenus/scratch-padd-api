from flask import Flask, request, jsonify
from confdb import init_db
from models import Pad

app = Flask(__name__)
app.debug = True

db = init_db(app)


@app.route('/')
def index():
    return 'Online!'


@app.route('/pads', methods=['POST'])
def add_pad():
    post_data = request.get_json()
    try:
        new_pad = Pad(title=post_data["title"], content=post_data["content"])
        db.session.add(new_pad)
        db.session.commit()
        return jsonify(new_pad.id)
    except Exception:
        print(">>>>>@add_pad<<<<<\n{}".format(Exception))
        return jsonify({"error": True}), 500


@app.route('/pads', methods=['GET'])
def list_pads():
    pads_list = []
    for pad in Pad.query.all():
        pad = pad.to_json()
        pad.pop("content")
        pads_list.append(pad)

    return jsonify(pads_list)


@app.route('/pads/<id>', methods=['GET'])
def get_pad(id):
    pad = Pad.query.get(id)
    return jsonify(pad.to_json())


@app.route('/pads/<id>', methods=['PUT'])
def update_pad(id):
    data = request.get_json()
    pad = Pad.query.get(id)
    pad.content = data["content"]
    db.session.commit()
    return '', 201


@app.route('/pads/<id>', methods=['DELETE'])
def remove_pad(id):
    pad = Pad.query.get(id)
    db.session.delete(pad)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.debug = True
    app.run()
