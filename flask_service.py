#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, redirect
from flask_googlemaps import GoogleMaps, Map
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__, template_folder=".")
app.config['SECRET_KEY'] = 'you-will-never-guess'
# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDpD86Gd0GN7nVRLJUsM-R3qy97bv3xsyc"

# Initialize the extension
GoogleMaps(app)

class LocForm(FlaskForm):
    lat = StringField('Longitude')
    lon = StringField('Latitude')
    submit = SubmitField('Submit')

blue_icon = "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
red_icon = "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
starbucks_icon = 'https://s3.amazonaws.com/bootcamp111/rsz_1starbuck.jpg'
hospital_icon = 'https://s3.amazonaws.com/bootcamp111/Webp.net-resizeimage.jpg'




@app.route("/", methods=['GET', 'POST'])
def location_form():
    form = LocForm()
    loc = {
                    'lat': form.lat.data,
                    'lng': form.lon.data,
                    'infobox': "Our location"
                }

    lat = float(form.lat.data)
    lon = float(form.lon.data)

    starbucks_locs = [(lat + 0.01, lon), (lat - 0.01, lon), (lat + 0.01, lon + 0.01), (lat + 0.02, lon),
                      (lat + 0.01, lon - 0.01)]

    hospital_locs = [(lat + 0.02, lon), (lat + 0.02, lon), (lat - 0.04, lon + 0.03), (lat - 0.02, lon),
                      (lat + 0.03, lon)]

    starbucks_markers = []
    hospital_markers = []

    for loc in starbucks_locs:
        marker = {
            'icon': blue_icon,
            'lat': str(loc[0]),
            'lng': str(loc[1]),
            'infobox': "<img src='https://s3.amazonaws.com/bootcamp111/rsz_1starbuck.jpg' />"
        }
        starbucks_markers.append(marker)

    for loc in hospital_locs:
        marker = {
            'icon': red_icon,
            'lat': str(loc[0]),
            'lng': str(loc[1]),
            'infobox': "<img src='https://s3.amazonaws.com/bootcamp111/Webp.net-resizeimage.jpg' />"
        }
        hospital_markers.append(marker)


    markers = starbucks_markers + hospital_markers
    markers.append(loc)
    if form.validate_on_submit():
        map = Map(
            identifier="test",
            lat=form.lat.data,
            lng=form.lon.data,
            style="height:800px;width:800px;margin:0;",
            markers = markers
        )

        return render_template('index.html', form=form, lat=form.lat.data, lon=form.lon.data, map=map)
    return render_template('index.html', form=form, lat=None, lon=None, map=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

