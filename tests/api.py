import pytest
from pages.main import Main


def test_get_request():
    main = Main()
    res = main.get("https://gorest.co.in/public/v2/users")
    status_code = res.status_code
    json_data = res.json()
    body = res.content

    assert status_code == 200
    print(f" JSON DATA => {json_data}")
    print(f" status code is => {status_code}")
    print(f"body content {body}")