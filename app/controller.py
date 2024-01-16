import os
import pymysql


def get_db_connection():
    return pymysql.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        db=os.environ["MYSQL_DATABASE"],
        port=int(os.environ["MYSQL_PORT"]),
    )


def search_data(title=None, url=None, date_after=None, date_before=None):
    query_conditions = []
    parameters = []

    if title:
        query_conditions.append("title LIKE %s")
        parameters.append(f"%{title}%")

    if url:
        query_conditions.append("url LIKE %s")
        parameters.append(f"%{url}%")

    if date_after:
        query_conditions.append("date_added >= %s")
        parameters.append(date_after)

    if date_before:
        query_conditions.append("date_added <= %s")
        parameters.append(date_before)

    query = "SELECT title, url, date_added FROM data"
    if query_conditions:
        query += " WHERE " + " AND ".join(query_conditions)

    results = []
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
    finally:
        connection.close()

    return results
