import time
from loguru import logger
import redis
from flask import Flask, request
from celery import Celery

app = Flask(__name__)




cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    logger.debug('inside hello')
    count = get_hit_count()
    return 'Hello World! {} times.\n'.format(count)



