from database import Database
from valve.rcon import *


def check_server_state(ip):
    Database.initialize("tomandb")
    if ip == "":
        Database.read("ServerCol","{},{ip: 1}")