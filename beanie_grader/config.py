import yaml
from pathlib import Path
from beanie_grader.beanie_config import PRODUCT_CONFIG

def load_config(path: str) -> dict:
    """
    Load config from YAML file. Falls back to default PRODUCT_CONFIG if path is invalid or file doesn't exist.
    """
    if not path or path.strip() == "":
        return PRODUCT_CONFIG
    
    config_path = Path(path)
    
    if not config_path.exists():
        print(f"Warning: Config file not found: {path}. Using default config.")
        return PRODUCT_CONFIG
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            if config is None:
                print(f"Warning: Config file is empty or invalid: {path}. Using default config.")
                return PRODUCT_CONFIG
            return config
    except Exception as e:
        print(f"Warning: Error loading config file {path}: {e}. Using default config.")
        return PRODUCT_CONFIG