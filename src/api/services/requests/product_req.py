import json
from math import ceil

from src.api.storage.stored_data import StoreData as sD
from src.api.services.data.product_body import productBody
from src.api.services.data.category_body import categoryBody
from faker import Faker
import requests
import jsonpickle


class ProductReq:

    def getProductList(self, page=1):
        url = f"https://api.dev.halterranch.com/v1/product?page={page}"
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

    def deleteProduct(self, productId):
        url = f"https://api.dev.halterranch.com/v1/product/{productId}"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        print(f'\n*** *** *** Send deleteProduct request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')

        resp = requests.delete(url, headers=headers)
        print(f'\n*** *** *** Get deleteProduct response *** *** ***\n')

        assert resp.status_code == 204, f'Wrong status code - {resp.status_code}' \
                                        f'\nResponse:\n{json.dumps(resp.json(), indent=4)}'

    def deleteCreatedProducts(self, startstr):
        listOfProducts = []
        deletedItems = []
        page = 1

        # go through all the pages and add all the items to the listOfProducts list
        while True:
            self.getProductList(page)
            listOfProducts.extend(sD.store['productListResp']['items'])
            numOfPages = ceil(sD.store['productListResp']['total'] / sD.store['productListResp']['page_size'])
            if page >= numOfPages:
                break
            page += 1

        # remove those that start with the startstr
        for product in listOfProducts:
            if str(product['product_name']).startswith(startstr):
                self.deleteProduct(product['id'])
                deletedItems.append(product['product_name'])

        print(f'\nDeleted items:\n')
        print([f'{item}' for item in deletedItems])
