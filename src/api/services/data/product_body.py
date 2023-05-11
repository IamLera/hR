import json


class productBody:

    def __init__(self, product_name, inventory_type, cost=100, price="100$", tax_rate="default_rate",
                 sku_type="general", category_id=None, subcategory_id=None, category=None,
                 processing_time="not_assigned", product_description="", comment=""
):

        self.product_description = product_description
        self.comment = comment
        self.product_name = product_name
        self.processing_time = processing_time
        self.inventory_type = inventory_type
        self.category = category
        self.category_id = category_id
        self.subcategory_id = subcategory_id
        self.sku_type = sku_type
        self.cost = cost
        self.price = price
        self.tax_rate = tax_rate
