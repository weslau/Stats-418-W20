from flask import Flask
import logging
import datetime

app = Flask(__name__)

##logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%H:%M:%S')
logging.warning('is when this event was logged.')


##logging.warning('Hello World! Good %s')
##get the current time in military time
z = int(datetime.datetime.today().strftime('%H')) ##z is just the number for hour
##logging.warning(z)
##convert the military time into morning, afternoon, etc

##function to convert hours to time of day
def gettime(curr_time):
    if (curr_time>=6 and curr_time<12):
        return "morning"
    elif (curr_time>=12 and curr_time<18):
        return "afternoon"
    elif (curr_time>=18 and curr_time<21):
        return "evening"
    elif (curr_time>=21 and curr_time<=24) or (curr_time>=0 and curr_time<6):
        return "night"
    else:
        return "unrecognized time"

time_day = gettime(z) ##run function on the current hour
##logging.warning(time_day)

@app.route("/")
def hello():
    return "Hello World! Good " + time_day



##logging.shutdown()