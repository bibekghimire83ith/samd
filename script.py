# -*- coding: utf-8 -*-
"""
Created on Sat May 12 20:02:29 2018

@author: BIBEK GHIMIRE
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)