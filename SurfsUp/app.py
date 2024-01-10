# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    """homepage route - List all available route"""
    return (
        f"Available Route:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end")

@app.route("/api/v1.0/precipitation")
def precipitation():
    """ Return JSON representation of last 12 months of precipitation data"""
    
    # most recent data and one year before 
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    
    #convert to datetime
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date()
    
    #one year prior
    one_year_ago = most_recent_date - dt.timedelta(days=365)
    
    #Query last 12 months of data
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= one_year_ago)\
        .filter(Measurement.date <= most_recent_date)\
        .all()
    
    #convert query to dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

if __name__ '__main__':
    app.run(debug=True)
