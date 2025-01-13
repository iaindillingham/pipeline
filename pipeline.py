import requests


def extract():
    response = requests.get("https://example.com/")
    page = response.json()
    yield from page["records"]
