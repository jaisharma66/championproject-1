import os

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/application")
def application():
    return render_template("application.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
