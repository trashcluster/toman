from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with
#from valve.rcon import *
import pymongo
import dns
import os
import sys
from email.utils import formatdate
import time

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
#db = mogodbclient.tomandb

#valve.rcon.execute(("85.10.205.252",27015),"password","help")

################################## USER MANAGMENT ####################################

# Init User collection/table
# print("init UserCol")
# UserCol = db.UserCol
# print("insert data in userCol")
# dict = { "USER": "TESTUSER" , "HAHA": "PROMP" }
# print(dict)
# 
# print( "id", x )
# for x in UserCol.find():
#     print(x)

### Def Database column
#UserCol = db.UserCol

### Def user fields
user_fields = {
    'user_id': fields.Integer,                  # user ID
    'user_firstname': fields.String,            # First Name
    'user_name': fields.String,                 # Name
    'user_fullname': fields.String,             # Full Name of the user, can be different than the name + firstname 
    'user_pseudoname': fields.String,           # Pseudonym, can be canged by the user
    'user_org_id': fields.Integer(default=0),   ## Org ID member
    'user_role_id': fields.Integer(default=0),  ## Role ID, whole server role
    'user_date_updated': fields.DateTime(dt_format='rfc822', default=formatdate(time.time())),
}

### Def Org
org_fields = {
    'org_id': fields.Integer,
    'org_name': fields.String,
    'org_members': fields.List,
    'org_owner': fields.Integer,
    'org_date_updated': fields.DateTime(dt_format='rfc822'),
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

### Def Role
role_fields = {
    'role_id': fields.Integer,
    'role_name': fields.String,
    'role_perm_id': fields.Integer,
}

### _id : mongodb id
def db_get_data_id(database, column, searchid):
    db = mogodbclient[database]
    col = db[column]
    for x in col.find({},{ "_id": searchid}):
        return x

### database : database to use, column : column/table to use, dict : dictionary to insert into the database
### mongodbclient is defined at the top of the app
def db_put_data(database, column, dict):
    db = mogodbclient[database]
    col = db[column]
    x = col.insert_one(dict).inserted_id
    return {'id': x, 'inserted data': db_get_data_id(database, column, x)}



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
    
    @marshal_with(user_fields, envelope='resource')
    def put(self, **kwargs):
        db_put_data(tomandb, user, )
        return
    
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