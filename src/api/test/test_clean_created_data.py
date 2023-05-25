from src.api.services.requests.product_req import ProductReq


class TestCleanData:
    def testDeleteProducts(self, api_login):
        startstr='fff'

        pR = ProductReq()
        pR.deleteCreatedProducts(startstr)
