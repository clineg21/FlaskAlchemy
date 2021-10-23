from flask import Blueprint
from flask_restx import Api

from apis.dataLoad import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)

api.add_namespace(ns1)