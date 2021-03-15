import time
from loguru import logger
import redis
from flask import Flask, request
from celery import Celery

app = Flask(__name__)

from tasks1 import add


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
    result = add.delay(4, 4)
    return 'Hello World! {} times.\n'.format(count)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


