import requests


class ProductClient:

    @staticmethod
    def get_product(slug):
        response = requests.request(method="GET", url='http://192.168.0.104:8081/api/product/' + slug)
        product = response.json()
        return product

    @staticmethod
    def get_products():
        r = requests.get('http://192.168.0.104:8081/api/products')
        products = r.json()
        return products
