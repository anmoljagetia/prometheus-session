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
    redis.incr('hits')
    return '<img src="http://thecatapi.com/api/images/get?format=src&type=gif" style="display:block;margin-left:auto;margin-right:auto;width:50%%;height:50%%"> <br />Hello World! <br />I have been seen %s times. <br />My Host name is %s <br />' % (redis.get('hits') ,host)

if __name__ == "__main__":
    monitor(app, port=8000)
    app.run(host="0.0.0.0")
