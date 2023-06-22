import json
from math import ceil

from src.api.storage.stored_data import StoreData as sD
import requests
import jsonpickle


class CustomerReq:
    def getCustomerList(self, page=1):
        url = f"https://api.dev.halterranch.com/v1/customer?page={page}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        print(f'\n*** *** *** Send getCustomerList request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        resp = requests.get(url, headers=headers)

        print(f'\n*** *** *** Get getCustomerList response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 200:
            sD.store['getCustomerListResp'] = resp.json()
        else:
            raise AssertionError(f'Wrong status code - {resp.status_code}')

        assert len(resp.json()["items"]) > 0, "No items were found"

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

    def editCustomerProfile(self, body, customerId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}/profile"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send editCustomerProfile request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.patch(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get editCustomerProfile response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 200:
            sD.store['editCustomerProfileResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def editCustomerAddress(self, body, customerId, addressId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}/address/{addressId}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send editCustomerAddress request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.patch(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get editCustomerAddress response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 200:
            sD.store['editCustomerAddressResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def addCustomerAddress(self, body, customerId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}/address"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send addCustomerAddress request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.post(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get addCustomerAddress response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 201:
            sD.store['addCustomerAddressResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def addCustomerWallet(self, body, customerId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}/card"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send addCustomerWallet request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.post(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get addCustomerWallet response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 201:
            sD.store['addCustomerWalletResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def editCustomerClub(self, body, customerId, clubId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}/club-membership/{clubId}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send editCustomerClub request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.patch(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get editCustomerClub response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data, if correct code is returned
        if resp.status_code == 200:
            sD.store['editCustomerClubResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def deleteCustomer(self, customerId):
        url = f"https://api.dev.halterranch.com/v1/customer/{customerId}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        print(f'\n*** *** *** Send deleteCustomer request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')

        resp = requests.delete(url, headers=headers)
        print(f'\n*** *** *** Get deleteCustomer response *** *** ***\n')

        assert resp.status_code == 204, f'Wrong status code - {resp.status_code}' \
                                        f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'

    def deleteCreatedCustomers(self, startstr):
        listOfCustomers = []
        deletedItems = []
        page = 1

        # go through all the pages and add all the items to the listOfCustomers list
        while True:
            self.getCustomerList(page)
            listOfCustomers.extend(sD.store['getCustomerListResp']['items'])
            numOfPages = ceil(sD.store['getCustomerListResp']['total'] / sD.store['getCustomerListResp']['page_size'])
            if page >= numOfPages:
                break
            page += 1

        # remove those that start with the startstr
        for customer in listOfCustomers:
            if str(customer['first_name']).startswith(startstr):
                self.deleteCustomer(customer['id'])
                deletedItems.append(customer['first_name'])

        print(f'\nDeleted items:\n')
        print([f'{item}' for item in deletedItems])

