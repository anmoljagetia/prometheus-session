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
    return '\nHello World!\nI have been seen %s times.\nMy Host name is %s\n\n' % (redis.get('hits') ,host)

if __name__ == "__main__":
    monitor(app, port=8000)
    app.run(host="0.0.0.0")
