import requests

def test_external_ping():
    resp = requests.get("https://api.github.com", timeout=5)

    assert resp.status_code == 200
