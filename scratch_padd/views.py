from flask import Blueprint, request, jsonify, abort, flash
from . import db
from .models import Pad

padds = Blueprint('padds', __name__)


@padds.route('/')
def index():
    return 'Online!'


@padds.route('/pads', methods=['POST'])
def add_pad(): 
    error_code = 500
    error_message = ""
    try:
        post_data = request.json
        if 'title' not in post_data and 'content' not in post_data:
            error_code = 400
            error_message = "Data must have both 'title' and 'content' parameters"
            abort(error_code, error_message)
        new_pad = Pad(title=post_data["title"], content=post_data["content"])
        db.session.add(new_pad)
        db.session.commit()
        return jsonify(new_pad.id)
    except Exception as e:
        print(">>>>>@add_pad<<<<<")
        print(e.args)
        abort(error_code, error_message)


@padds.route('/pads', methods=['GET'])
def list_pads():
    try:
        return jsonify([{'id': id, 'title': title} for id, title in db.session.query(Pad.id, Pad.title).all()])
    
    except Exception as error:
        print('>>>>>>@list_pads<<<<<<<<>')
        print(error.args)
        abort(error_code, error_message)


@padds.route('/pads/<id>', methods=['GET'])
def get_pad(id):
    error_code = 500
    error_message = ""
    try:
        pad = Pad.query.get(id)
        if not pad:
            error_code = 404
            error_message = "Pad does not exist"
            flash(error_message)
            abort(error_code, error_message)
        return jsonify(pad.to_json())

    except Exception as error:
        print('>>>>>>>@get_pad<<<<<<<<>')
        print(error.args)
        abort(error_code, error_message)
    

@padds.route('/pads/<id>', methods=['PUT'])
def update_pad(id):
    error_code = 500
    error_message = ""
    try:
        data = request.get_json()

        if 'title' not in data or 'content' not in data:
            error_code = 400
            error_message = "Update should pass either 'title' or 'contet' property"
            abort(error_code, error_message)
        pad = Pad.query.get(id)
        if not pad:
            error_code = 404
            error_message = "Pad does not exist to update"
            abort(error_code, error_message)
        if "content" in data:
            pad.content = data["content"]

        if "title" in data:
            pad.title = data["title"]

        db.session.commit()
        return jsonify(True), 201
    except Exception as error:
        print('>>>>>>>>@update_pad<<<<<<<<<>')
        print(error.args)
        abort(error_code, error_message)


@padds.route('/pads/<id>', methods=['DELETE'])
def remove_pad(id):
    error_code = 500
    error_message = ""
    try:
        pad = Pad.query.get(id)
        if not pad:
            error_code = 404
            error_message = "Pad does not exist"
            abort(error_code, error_message)
        db.session.delete(pad)
        db.session.commit()
        return '', 204
    except Exception as error:
        print('>>>>>>@remove_pad<<<<<<<<>')
        print(error.args)
        abort(error_code, error_message)

