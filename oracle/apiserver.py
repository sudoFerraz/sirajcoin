import auxiliary
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
import json
import model
from model import Refer, Subscribe
import flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import requests
