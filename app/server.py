import os
import pymysql

from flask import Flask, request, render_template
from populate_db import populate_db_from_json
from controller import search_data


app = Flask(__name__)


@app.route("/")
def index():
    title = request.args.get("title", default=None)
    url = request.args.get("url", default=None)
    date_after = request.args.get("date_after", default=None)
    date_before = request.args.get("date_before", default=None)

    data_entries = search_data(title, url, date_after, date_before)

    return render_template("index.html", data_entries=data_entries)


@app.post("/populate-db")
def populate_db_endpoint():
    js_data = request.json
    if not js_data or "items" not in js_data:
        return "Invalid JSON", 400

    populate_db_from_json(js_data["items"])

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
