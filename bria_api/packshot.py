import requests
import os
import dotenv

dotenv.load_dotenv()

api = os.getenv("BRIA_API_TOKEN")

def generate_packshot(image_url):
    url = "https://engine.prod.bria-api.com/v1/product/packshot"
    headers = {
        "Content-Type": "application/json",
        "api_token": api
    }

    data = {
        "image_url": image_url
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['result_url']

