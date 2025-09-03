
from fastapi import FastAPI, UploadFile, File, Form
from PIL import Image
import io
import uvicorn
from vqa_service import vqa_service


app = FastAPI()


# API root endpoint - returns service information
@app.get("/")
def get_api_info():
    return {
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



# Visual Question Answering endpoint
@app.post("/vqa")
async def answer_question_about_image(question: str = Form(...), image: UploadFile = File(...)):
    # Convert uploaded file to PIL Image
    image_bytes = await image.read()
    pil_image = Image.open(io.BytesIO(image_bytes))
    
    # Get answer from VQA service
    answer = vqa_service.answer_question(question, pil_image)
    return {"answer": answer}




# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)







