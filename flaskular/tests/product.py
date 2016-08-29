from base import BaseTestCase


class ProductTestCase(BaseTestCase):

    def test_products_all(self):
        rv = self.client.get('/products')
        j = self.parseJsonResponse(rv)
        assert len(j['products']) > 100
        return j

    def test_product_code(self):
        rv = self.client.get('/products/878217')
        j = self.parseJsonResponse(rv)
        assert j['cnetID'] == 'S8725865'
        return j

    def test_products_by_category(self):
        rv = self.client.get('/products?category=HH_Druckerpatronen_Toner')
        j = self.parseJsonResponse(rv)
        assert len(j['products']) > 0
        return j

    def test_product_invalid_code(self):
        rv = self.client.get('/products/not_valid_code')
        assert rv.status_code == 404