from flask import Flask
from valve.rcon import *

app = Flask(__name__)

valve.rcon.execute(("85.10.205.252",27015),"password","")
mongodb+srv://tomandb:$MONGODBPASSWORD@toman-cluster.m5fe4.mongodb.net/$DBNAME?retryWrites=true&w=majority

@app.route('/')
def hello():
    return 


if __name__ == '__main__':
    app.run()

