#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map
app = Flask(__name__, template_folder=".")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDpD86Gd0GN7nVRLJUsM-R3qy97bv3xsyc"

# Initialize the extension
GoogleMaps(app)



@app.route("/")
def hello():

    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )

    return render_template('example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

