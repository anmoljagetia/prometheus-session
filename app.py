from flask import Flask
from redis import Redis
from flask_prometheus import monitor
import os
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def hello():
    try:
        redis.incr('hits')
        result='<img src="http://thecatapi.com/api/images/get?format=src&type=gif" style="display:block;margin-left:auto;margin-right:auto;width:50%%;height:50%%"> <p align="center"> <br /><h1 align="center">I have been seen <b>%s</b> times.</h1><h2 align="center">My Host name is <br /><b>%s</b></h2></p>' % (int(redis.get('hits')) ,host)
    except:
        result='<img src="http://thecatapi.com/api/images/get?format=src&type=gif" style="display:block;margin-left:auto;margin-right:auto;width:50%%;height:50%%"> <p align="center"> <br /><h1 align="center">I have been seen <b>0</b> times.</h1><h2 align="center">My Host name is <br /><b>%s</b></h2></p>' % (host)
    return str(result)

if __name__ == "__main__":
    monitor(app, port=8000)
    app.run(host="0.0.0.0")
