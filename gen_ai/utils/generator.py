from diffusers import StableDiffusionXLPipeline
import torch
from datetime import datetime
import os

# 🔐 Hugging Face access token
HF_TOKEN = "hf_yZakEUYJU"

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    variant="fp16",
    token=HF_TOKEN
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, user):
    print("⏳ Generating image...")
    image = pipe(prompt=prompt, guidance_scale=0.0, num_inference_steps=1).images[0]
    filename = f"static/generated/{user}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)
    print(f"✅ Saved image at {filename}")
    return filename
