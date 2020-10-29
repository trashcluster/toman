from flask import Flask
from flask_restful import Resource, Api
import valve.rcon

app = Flask(__name__)

valve.rcon.execute(("85.10.205.252",27015),"password","help")

@app.route('/')
def hello():
    return 


if __name__ == '__main__':
    app.run()

