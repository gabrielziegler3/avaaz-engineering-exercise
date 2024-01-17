# Avaaz Engineering Exercise

Thanks for your interest in joining Avaaz! We are thrilled that you considered working with us.

Your task is to build a small application that allows a user to search data using several filters:
- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

The following things are provided in this repository:
- The destination database table (see `database/initdb.d/setup.sql`)
- A bare bones Flask app (see `app/server.py`)

**We recommend you spend a maximum of two hours on it, and don't worry if you didn’t cover all of the requirements.**

## Instructions

- Use Python and Flask for your application
- The application ingests JSON source data (see the input folder)
- The application stores valid data and normalized datetimes in the provided database
- The application allows searching the data through an API endpoint (using the filters described above)

Submit your solution by sending a zipped file via email to your Avaaz recruiting contact (you can reply to your existing email thread).

# Solution

# Running the app

## Spin up containers

```bash
docker-compose up
```

## Populate DB (only needs to be done once)

Here we populate with curl so that we don't need to move the data into the container nor install mysql client on our host machine.

```bash
curl localhost:5000/populate-db \
    -X POST \
    -d @input/data.json \
    -H 'Content-Type: application/json'
```

## Access the website and search

```
http://localhost:5000/
```

## Future improvements

- Add pagination to the search endpoint
- Add a frontend to the app
- Add tests for controller, service, and server.
- CI pipeline to check for linting and tests.
- Improve title and url check when populating DB.
- Improve datetime check when populating DB (timezone, dealing with missing year, etc)
