from fastapi.testclient import TestClient
from api import app  

client = TestClient(app)

def test_get_products_default():
    response = client.get("api/v1/products")
    assert response.json() == [{'categories': ['electronics', 'toys'],
        'id': 'EBK46802',
        'name': 'Amazon Kindle Paperwhite Kids Edition',
        'price': 11000,
        'stars': 492},
        {'categories': ['electronics'],
        'id': 'BCD35791',
        'name': 'Apple MacBook Pro 14-inch',
        'price': 199900,
        'stars': 499},
        {'categories': ['electronics'],
        'id': 'CAN24680',
        'name': 'Canon EOS R Mirrorless Camera',
        'price': 179900,
        'stars': 160}]
    assert response.status_code == 200

def test_get_products_with_sort_and_order():
    response = client.get("api/v1/products?sort=price&order=desc")
    assert response.status_code == 200

def test_get_products_with_categories():
    response = client.get("api/v1/products?categories=electronics,beauty")
    assert response.status_code == 200

def test_lots_filters():
    response = client.get("/api/v1/products?categories=electronics&limit=10&order=desc&price_max=1500&price_min=1000&sort=price&star_max=500&star_min=400")
    assert response.status_code == 200