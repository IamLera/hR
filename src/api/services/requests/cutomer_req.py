import json
from math import ceil

from src.api.storage.stored_data import StoreData as sD
import requests
import jsonpickle


class CustomerReq:

    def createCustomer(self, body):
        url = "https://api.dev.halterranch.com/v1/customer"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send createCustomer request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.post(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get createCustomer response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 201:
            sD.store['createCustomerResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )
