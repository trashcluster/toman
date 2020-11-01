# Tournament Manager  
Tournament Manager for CS:GO  

The idea is to make a tournament manager for csgo in a nice Django app, the tournament part is tightly connected with Toornament and the CSGO server part managment is done using RCON commands for the sake of setup simplicity as a standard default srcds can be used without modification



## 25/10/2020  

CSGO Log files streaming to remote : https://www.reddit.com/r/GlobalOffensive/comments/cx3i3j/  csgo_server_writting_all_player_stats_to_log_file/  
python-valve, RCON source : https://python-valve.readthedocs.io/en/latest/rcon.html  
Django tuto : https://www.youtube.com/watch?v=tkzIZNIb_gA&list=PLxhnp_qsD8ENSAazjTbUWbfIA7j0-m5Ww&index=5  
quick start docker django : https://docs.docker.com/compose/django/  
django intro : https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release  
toornament developer website : https://developer.toornament.com/v2/overview/get-started  
  
## 26/10/2020  

after a bit of research Django doesn't seem to fit the approach of the project,
A client - server app does look more promising, the idea is to use flask as a backend api server and a frontend app to interact with the api, i have never coded a frontend app and am completely unfamiliar with any web app framework 
flask official doc : https://flask.palletsprojects.com/en/1.1.x/
  
## 29/10/2020  

for the api side i think using flask-restful seems the best choice, or at least the easiest way to do it for now. I also have created a mongodb altas free tier account and will be experimenting with data storage on mongodb  
I am also setting up the project page to keep track of the functions

pymongo W3S doc : https://www.w3schools.com/python/python_mongodb_getstarted.asp
flask-restful official doc : https://flask-restful.readthedocs.io/en/latest/

## 31/10/2020  

avanced a bit on the user, group, roles fields.
Found out thst the way i used in the program to initialize vars isn't so nice. Check https://blog.tecladocode.com/marshmallow-serialization-mongodb-python/.

