import requests
import os
import dotenv
dotenv.load_dotenv()

api = os.getenv("BRIA_API_TOKEN")

def generate_lifestyle(image_url):
    url = "https://engine.prod.bria-api.com/v1/product/lifestyle_shot_by_text"
    headers = {
        "Content-Type": "application/json",
        "api_token": api
    }
    data = {
        "image_url": image_url,
        "scene_description": "In a living room interior, on a kitchen counter",
        "placement_type": "original",
        "num_results": 1,
        "original_quality": True,
        "optimize_description": True,
        "sync": True
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['result'][0][0]
