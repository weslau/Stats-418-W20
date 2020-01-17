from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig(filename='demo.log', level=logging.DEBUG)
@app.route("/")
def hello():
    return "Hello World! Good "

##get the time from logging info, it will be in UTC time tho
def gettime(curr_time):
    if (curr_time<6 and curr_time>21):
        return "night"
    elif curr_time<12:
        return "morning"
    elif curr_time<18:
        return "afternoon"
    elif curr_time<21:
        return "evening"
    else:
        return "unrecognized time"