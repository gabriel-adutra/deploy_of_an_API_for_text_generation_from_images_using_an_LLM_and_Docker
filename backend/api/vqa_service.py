from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


class VQAService:
    """Visual Question Answering service using ViLT model"""
    
    def __init__(self):
        self.processor = None
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load ViLT model components"""
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        self.model = ViltForQuestionAnswering.from_pretrained('dandelin/vilt-b32-finetuned-vqa')
    
    def answer_question(self, question: str, image: Image.Image) -> str:
        """
        Answer a question about an image using ViLT model
        
        Args:
            question: Text question about the image
            image: PIL Image object
            
        Returns:
            Answer to the question
        """
        # Encode image and question for the model
        model_inputs = self.processor(image, question, return_tensors="pt")
        
        # Get model predictions
        model_outputs = self.model(**model_inputs)
        prediction_scores = model_outputs.logits
        
        # Find the most likely answer
        best_answer_index = prediction_scores.argmax(-1).item()
        return self.model.config.id2label[best_answer_index]


# Global service instance
vqa_service = VQAService()

