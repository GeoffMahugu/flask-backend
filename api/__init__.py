from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

import config
from pprint import pprint

api = Api(prefix=config.API_PREFIX)
parser = reqparse.RequestParser()


#  NOTE: Remove the print and test API's Once Done

class TestGetAPI(Resource):
    def get(self):
        return {'You are task home': 'API 1 Done'}, 201


class TestPostAPI(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        json_data['message'] = 'Data has been processed'
        return json_data, 201


# ENDPOINTS

# Test GET Api
api.add_resource(TestGetAPI, '/test-get')

# Test Post Api
api.add_resource(TestPostAPI, '/test-post')
