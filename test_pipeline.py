import datetime
from unittest import mock

import pipeline


@mock.patch("requests.get")
def test_extract(mocked_get):
    mocked_response = mocked_get.return_value
    page = {"records": [{"publish_date": datetime.date(2025, 1, 1)}]}
    mocked_response.json.return_value = page

    next(pipeline.extract())

    mocked_get.assert_called_once_with("https://example.com/")
    mocked_response.json.assert_called_once_with(object_hook=pipeline.object_hook)


def test_transform():
    record = {"publish_date": datetime.date(2025, 1, 1)}
    book = pipeline.transform(record)
    assert book == pipeline.Book(datetime.date(2025, 1, 1))
