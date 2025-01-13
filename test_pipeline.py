import datetime

import requests

import pipeline


class MockResponse:
    def json(self, **kwargs):
        return {"records": [{"publish_date": "2025-01-01"}]}


def test_extract(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())
    record = next(pipeline.extract())
    assert record["publish_date"] == "2025-01-01"


def test_transform():
    record = {"publish_date": "2025-01-01"}
    book = pipeline.transform(record)
    assert book == pipeline.Book(datetime.date(2025, 1, 1))
