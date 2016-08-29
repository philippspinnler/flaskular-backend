

class ProductMock(object):
    def __init__(self, mock_data):
        self.mock_data = mock_data

    # helper method to mock mongoengine
    def objects(self, code=None, category=None):
        if code is not None:
            return self.get_product_by_code(code)
        if category is not None:
            return self.get_products_by_category(category)
        else:
            return self.get_products()

    def get_products(self):
        products = []
        for product in self.mock_data.iter("product"):
            products.append(ProductMock.create_product(product))

        return products

    def get_product_by_code(self, code):
        product = self.mock_data.xpath('.//code[text()="%s"]' % code)
        if len(product) > 0:
            return ProductMock.create_product(product[0].getparent())
        else:
            return None

    def get_products_by_category(self, category):
        products = []
        for product in self.mock_data.xpath('.//categoryID[text()="%s"]' % category):
            products.append(ProductMock.create_product(product.getparent()))

        if len(products) > 0:
            return products
        return None

    @staticmethod
    def create_product(product):
        created_product = {'features': {}}
        for feature in product.iter("feature"):
            label = feature.findtext('label', default=None)
            value = feature.findtext('value', default=None)
            created_product['features'][label] = value
        for c in product.getchildren():
            created_product[c.tag] = c.text

        return created_product
