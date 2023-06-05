import json

import requests
from src.api.storage.stored_data import StoreData as sD


class CategoryReq:

    def getCategoryList(self):
        url = "https://api.dev.halterranch.com/v1/category"
        headers = {"Authorization": f'Bearer {sD.store["access_token"]}'}

        print(f'\n*** *** *** Send getCategoryList request *** *** ***\n')
        print(f'Request header - {headers}')
        print(f'Request url - {url}')
        resp = requests.get(url, headers=headers)

        print(f'\n*** *** *** Get getCategoryList response *** *** ***\n')
        print(f'\nResponse:\n{json.dumps(resp.json(), indent=4)}')

        # store the data
        if resp.status_code == 200:
            sD.store['getCategoryListResp'] = resp.json()
        else:
            raise AssertionError(f'Wrong status code - {resp.status_code}')

        assert len(resp.json()["items"]) > 0, "No items were found"

    def returnCategoryDict(self):
        data_dict = {}
        subcat_dict={}
        data = sD.store["getCategoryListResp"]

        # add categories to the dictionary - dict={"cat":["cat_id", "subcatDict":
        #                                                                           [{"subcatName1"},{"subcatId1}...]]}
        for item in data.get('items', []):
            item_id = item.get('id')
            item_name = item.get('name')
            data_dict[item_name] = []  # Create an empty list as the value for the key
            data_dict[item_name].append(item_id)

            subcategories = item.get('subcategories', [])
            for subcategory in subcategories:
                subcategory_id = subcategory.get('id')
                subcategory_name = subcategory.get('name')
                subcat_dict[subcategory_name] = subcategory_id
            data_dict[item_name].append(subcat_dict)


        return data_dict