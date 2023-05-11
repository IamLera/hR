import json
from src.api.storage.stored_data import StoreData as sD
from src.api.services.data.product_body import productBody
from src.api.services.data.category_body import categoryBody
from faker import Faker
import requests
import jsonpickle


class ProductReq:

    def getProductList(self):
        url = "https://api.dev.halterranch.com/v1/product"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        print(f'\n*** *** *** Send getProductList request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        resp = requests.get(url, headers=headers)

        print(f'\n*** *** *** Get getProductList response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 200:
            sD.store['productListResp'] = resp.json()
        else:
            raise AssertionError(f'Wrong status code - {resp.status_code}')

        assert len(resp.json()["items"]) > 0, "No items were found"

    def createProduct(self, body):
        url = "https://api.dev.halterranch.com/v1/product"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send createProduct request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.post(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get createProduct response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 201:
            sD.store['createProductResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def createDiscountProduct(self, body):
        url = "https://api.dev.halterranch.com/v1/product"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(body, unpicklable=False)

        print(f'\n*** *** *** Send createDiscountProduct request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.post(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get createDiscountProduct response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 201:
            sD.store['createDiscountProductResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )

    def editProduct(self, bodyUpdated):
        productId = sD.store['createProductResp']['id']
        url = f"https://api.dev.halterranch.com/v1/product/{productId}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        jsonBody = jsonpickle.encode(bodyUpdated, unpicklable=False)

        print(f'\n*** *** *** Send editProduct request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        print(f'\nRequest body:\n{json.dumps(json.loads(jsonBody), indent=4)}')

        resp = requests.put(url, headers=headers, data=jsonBody)
        print(f'\n*** *** *** Get editProduct response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 200:
            sD.store['editProductResp'] = resp.json()
        else:
            raise AssertionError(
                f'Wrong status code - {resp.status_code}'
                f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'
            )
