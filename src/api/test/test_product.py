from src.api.services.data.category_body import categoryBody
from src.api.services.data.product_body import productBody
from src.api.services.requests.category_req import CategoryReq
from src.api.services.requests.product_req import ProductReq
from src.helpers.value_generators import Generators


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

        body = productBody(name, invType, category_id=catDict['Experiences'])

        pR = ProductReq()
        pR.createProduct(body)

    def testCreateExperiencesProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "experiences"

        cat = CategoryReq()
        cat.getCategoryList()
        catDict = cat.returnCategoryDict()

        body = productBody(name, invType, category_id=catDict['Experiences'][0])

        pR = ProductReq()
        pR.createProduct(body)

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

    def testCreateProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "gratuity"
        body = productBody(name, invType)

        pR = ProductReq()
        pR.createProduct(body)

    def testEditProduct(self, api_login):
        name = Generators.stringGenerator()
        invType = "gratuity"
        body = productBody(name, invType)

        invType = "gratuity"

        bodyUpdated = productBody(name, invType, price="150$")

        pR = ProductReq()
        pR.createProduct(body)
        pR.editProduct(bodyUpdated)
