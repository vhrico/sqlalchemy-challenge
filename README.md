# sqlalchemy-challenge
SQL Alchemy Challenge Module 10 (Week 10)


This challenge uses SQLite database of weather stations in Hawaii. It is divided into 2 parts, a jupyter notebook analysis and Flask app.
Two files were provided for the analysis, climate_starter.ipynb and hawaii.sqlite.

Part 1. Jupyter notebook Analysis and exploration of Climate Data
This section, uses Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. 

Analysis 1: Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

Analysis 2: Station Analysis Design a query to calculate the total number of stations in the dataset.

Analysis 3: Design a query to find the most-active stations and which station id has the greatest number of observations?

Analysis 4: Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Analysis 5: Design a query to get the previous 12 months of temperature observation (TOBS) data. 
Query the previous 12 months of TOBS data for that station.

Plot the results as a histogram.

Part 2. Write a Flask app that displays the previous queries in JSON format. Two files are used, app.py and sqlhelper.py

App.py provides the routes to the queries and displays them in webpage

Sqlhelper.py has all the required queries and logic.