from flask import request, jsonify
from config import app, db
from models import Pad



@app.route('/')
def index():
    return 'Online!'


@app.route('/pads', methods=['POST'])
def add_pad(): 
    try:
        post_data = request.json
        new_pad = Pad(title=post_data["title"], content=post_data["content"])
        db.session.add(new_pad)
        db.session.commit()
        return jsonify(new_pad.id)
    except Exception as e:
        print(">>>>>@add_pad<<<<<")
        print(e.args)
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
    if "content" in data:
        pad.content = data["content"]

    if "title" in data:
        pad.title = data["title"]

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
