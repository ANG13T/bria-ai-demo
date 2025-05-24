import requests
import os
import dotenv

dotenv.load_dotenv()

api = os.getenv("BRIA_API_TOKEN")

def add_shadow(image_url, shadow_color="#000000", shadow_intensity=60, shadow_blur=15):
    url = "https://engine.prod.bria-api.com/v1/product/shadow"
    headers = {
        "Content-Type": "application/json",
        "api_token": api
    }
    data = {
        "image_url": image_url,
        "shadow_color": shadow_color,
        "shadow_intensity": shadow_intensity,
        "shadow_blur": shadow_blur
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['result_url']
