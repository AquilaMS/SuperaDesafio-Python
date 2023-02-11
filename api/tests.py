from django.test import TestCase


class TestConnections(TestCase):
    def test_success_signup(self):
        response = self.client.post('/api/signup/')
        self.assertEqual(response.status_code, 200)

    # Test with no AUTH
    def test_success_gettoken(self):
        response = self.client.post('/api/get-token/')
        self.assertEqual(response.status_code, 400)

    def test_success_post_cart(self):
        response = self.client.post('/api/cart/')
        self.assertEqual(response.status_code, 401)

    def test_success_delete_cart(self):
        response = self.client.delete('/api/cart/')
        self.assertEqual(response.status_code, 401)

    def test_success_checkout(self):
        response = self.client.post('/api/cart/checkout/')
        self.assertEqual(response.status_code, 401)

    def test_success_filter_price(self):
        response = self.client.get('/api/cart/filter/price/')
        self.assertEqual(response.status_code, 401)

    def test_success_filter_score(self):
        response = self.client.get('/api/cart/filter/score/')
        self.assertEqual(response.status_code, 401)

    def test_success_filter_name(self):
        response = self.client.get('/api/cart/filter/name/')
        self.assertEqual(response.status_code, 401)


class TestInputs(TestCase):
    pass
