from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Version 1 of the API
class ResourceV1(Resource):
    def get(self):
        return {'data': 'This is version 1'}

api.add_resource(ResourceV1, '/api/v1/resource')

# Version 2 of the API
class ResourceV2(Resource):
    def get(self):
        return {'data': 'This is version 2'}

api.add_resource(ResourceV2, '/api/v2/resource')

if __name__ == '__main__':
    app.run(debug=True)
