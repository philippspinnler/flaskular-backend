

class ProductCategoryMock(object):
    def __init__(self, mock_data):
        self.mock_data = mock_data

    # helper method to mock mongoengine
    def objects(self, id=None):
        if id is None:
            return self.get_product_categories()
        else:
            return self.get_product_category_by_id(id)

    def get_product_categories(self):
        productcategories = []
        productcategory_ids = []
        for product in self.mock_data.iter("product"):
            category_id = product.findtext('categoryID', default=None)
            if category_id not in productcategory_ids:
                productcategories.append(ProductCategoryMock.create_productcategory(product))
                productcategory_ids.append(category_id)
        return productcategories

    def get_product_category_by_id(self, id):
        product_category = self.mock_data.xpath('.//categoryID[text()="%s"]' % id)
        if len(product_category) > 0:
            return ProductCategoryMock.create_productcategory(product_category[0].getparent())
        else:
            return None

    @staticmethod
    def create_productcategory(product):
        created_productcategory = {
            'id': product.findtext('categoryID', default=None),
            'name': product.findtext('category', default=None)
        }

        return created_productcategory
