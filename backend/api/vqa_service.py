from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import logging
import os


class VQAService:
    """Visual Question Answering service using ViLT model"""
    
    def __init__(self):
        self.processor = None
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load ViLT model components"""
        logging.info("Loading ViLT model components...")
        try:
            self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
            logging.info("ViLT processor loaded successfully")
            
            self.model = ViltForQuestionAnswering.from_pretrained('dandelin/vilt-b32-finetuned-vqa')
            logging.info("ViLT model loaded successfully")
        except Exception as e:
            logging.error(f"Failed to load ViLT model: {str(e)}")
            raise
    
    def _convert_image_to_rgb(self, image: Image.Image) -> Image.Image:
        """Convert image to RGB format for ViLT model"""
        if image.mode == 'RGBA':
            logging.debug("Converting RGBA image to RGB")
            # Create a white background
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])  # Use alpha channel as mask
            return background
        elif image.mode != 'RGB':
            logging.debug(f"Converting image from {image.mode} to RGB")
            return image.convert('RGB')
        else:
            logging.debug("Image is already in RGB format")
            return image

    def _run_model_inference(self, image: Image.Image, question: str) -> str:
        """Run ViLT model inference on image and question"""
        try:
            # Encode image and question for the model
            logging.debug("Encoding image and question for model")
            model_inputs = self.processor(image, question, return_tensors="pt")
            
            # Get model predictions
            logging.debug("Running model inference")
            model_outputs = self.model(**model_inputs)
            prediction_scores = model_outputs.logits
            
            # Find the most likely answer
            best_answer_index = prediction_scores.argmax(-1).item()
            answer = self.model.config.id2label[best_answer_index]
            
            logging.debug(f"Model prediction completed - Answer: '{answer}'")
            return answer
            
        except Exception as e:
            logging.error(f"Error during model inference: {str(e)}")
            raise

    def answer_question(self, question: str, image: Image.Image) -> str:
        """
        Answer a question about an image using ViLT model
        
        Args:
            question: Text question about the image
            image: PIL Image object
            
        Returns:
            Answer to the question
        """
        logging.debug(f"Processing question: '{question}' with image size: {image.size}, mode: {image.mode}")
        
        # Convert image to RGB format
        rgb_image = self._convert_image_to_rgb(image)
        
        # Run model inference
        answer = self._run_model_inference(rgb_image, question)
        
        return answer


# Global service instance
vqa_service = VQAService()

