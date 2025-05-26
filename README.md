# Product Snap
Product Snap is a smart product creator application that allows users to generate, modify, and enhance product images through a series of steps using the [Bria API](https://bria.ai/)

 <img src="https://github.com/ANG13T/bria-ai-demo/blob/main/assets/app_files/result.png?raw=true" width="300"/>

 <img src="https://github.com/ANG13T/bria-ai-demo/blob/main/assets/app_files/app.png?raw=true" width="600"/>
 
## Features
1. **Generate Image**: Create a product image based on a text prompt and specified aspect ratio.
2. **Cutout**: Remove the background from the generated image to isolate the product.
3. **Enhance Resolution**: Improve the resolution of the cutout image for better quality.
4. **Packshot**: Generate a professional packshot of the product.
5. **Add Shadow**: Add realistic shadows to the packshot to enhance its appearance.
6. **Lifestyle Shot**: Create a lifestyle shot by placing the product in a real-world context.

# Getting Started
```
git clone https://github.com/ANG13T/bria-ai-demo.git

cd bria-ai-demo

python3 -m venv briademo

source briademo/bin/activate

pip install streamlit dotenv

streamlit run app.py
```

Go to: `http://localhost:8501` on a browser

# Provide API Key
Get your API key here: [https://platform.bria.ai/console/account/api-keys](https://platform.bria.ai/console/account/api-keys)

Create a `.env` file including your API key at the root of the code base 

```
BRIA_API_TOKEN=API_KEY_HERE
```

# Bria API Endpoints

**Generate Image**: Generates an image from a text prompt with specified parameters like aspect ratio and seed for randomness
`https://engine.prod.bria-api.com/v1/text-to-image/hd/2.2`

**Product Cutout**: Removes the background from an image to create a cutout of the product
`https://engine.prod.bria-api.com/v1/product/cutout`

**Increase Resolution**: Enhances the resolution of an image to improve its quality
`https://engine.prod.bria-api.com/v1/image/increase_resolution?desired_increase=2`

**Generate Packshot**: Creates a professional packshot of the product
`https://engine.prod.bria-api.com/v1/product/packshot`

**Add Shadow**: Adds shadows to an image to give it a more realistic appearance
`https://engine.prod.bria-api.com/v1/product/shadow`

**Generate Lifestyle**: Generates a lifestyle shot by placing the product in a contextual background
`https://engine.prod.bria-api.com/v1/product/lifestyle_shot_by_text`
