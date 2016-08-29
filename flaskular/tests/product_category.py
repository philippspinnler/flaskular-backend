from base import BaseTestCase


class ProductCategoryTestCase(BaseTestCase):

    def test_productcategories_all(self):
        rv = self.client.get('/productcategories')
        j = self.parseJsonResponse(rv)
        assert len(j['productcategories']) > 100
        return j

    def test_productcategories_id(self):
        rv = self.client.get('/productcategories/HH_Druckerpatronen_Toner')
        j = self.parseJsonResponse(rv)
        assert len(j['products']) > 0
        return j

    def test_productcategories_invalid_id(self):
        rv = self.client.get('/productcategories/not_valid_id')
        assert rv.status_code == 404