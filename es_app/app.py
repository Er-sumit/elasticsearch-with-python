from flask import Flask, request
from flask.helpers import make_response
from flask.json import jsonify
from User import *
from Wallet import *

myapp = Flask(__name__)

#error handler method
@myapp.errorhandler(404)
def do_when_404(error):
    return (make_response('The page you are look for is not available, pls try / or /employee. <br></br> The error is: +'+str(error),404))

#home page - hello world
@myapp.route("/", methods=['GET'])
def home():
    return('Hello World')

@myapp.route("/user", methods=['GET','POST'])
def user_api():
    if request.method == 'GET':
        users = User()
        response = users.get_users()
        return(make_response(jsonify(response),200))
    elif request.method == 'POST':
        request_body = request.json
        if request_body is not None:
            new_user = User()
            response = new_user.create(**request_body)
            return(make_response(jsonify(response),201))
        else:
            return(make_response('request body not provided', 400))
    else:
        return (make_response('invalid method called',400))

@myapp.route("/wallet", methods=['GET', 'POST'])
def wallet_api():
    if request.method == "GET":
        return ("dnd")
    elif request.method == "POST":
        request_body = request.json
        if request_body is None:
            return (make_response("input data not provided", 400))
        else:
            new_wallet = Wallet()
            response = new_wallet.create(**request_body)
            if response.get('request_status') == 'success':
                response.pop("request_status")
                return(make_response(jsonify(response)), 201)
            else:
                response.pop("request_status")
                return(make_response(jsonify(response)), 400)
myapp.run(port=4040, debug=True)