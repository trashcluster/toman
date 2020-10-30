from flask import Flask
from flask_restful import Resource, Api
import valve.rcon

app = Flask(__name__)
api=Api(app)

valve.rcon.execute(("85.10.205.252",27015),"password","help")

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()

