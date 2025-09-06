
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import uvicorn
import logging
import os

# Create log directory if it doesn't exist
os.makedirs("/var/log/vqa", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/vqa/backend.log'),
        logging.StreamHandler()
    ]
)

# Disable noisy loggers
logging.getLogger('filelock').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('python_multipart').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)
logging.getLogger('transformers').setLevel(logging.WARNING)

from vqa_service import vqa_service


app = FastAPI()


# Allow frontend container or localhost to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou ["http://localhost:8080"] para restringir ao frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API root endpoint - returns service information
@app.get("/")
def get_api_info():
    logging.info(" / endpoint is called.")
    api_data = {
        "name": "Visual Question Answering API",
        "description": "A REST API that uses ViLT (Vision-and-Language Transformer) to answer questions about images",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API information and documentation",
            "POST /vqa": "Submit a question and image for analysis"
        },
        "model": "dandelin/vilt-b32-finetuned-vqa",
        "usage": {
            "method": "POST",
            "endpoint": "/vqa",
            "content_type": "multipart/form-data",
            "parameters": {
                "question": "Question about the image (string)",
                "image": "Image file (binary)"
            },
            "example": {
                "question": "What color is the car?",
                "image": "car_image.jpg"
            }
        },
        "status": "active"
    }
    logging.info(f"/ endpoint is returning: {api_data}")
    return api_data



# Visual Question Answering endpoint
@app.post("/vqa")
async def answer_question_about_image(question: str = Form(...), image: UploadFile = File(...)):
    logging.info(f"VQA is called with question: '{question}' and image: {image.filename}")
    
    try:
        # Convert uploaded file to PIL Image
        image_bytes = await image.read()
        pil_image = Image.open(io.BytesIO(image_bytes))
        logging.info(f"Image processed - Size: {pil_image.size}, Mode: {pil_image.mode}")
        
        # Get answer from VQA service
        answer = vqa_service.answer_question(question, pil_image)
        logging.info(f"VQA is returning: {{'answer': '{answer}'}}")
        
        return {"answer": answer}
    except Exception as e:
        logging.error(f"Error processing VQA request: {str(e)}")
        raise




# Start the FastAPI server
if __name__ == "__main__":
    logging.info("Starting VQA API server on host 0.0.0.0:3000")
    uvicorn.run(app, host="0.0.0.0", port=3000)







