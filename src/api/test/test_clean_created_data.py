from src.api.services.requests.cutomer_req import CustomerReq
from src.api.services.requests.product_req import ProductReq


class TestCleanData:
    def testDeleteProducts(self, api_login):
        startstr='py-'

        pR = ProductReq()
        pR.deleteCreatedProducts(startstr)

    def testDeleteCustomers(self, api_login):
        startstr='py-'

        cR = CustomerReq()
        cR.deleteCreatedCustomers(startstr)
