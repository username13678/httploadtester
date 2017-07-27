#!/usr/bin/env python

import random
import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  time.sleep(random.random())
  if not random.randint(0,100):
    return 'Internal Server Error', 500
  return 'Hello, World!'

if __name__ == '__main__':
    app.run()
