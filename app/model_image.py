from PIL import Image
import numpy as np
import cv2
import io

def analyze_image(content: bytes):
    # Example dummy implementation (replace with real model logic)
    image = Image.open(io.BytesIO(content)).convert("RGB")
    np_image = np.array(image)

    # Placeholder: simulate detection
    nsfw_score = 0.92
    category = "porn"

    return {
        "nsfw_score": round(nsfw_score, 3),
        "category": category,
        "recommendation": "block" if nsfw_score > 0.8 else "allow"
    }
