from flask import Flask
from valve.rcon import *

app = Flask(__name__)

valve.rcon.execute(("85.10.205.252",27015),"password","")

@app.route('/')
def hello():
    return 


if __name__ == '__main__':
    app.run()

