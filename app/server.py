import os

from flask import Flask, request
from populate_db import populate_db_from_json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}@{os.environ.get('MYSQL_HOST')}"


@app.post('/populate-db')
def populate_db_endpoint():
    js_data = request.json
    if not js_data or 'items' not in js_data:
        return 'Invalid JSON', 400

    populate_db_from_json(js_data['items'])

    return 'OK', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
