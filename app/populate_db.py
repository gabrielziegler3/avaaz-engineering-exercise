import json
import os
import pymysql
import sys
import logging

from models.data import DataModel
from logger import LogHandler


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(LogHandler())

DATA_PATH = "input/data.json"


def populate_db_from_json(data):
    connection = pymysql.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        db=os.environ["MYSQL_DATABASE"],
        port=int(os.environ["MYSQL_PORT"]),
    )
    inserted = 0

    try:
        with connection.cursor() as cursor:
            for item in data:
                try:
                    logger.debug(
                        f"Inserting title {item['title']}, date {item['date']}, uri {item['uri']}"
                    )
                    data_model = DataModel(
                        title=item["title"], uri=item["uri"], date=item["date"]
                    )
                    sql = "INSERT INTO `data` (`title`, `url`, `date_added`) VALUES (%s, %s, %s)"
                    cursor.execute(sql, data_model.to_db_tuple())
                    inserted += 1
                except ValueError:
                    logger.warn(
                        f"Failed to parse record: {item['title']}, {item['date']}, {item['uri']}']"
                    )
                    continue
                except Exception:
                    logger.error(
                        f"Unknown error inserting record: {item['title']}, {item['date']}, {item['uri']}']"
                    )
                    continue
        logger.info(f"Inserted {inserted} records out of {len(data)}")
        connection.commit()
    finally:
        connection.close()
