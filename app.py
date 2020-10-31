from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with
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

### Def Database column
UserCol = db.UserCol

### Def user fields
user_fields = {
    'user_id': fields.Integer,          # user ID
    'user_firstname': fields.String,         # First Name
    'user_name': fields.String,              # Name
    'user_fullname': fields.String,          # Full Name of the user, can be different than the name + firstname 
    'user_pseudoname': fields.String,        # Pseudonym, can be canged by the user
    'user_org_id': fields.Integer,              ## Org ID
    'user_role_id': fields.Integer,             ## Role ID, whole server 
    'user_date_updated': fields.DateTime(dt_format='rfc822'),
}

### Def permissions
perm_fields = {
    'perm_id': fields.Integer,              # permission ID
    'perm_name': fields.String,             # permission name eg. Admin, Guest, Group creator
    'edit_user_name': fields.Boolean,
    'edit_user_firstname': fields.Boolean,
    'edit_user_fullname': fields.Boolean,
    'edit_user_pseudoname': fields.Boolean,
    'edit_user_org': fields.Boolean,
    'edit_user_role': fields.Boolean,
}

### Def Org
org_fields = {
    'org_id': fields.Integer,
    'org_name': fields.String,
    'org_date_updated': fields.DateTime(dt_format='rfc822'),
}

### Def Role
role_fields = {
    
}


#Create a user, no right managment implemented for now.
# UserCreate endpoint
class UserCreate(Resource):
    # GET request, does not perform any actions
    def get(self):
        return {'405 error': 'use this endpoint to create a user, send a put request'}, 405

    # PUT request, create a user entry in the database
    def put(self):
        putdata = request.form['username']
        userid = UserCol.insert_one(putdata).inserted_id
        print(userid)
        #return {'userid' : x, 'username' : putdata}, 200
        return {'userid' : 'YEET', 'username' : putdata}, 200
    
class UserEdit(Resource):
    def get(self):
        userinfo

class UserList(Resource):
    def get(self):
        return {UserCol.find()}, 200


api.add_resource(UserCreate, '/api/v1/user/create')
api.add_resource(UserList, '/api/v1/user/list')

if __name__ == '__main__':
    app.run()