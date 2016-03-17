#!/usr/bin/env python3
"""
Flask test in python
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def main():
    return render_template("index.html")

@app.route('/about')
def show_about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run()
