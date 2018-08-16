import os

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Home Route
@app.route("/")
def index():
    return render_template("index.html")

# Application Route
@app.route("/application")
def application():
    return render_template("application.html")

# About Route
@app.route("/about")
def about():
    return render_template("about.html")
# Gallery Route
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
