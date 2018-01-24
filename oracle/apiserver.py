import auxiliary
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
import json
import model
from model import Refer, Subscription
import flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import requests

app = Flask(__name__, template_folder='')
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SECRET_KEY'] = 'postgres'
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)

os_tools = auxiliary.ostools()
session = os_tools.db_connection()
refer_handler = auxiliary.refer_handler()
subscription_handler = auxiliary.subscription_handler()

@app.teardown_request
def app_teardown(response_or_exc):
    session.remove()
    return response_or_exc

@app.route('/<string:pubkey>', methods=['GET', 'POST'])
@cross_origin()
def refer(pubkey):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        account = request.form['account']
        refer = refer_handler.consult_or_create(session, pubkey)
        subscription = subscription_handler.create_subscription(session, pubkey, account)
        return "200"

