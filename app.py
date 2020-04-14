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

# Save reference to the table
measurement_table = Base.classes.measurement
station_table = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(measurement_table.date,measurement_table.prcp).\
        filter(measurement_table.date > '2016-08-23').all()
    
    return jsonify(results)
    
    session.close()



@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(station_table.station).all()
    return jsonify(results)

    session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results=session.query(measurement_table.tobs).filter(measurement_table.station=="USC00519281").\
filter(measurement_table.date >= '2016-08-23').all()

    results_one=list(np.ravel(results))

    return jsonify(results_one)

    session.close()

@app.route("/api/v1.0/<start>")
def temp_start(start=None):
      # Create our session (link) from Python to the DB
    session = Session(engine)

    results=session.query(func.min(measurement_table.tobs), func.avg(measurement_table.tobs), func.max(measurement_table.tobs)).\
        filter(measurement_table.date >= start).all()
    

    results=list(np.ravel(results))

    return jsonify(results)

    session.close()
     


@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start=None,end=None):
      # Create our session (link) from Python to the DB
    session = Session(engine)

    results=session.query(func.min(measurement_table.tobs), func.avg(measurement_table.tobs), func.max(measurement_table.tobs)).\
        filter(measurement_table.date >= start).filter(measurement_table.date <= end).all()

    results=list(np.ravel(results))

    return jsonify(results)

    session.close()


if __name__ == '__main__':
    app.run(debug=True)
