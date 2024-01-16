import pytest

from datetime import datetime
from app.models.data import DataModel

@pytest.mark.parametrize("title, uri, date_str, expected", [
    ("Test Date 1", "http://example.com", "2014-03-08T15", datetime(2014, 3, 8, 15, 0)),
    ("Test Date 2", "http://example.com", "March 30 1985", datetime(1985, 3, 30)),
    ("Test Date 3", "http://example.com", "1991-03-11T01:39:21", datetime(1991, 3, 11, 1, 39, 21)),
])
def test_data_model_date_parsing(title, uri, date_str, expected):
    data_model = DataModel(title, uri, date_str)
    assert data_model.date == expected

@pytest.mark.parametrize("title, uri, date_str", [
    ("Invalid Date 1", "http://example.com", "invalid-date"),
    ("Invalid Date 2", "http://example.com", "2021-02-30"),
    ("Invalid Date 3", "http://example.com", "2021-13-01"),
    ("Invalid Date 4", "http://example.com", "Feb 30 2021"),
    ("Invalid Date 5", "http://example.com", "202103"),
    ("Invalid Date 6", "http://example.com", "2021/13/01"),
])
def test_data_model_date_parsing_invalid(title, uri, date_str):
    with pytest.raises(ValueError):
        DataModel(title, uri, date_str)
