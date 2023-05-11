from src.api.services.requests.category_req import CategoryReq


class TestCategories:

    def testGetProducts(self, api_login):
        cR = CategoryReq()
        cR.getCategoryList()
