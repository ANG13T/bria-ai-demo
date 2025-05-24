import requests
import os
import dotenv

dotenv.load_dotenv()

api = os.getenv("BRIA_API_TOKEN")

def generate_image(prompt, aspect_ratio="1:1", seed=0, steps_num=30):
    url = "https://engine.prod.bria-api.com/v1/text-to-image/hd/2.2"
    headers = {
        "Content-Type": "application/json",
        "api_token": api
    }

    data = {
        "prompt": prompt,
        "num_results": 1,
        "sync": True,
        "aspect_ratio": aspect_ratio,
        "steps_num": steps_num
    }

    # Only include seed if user set a non-zero value
    if seed != 0:
        data["seed"] = seed

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    image_url = response.json()["result"][0]["urls"][0]
    return image_url
