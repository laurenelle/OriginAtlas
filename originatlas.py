from PIL import Image, ImageChops, ImageOps
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash, session, request, g, json, jsonify
from werkzeug import secure_filename
import model
import re
import time
import os
# import forms
# import bcrypt

from sqlalchemy import select, func, types, sql, update
from geopy import geocoders

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home_page():
	return render_template("index.html")


@app.route('/library')
def library():
	return render_template("library.html")

@app.route('/map')
def map():
	return render_template("map.html")




if __name__ == '__main__':
    app.run(debug=True)