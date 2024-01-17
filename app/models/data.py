import logging

from logger import LogHandler
from datetime import datetime
from dateutil import parser as dt_parser


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(LogHandler())

DB_DATETIME_FMT = "%Y-%m-%d %H:%M:%S"


class DataModel:
    def __init__(self, title: str, uri: str, date: str | datetime):
        self.title = title
        self.uri = uri

        # check if uri looks like a url
        if not uri or (not self.uri.startswith("http")) and (not self.uri.startswith("www")):
            logger.debug(f"Invalid uri: {self.uri}")
            raise ValueError(f"Invalid uri: {self.uri}")

        # check if date is valid
        if isinstance(date, datetime):
            self.date = date
        else:
            try:
                self.date = dt_parser.parse(date, fuzzy=True, default=None)
            except ValueError as e:
                logger.debug(f"Failed to parse date: {date}")
                raise e

    def to_db_tuple(self):
        return (self.title, self.uri, self.date.strftime(DB_DATETIME_FMT))
