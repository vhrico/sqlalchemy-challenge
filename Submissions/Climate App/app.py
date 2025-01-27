# Import Dependacies

import pandas as pd
import numpy as np
from flask import Flask, jsonify
from sql_helper import SQLHelper

####################
# Database Setup Section was created in the sql_helper file as per instructor    
####################

# Flask Setup
####################
app = Flask(__name__)
sqlHelper = SQLHelper();

####################
# Flask Routes
####################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/precipitation</a><br/>" # ORM
        f"<a href='/api/v1.0/precipitation2' target='_blank'>/api/v1.0/precipitation2</a><br/>" # SQL
        f"<a href='/api/v1.0/stations' target='_blank'>/api/v1.0/stations</a><br/>" # ORM
        f"<a href='/api/v1.0/stations2' target='_blank'>/api/v1.0/stations2</a><br/>" # SQL
        f"<a href='/api/v1.0/tobs' target='_blank'>/api/v1.0/tobs</a><br/>" # ORM
        f"<a href='/api/v1.0/tobs2' target='_blank'>/api/v1.0/tobs2</a><br/>" # SQL
        f"<a href='/api/v1.0/orm/2017-01-01' target='_blank'>/api/v1.0/orm/2017-01-01</a><br/>" # ORM
        f"<a href='/api/v1.0/2017-01-01' target='_blank'>/api/v1.0/2017-01-01</a><br/>" # SQL
        f"<a href='/api/v1.0/orm/2017-01-01/2017-01-31' target='_blank'>/api/v1.0/orm/2017-01-01/2017-01-31</a><br/>" # ORM
        f"<a href='/api/v1.0/2017-01-01/2017-01-31' target='_blank'>/api/v1.0/2017-01-01/2017-01-31</a><br/>" # SQL
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Execute queries
    df = sqlHelper.queryPrecipitationORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/precipitation2")
def precipitation2():
    # Execute Query
    df = sqlHelper.queryPrecipitationSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    # Execute Query
    df = sqlHelper.queryStationsORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations2")
def stations2():
    # Execute Query
    df = sqlHelper.queryStationsSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def temperature2():
    # Execute Query
    df = sqlHelper.queryTemperatureORM()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/tobs2")
def temperature():
    # Execute Query
    df = sqlHelper.queryTemperatureSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/orm/<start>")
def tstats1(start):
    # Execute Query
    df = sqlHelper.queryTStatsORM(start)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def tstats2(start):
    # Execute Query
    df = sqlHelper.queryTStatsSQL(start)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def tstats_startend1(start, end):
    # Execute Query
    df = sqlHelper.queryTStats_StartEndSQL(start, end)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/orm/<start>/<end>")
def tstats_startend2(start, end):
    # Execute Query
    df = sqlHelper.queryTStats_StartEndORM(start, end)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
