import requests
import os
import dotenv

dotenv.load_dotenv()

api = os.getenv("BRIA_API_TOKEN")

def increase_resolution(image_url):
    url = "https://engine.prod.bria-api.com/v1/image/increase_resolution?desired_increase=2"
    headers = {
        "api_token": api
    }
    files = {
        "image_url": (None, image_url)
    }
    response = requests.post(url, headers=headers, files=files)
    response.raise_for_status()
    return response.json()['result_url']
