#!/udr/bin/en python

import pprint
import hashlib
import pymongo

from flask import Flask, jsonify, abort, url_for, request, make_response

import savedb

pp = pprint.PrettyPrinter()
app = Flask(__name__)


@app.route('/api/signup', methods=['POST', 'GET'])
def signup():
    """
        name,
        pass,
        isAdmin,
        org
    """
    if "application/json" in request.headers["Content-Type"]:
        token = savedb.signup(request.json)
        if token == None:
            return jsonify({'token':''}), 400
        else:
            return jsonify({'token': token}), 201
    return jsonify({'token': ''}), 400

@app.route('/api/login', methods=['POST', 'GET'])
def login():
    """
        _id,
        pass
    """
    if "application/json" in request.headers["Content-Type"]:
        log_result = savedb.login(request.json)
        if log_result == 0:
            return jsonify({'loggedIn':False})
        else:
            return jsonify({'loggedIn':True})
        #return jsonify({'token': token}), 201
    return jsonify({'token': ''}), 400


@app.route('/api/items', methods=['POST', 'GET'])
def set_items():
    """
        _id,
        food:[{skksdkfkhfd:skajfl}, {fdjkgbdkhkdfh}]
    """
    if "application/json" in request.headers["Content-Type"]:
        log_result = savedb.insert_items(request.json)
    
    return jsonify({'insertion_status':'complete'}) , 200


@app.route('/')
def index():
    return 'API home page'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

