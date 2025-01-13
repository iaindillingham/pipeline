import collections
import datetime

import requests


Book = collections.namedtuple("Book", "publish_date")


def extract():
    response = requests.get("https://example.com/")
    page = response.json()
    yield from page["records"]


def transform(record):
    publish_date = datetime.date.fromisoformat(record["publish_date"])
    return Book(publish_date)
