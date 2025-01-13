import datetime

import requests

import pipeline


class RequestsResponse(requests.Response):
    def __init__(self):
        super().__init__()
        self._content = '{"records": [{"publish_date": "2025-01-01"}]}'.encode("utf-8")


def test_extract(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: RequestsResponse())
    record = next(pipeline.extract())
    assert record["publish_date"] == datetime.date(2025, 1, 1)


def test_transform():
    record = {"publish_date": datetime.date(2025, 1, 1)}
    book = pipeline.transform(record)
    assert book == pipeline.Book(datetime.date(2025, 1, 1))
