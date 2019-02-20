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


@app.route("/", methods=['GET', 'POST'])
def location_form():
    form = LocForm()
    if form.validate_on_submit():
        print(form.lat.data)
        print(form.lon.data)

        mymap = Map(
            identifier="view-side",
            lat=form.lat.data,
            lng=form.lon.data,
            markers=[(form.lat.data, form.lon.data)]
        )

        sndmap = Map(
            identifier="sndmap",
            lat=form.lat.data,
            lng=form.lon.data,
            markers=[
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': form.lat.data,
                    'lng': form.lon.data,
                    'infobox': "<b>Hello World</b>"
                },
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    'lat': form.lat.data,
                    'lng': form.lon.data,
                    'infobox': "<b>Hello World from other place</b>"
                }
            ]
        )

        return render_template('example.html', mymap=mymap, sndmap=sndmap, lat=form.lat.data, lon=form.lon.data)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

