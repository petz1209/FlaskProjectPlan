import pytest
import requests

def test_indexRoute():
    with requests.Session() as r:
        r.get("/")
        response = r.json()
    assert (response, "hello world")
