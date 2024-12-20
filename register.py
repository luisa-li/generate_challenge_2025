from util import load_configs
import requests

configs = load_configs()

def register() -> dict:
    url = configs.get('BASE_URL') + "/api/v1/register"
    payload = {
        "email": configs.get("EMAIL"),
        "name": configs.get("NAME")
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print("Successfully registered.")
        return response.json()
    else:
        print("Registration failed.")

if __name__ == "__main__":
    response = register()
    print(response)