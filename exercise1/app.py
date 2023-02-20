from flask import Flask, render_template #import flask, datetime, calendar
import datetime
import calendar

#help with flask from: https://flask.palletsprojects.com/en/2.2.x/quickstart/

app = Flask(__name__) #name flask app

@app.route('/') #create route

def date_time(): #define date_time
    currtime = datetime.datetime.now() #set currtime variable to current date and time
    strtime = currtime.strftime("%B %d %Y %H:%M:%S") #layout time in string format to match example on canvas

    return render_template('date_time.html', currtime = calendar.day_name[currtime.weekday()]+ ', '+ strtime) #return the weekday, then the strtime we created

app.run() #run the app