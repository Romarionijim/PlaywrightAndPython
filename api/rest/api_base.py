import json
from playwright.sync_api import APIRequestContext
import requests


class ApiFunctions:
    def __init__(self, api_request_context: APIRequestContext):
        self.api_request_context = api_request_context

    def get(self, url: str):
        response = self.api_request_context.get(url, headers={
            'Content-Type': 'application-json',
        })
        return response

