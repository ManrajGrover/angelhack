#!/udr/bin/en python
import json
import pprint
import hashlib
import pymongo

from flask import Flask, jsonify, abort, url_for, request, make_response

import savedb

pp = pprint.PrettyPrinter()
app = Flask(__name__)



from flask import current_app, abort, jsonify
from datetime import timedelta
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
        max_age=21600, attach_to_all=True,
        automatic_options=True):
  if methods is not None:
    methods = ', '.join(sorted(x.upper() for x in methods))
  if headers is not None and not isinstance(headers, basestring):
    headers = ', '.join(x.upper() for x in headers)
  if not isinstance(origin, basestring):
    origin = ', '.join(origin)
  if isinstance(max_age, timedelta):
    max_age = max_age.total_seconds()

  def get_methods():
    if methods is not None:
      return methods

    options_resp = current_app.make_default_options_response()
    return options_resp.headers['allow']

  def decorator(f):
    def wrapped_function(*args, **kwargs):
      if automatic_options and request.method == 'OPTIONS':
        resp = current_app.make_default_options_response()
      else:
        resp = make_response(f(*args, **kwargs))
      if not attach_to_all and request.method != 'OPTIONS':
        return resp

      h = resp.headers

      h['Access-Control-Allow-Origin'] = origin
      h['Access-Control-Allow-Methods'] = get_methods()
      h['Access-Control-Max-Age'] = str(max_age)
      if headers is not None:
        h['Access-Control-Allow-Headers'] = headers
      return resp

    f.provide_automatic_options = False
    return update_wrapper(wrapped_function, f)
  return decorator




@app.route('/api/signup', methods=['POST', 'GET'])
@crossdomain(origin='*')
def signup():
    """
        name,
        pass,
        isAdmin,
        org,
        email
    """
    if "application/json" in request.headers["Content-Type"]:
        token = savedb.signup(request.json)
        if token == None:
            return jsonify({'token':''}), 400
        else:
            return jsonify({'token': token}), 201
    return jsonify({'token': ''}), 400

@app.route('/api/login', methods=['POST', 'GET'])
@crossdomain(origin='*')
def login():
    """
        _id,
        pass
    """
    # return 'd'
    #print 'Data' + request.data
    data = json.loads(request.data)
    # if "application/json" in request.headers["Content-Type"]:
    #log_result = savedb.login(request.json)
    log_result = savedb.login(data)
    if log_result == 0:
        return jsonify({'loggedIn':False})
    else:
        return jsonify({'loggedIn':True,'token': log_result })
    #return jsonify({'token': token}), 201
    # return jsonify({'token': ''}), 400


@app.route('/api/items', methods=['POST', 'GET'])
@crossdomain(origin='*')
def set_items():
    """
        _id,
        food:[{skksdkfkhfd:skajfl}, {fdjkgbdkhkdfh}]
    """
    data=json.loads(request.data)
    print "in set items"
    log_result = savedb.insert_items(data)
    
    return jsonify({'insertion_status':'complete'}) , 200


@app.route('/')
@crossdomain(origin='*')
def index():
    return 'API home page'

if __name__ == '__main__':
    app.run()
