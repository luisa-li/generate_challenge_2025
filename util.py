import json
import pandas as pd

def load_configs() -> dict:
    """Loads in the user-sensitive data."""
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config
    
def parse_categories(categories: list[str]) -> str:
    """Parses each category in the list by replacing %20 with a space"""
    return [category.replace("%20", " ") for category in categories]

def load_data() -> pd.DataFrame:
    """Loads data from the saved JSON"""
    DATA = "data.json"
    data = pd.read_json(DATA, orient='index')
    # reset index gets rid of the double indexing that happens 
    return data.reset_index(drop=True) 