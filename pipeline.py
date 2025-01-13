import collections
import datetime

import requests


Book = collections.namedtuple("Book", "publish_date")


def object_hook(obj):
    for key, value in obj.items():
        try:
            obj[key] = datetime.date.fromisoformat(value)
        except Exception:
            pass
        return obj


def extract():
    response = requests.get("https://example.com/")
    page = response.json(object_hook=object_hook)
    yield from page["records"]


def transform(record):
    return Book(record["publish_date"])
