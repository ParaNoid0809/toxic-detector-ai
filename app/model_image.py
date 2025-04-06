from nsfw_detector import predict
import os
import tempfile

model_path = "app/models/nsfw_mobilenet2.224x224.h5"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = predict.load_model(model_path)

def analyze_image(content: bytes):
    try:
        # Save the incoming bytes to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(content)
            tmp_file_path = tmp_file.name

        # Use nsfw_detector's classify() — handles resizing & preprocessing
        predictions = predict.classify(model, tmp_file_path)

        # Clean up temp file
        os.remove(tmp_file_path)

        if not predictions:
            raise ValueError("No prediction returned")

        result = list(predictions.values())[0]
        top_category = max(result, key=result.get)
        score = result[top_category]

        return {
            "category": top_category,
            "nsfw_score": round(score, 3),
            "recommendation": "block" if score > 0.8 else "allow"
        }

    except Exception as e:
        print("[ERROR] analyze_image failed:", str(e))
        raise RuntimeError(f"Error processing image: {str(e)}")
