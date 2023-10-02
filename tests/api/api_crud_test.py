from playwright.sync_api import APIRequestContext
import json
from api.rest.api_base import ApiFunctions
from api.endpoints.endpoints import EndPoints
from api.urls.api_url import Urls


def test_get_users(api_request_context: APIRequestContext):
    url = Urls.DUMMY_API
    endpoint = EndPoints.USERS
    api_functions = ApiFunctions(api_request_context)
    response = api_functions.get(f"{url}/{endpoint}")
    response_body = response.body()
    print(response_body)
