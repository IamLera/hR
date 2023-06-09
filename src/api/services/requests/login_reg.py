import requests
import pytest
import json
from src.api.services.data.login_body import loginBody as lB
from src.api.storage.stored_data import StoreData as sD


class LoginReq:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        url = "https://api.dev.halterranch.com/v1/auth/login"
        newlB = lB(self.email, self.password)

        jsonLB = json.loads(newlB.to_json())

        print(f'\n*** *** *** Send Login request *** *** ***\n')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(jsonLB, indent=4)}')
        resp = requests.post(url, data=newlB.to_json())

        print(f'\n*** *** *** Get Login response *** *** ***\n')
        print(f'\nResponse body:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 200:
            sD.store['access_token'] = resp.json()['access_token']
            sD.store['response'] = resp.json()
        else:
            raise AssertionError(f'Wrong status code - {resp.status_code}')


