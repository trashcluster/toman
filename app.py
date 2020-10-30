from flask import Flask, request
from flask_restful import Resource, Api
#from valve.rcon import *
import pymongo
import dns
import os
import sys

#Init Flask App
app = Flask(__name__)
#Init Flask-restful api
api=Api(app)

try:  
   os.environ['MONGODBURL']
   MongoDbAccessLink = os.getenv('MONGODBURL')
except KeyError: 
   print ("ERROR, Please pass MongoDB full url in the system environment variables")
   sys.exit(1)


#Init mongodb connection to database
mogodbclient = pymongo.MongoClient(MongoDbAccessLink)
#Init database "tomandb" on "atlasclient"
db = mogodbclient.tomandb

#valve.rcon.execute(("85.10.205.252",27015),"password","help")

################################## USER MANAGMENT ####################################

# Init User collection/table
# print("init UserCol")
# UserCol = db.UserCol
# print("insert data in userCol")
# dict = { "USER": "TESTUSER" , "HAHA": "PROMP" }
# print(dict)
# x = UserCol.insert_one(dict).inserted_id
# print( "id", x )
# for x in UserCol.find():
#     print(x)

#Create a user, no right managment implemented for now.
# UserCreate endpoint
class UserCreate(Resource):
    # GET request, doe snot perform any actions
    def get(self):
        return {'403 error': 'use this endpoint to create a user, send a put request'}, 403

    # PUT request, create a user entry in the database
    def put(self):
        putdata = request.form['username']
        #x = UserCol.insert_one(putdata).inserted_id
        print(x)
        #return {'userid' : x, 'username' : putdata}, 200
        return {'userid' : 'YEET', 'username' : putdata}, 200

class UserList(Resource):
    def get(self):
        return {UserCol.find()}, 200


api.add_resource(UserCreate, '/api/v1/user/create')
api.add_resource(UserList, '/api/v1/user/list')

if __name__ == '__main__':
    app.run()