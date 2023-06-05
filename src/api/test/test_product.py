from src.api.services.data.category_body import categoryBody
from src.api.services.data.product_body import productBody
from src.api.services.requests.category_req import CategoryReq
from src.api.services.requests.product_req import ProductReq
from src.helpers.value_generators import Generators
from src.api.storage.stored_data import StoreData as sD


class TestProducts:

    def testGetProducts(self, api_login):
        pR = ProductReq()
        pR.getProductList()

    def testCreateDiscountProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "discounts"

        cat = CategoryReq()
        cat.getCategoryList()
        catDict = cat.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict['Experiences'][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateExperiencesProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "experiences"

        cat = CategoryReq()
        cat.getCategoryList()
        catDict = cat.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict['Experiences'][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateCulinaryProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "culinary"
        category = 'Culinary'
        subCat = 'Starters'

        cat = CategoryReq()
        cat.getCategoryList()
        catDict = cat.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0], subcategory_id=catDict[category][1][subCat])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateTastingProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "tasting"
        category = 'Tasting Room'
        subCat = 'Ranch Flight'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0], subcategory_id=catDict[category][1][subCat])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateShippingProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "shipping"
        category = 'Experiences'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateNonInventoryProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "non_inventory_items"
        category = 'Experiences'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateMerchandiseProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "merchandise"
        category = 'Estate Goods'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateGratuityProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "gratuity"
        category = 'Estate Goods'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateRetailFoodProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "retail_food"
        category = 'Tasting Room'
        subCat = 'Ranch Flight'

        cR = CategoryReq()
        cR.getCategoryList()
        catDict = cR.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict[category][0], subcategory_id=catDict[category][1][subCat])

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testCreateProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "gratuity"
        body = productBody(name, invType)

        pR = ProductReq()
        pR.createProduct(body)

        assert name == sD.store['createProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["createProductResp"]["product_name"]}'
        assert invType == sD.store['createProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["createProductResp"]["inventory_type"]}'

    def testEditProduct(self, api_login):
        name = Generators.stringGenerator()
        nameUpd = Generators.stringGenerator()
        invType = "gratuity"
        body = productBody(name, invType)
        bodyUpdated = productBody(nameUpd, invType, price="150$")

        pR = ProductReq()
        pR.createProduct(body)
        pR.editProduct(bodyUpdated)

        assert nameUpd == sD.store['editProductResp']['product_name'],\
            f'Wrong product_name - {sD.store["editProductResp"]["product_name"]}'
        assert invType == sD.store['editProductResp']['inventory_type'],\
            f'Wrong product_name - {sD.store["editProductResp"]["inventory_type"]}'


    def testDeleteProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "gratuity"
        body = productBody(name, invType)

        pR = ProductReq()
        pR.createProduct(body)
        pR.deleteProduct(sD.store['createProductResp']['id'])
