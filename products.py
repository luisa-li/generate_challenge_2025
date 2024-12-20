import json 
import requests
from util import load_configs

configs = load_configs()

def product_detail(id: str) -> dict:
    """Retrieves the product detail for a given ID"""
    url = configs.get('BASE_URL') + f"/api/v1/products/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        print(response.json())
        raise Exception("Failed to get product details.")

if __name__ == "__main__":
    
    product_info = {}
    products = configs.get("PRODUCT_IDS")
    for product in products: 
        product_info[product] = product_detail(product)
    
    with open("data.json", "w") as json_file:
        json.dump(product_info, json_file, indent=4)
