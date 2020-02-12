# Import flash and other stuff we will need
import pandas as pd
import numpy as np
from flask import Flask, escape, request
import os
from datetime import datetime
import requests
import json
import sqlite3
import xml.etree.ElementTree as ET

# This is how we initiate a flask app to then build it
app = Flask(__name__)


#################
# Lets start with building a hello world API
#
# > http://$HOSTNAME/v1 -- return Hello World!
# > http://$HOSTNAME/v1?name=some_name -- return Hello $some_name
@app.route("/v1")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"


# Let's make the API more RESTful
#
# > http://$HOSTNAME/v2/some_name -- return Hello $some_name
@app.route("/v2/<name>", methods=["GET"])
def hello2(name):
    return f"Hello, {escape(name)} (v2)"


# first create the data call to OMDB
# put it under different route name
@app.route("/search/<string:query>", methods=["GET"])
def pullData(query):
    url = 'http://www.omdbapi.com/'
    key = '747d9548'
    params = {"apikey": key, "t": query}
    query1 = request.args.get('query')
    print(query1)
    return query1




##################
# Main method to launch Flask server
#
# --> host: makes it bind publically (could have als been 0.0.0.0 instead). If
# we did not specify this it would only bind to 127.0.0.1 which means it would
# only be accessible from the local computer
#
# --> port: set the "port" we bind to to be based on our Linux user ID. This
# way if multiple users try to launch flask servers each will run on a
# different port to avoid conflicts
#
# --> debug: enable debugging and more verbose information since we are still
# developing the app and not running it in a production environment
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50000, debug=True)
