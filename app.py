from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with
#from valve.rcon import *
from email.utils import formatdate
import time
# Database class from the database.py file
from database import Database

#Init Flask App
app = Flask(__name__)
#Init Flask-restful api
api=Api(app)

#valve.rcon.execute(("85.10.205.252",27015),"password","help")

################################## USER MANAGMENT ####################################

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

#Create a user, no right managment implemented for now.
# UserCreate endpoint
class UserCreate(Resource):
    Database.initialize("tomandb")
    # GET request, does not perform any actions
    def get(self):
        return {'405 error': 'use this endpoint to create a user, send a put request'}, 405

    # PUT request, create a user entry in the database
    def put(self):
        putdata = request.form['username']
        putdata += request.form['name']
        putdata += request.form['firstname']
        putdata += request.form['pseudonym']

        ### Database put data
        #return {'userid' : 'YEET', 'username' : putdata}, 200
        Database.insert("UserCol", {'userid' : 'YEET', 'username' : putdata})
        return putdata, 200



api.add_resource(UserCreate, '/api/v1/user/create')
#api.add_resource(UserList, '/api/v1/user/list')

if __name__ == '__main__':
    app.run()