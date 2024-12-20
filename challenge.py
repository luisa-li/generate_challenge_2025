from util import load_configs
import requests

configs = load_configs()

def register() -> dict:
    """Registers for the backend challenge"""
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
        
def submit(link: str): 
    """Submit the backend challenge"""
    url = configs.get('BASE_URL') + f"/api/v1/{configs.get('TOKEN')}/submit"
    payload = {"url": link}
    response = requests.post(url, json=payload)
    breakpoint()
    if response.status_code == 201:
        print("Sucessfully scored.")
        print(response.json())
    else:
        print("Scoring unsuccessful.")
        breakpoint()

if __name__ == "__main__":
    health = requests.get(f"{configs.get('BASE_URL')}/api/v1/health")
    link = "https://ad75-2800-200-e6f0-e60-61b6-48f0-fc6-9132.ngrok-free.app"
    submit(link)
    