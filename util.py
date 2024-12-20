import json

def load_configs() -> dict:
    """Loads in the user-sensitive data."""
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config
    
    