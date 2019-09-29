import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Dates & Precipitation for Select Dates"""
    result1 = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").all()
    #jsonify that shit w/ for-in
    for result in result1:
        precipitationdict = {}
        precipitationdict["date"]=Measurement.date
        precipitationdict["prcp"]=Measurement.prcp
    return jsonify(result1)


@app.route("/api/v1.0/stations")
def station():
    """List of Stations"""
    result2 = session.query(Station.station).all()
    #np.ravel to turn tuples into list 
    station_list = list(np.ravel(result2))
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    """Station & Temp"""
    # Query temps and dates from the last year
    result3 = session.query(Measurement.station, Measurement.tobs).all()
       
    #jsonify that shit w/ for-in
    for result in result3:
        result3dict = {}
        result3dict["date"]=Measurement.station
        result3dict["tobs"]=Measurement.tobs
    return jsonify(result3)

@app.route("/api/v1.0/<start>")
def start(start):
    #Define start date
    # startdate = datetime.strftime(start,'%Y-%m-%d')
    #fix
    startdate = datetime.strptime(start,'%Y-%m-%d')
    #Query temperature data
    maxtemp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= startdate).all()
    mintemp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= startdate).all()
    avgtemp = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= startdate).all()
    
    temp={}
    temp["Max Temperature"] = maxtemp[0]
    temp["Min Temperature"] = mintemp[0]
    temp["Avg Temperature"] = avgtemp[0]

    return jsonify(temp)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    #Define start date and end date
    # startdate = datetime.strftime(start,'%Y-%m-%d')
    # enddate = datetime.strftime(end,'%Y-%m-%d')
    #fix
    startdate = datetime.strptime(start,'%Y-%m-%d')
    enddate = datetime.strptime(end,'%Y-%m-%d')
    #Query temperature data
    max = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= startdate).filter(Measurement.date <= enddate).all()
    min = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= startdate).filter(Measurement.date <= enddate).all()
    avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= startdate).filter(Measurement.date <= enddate).all()
    
    temp={}
    temp["Max Temperature"] = max[0]
    temp["Min Temperature"] = min[0]
    temp["Avg Temperature"] = avg[0]

    return jsonify(temp)

if __name__ == '__main__':
    app.run(debug=True)
