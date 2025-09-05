# Visual Question Answering API

A REST API that uses ViLT (Vision-and-Language Transformer) to answer questions about images.

## 🚀 Features

- **Visual Question Answering**: Ask questions about images and get intelligent answers
- **ViLT Model**: Powered by `dandelin/vilt-b32-finetuned-vqa` from Hugging Face
- **FastAPI**: Modern, fast web framework for building APIs
- **Docker Support**: Easy deployment with containerization

## 📋 Prerequisites

- Docker
- Docker Compose (optional)

## 🛠️ Installation & Setup

### Using Docker Compose (Recommended)

#### 1. Clone the Repository
```bash
git clone https://github.com/gabriel-adutra/deploy_of_an_API_for_text_generation_from_images_using_an_LLM_and_Docker.git
cd deploy_of_an_API_for_text_generation_from_images_using_an_LLM_and_Docker
```

#### 2. Build and Run with Docker Compose
```bash
docker-compose up --build
```

This will:
- Build the Docker image automatically
- Start the container
- Mount the logs directory for easy access
- Set up health checks

#### 3. Run in Background (Detached Mode)
```bash
docker-compose up --build -d
```

#### 4. Check if the API is Running
```bash
docker-compose logs -f
```

#### 5. Stop the Services
```bash
docker-compose down
```

**Note**: The first run will download the ViLT model (~1.5GB), which may take a few minutes.

### Using Docker (Alternative)

If you prefer to use Docker directly:

```bash
# Build the Docker image
docker build -t vqa-api:latest .

# Run the container
docker run -d -p 3000:3000 --name vqa-container vqa-api:latest

# Check logs
docker logs vqa-container

# Stop and remove
docker stop vqa-container
docker rm vqa-container
```

## 🧪 Testing the API

The project includes pre-configured test scripts with sample images for easy testing.

### Prerequisites
Make sure the test scripts are executable:
```bash
chmod +x backend/api/tests/*.sh
```

### Available Test Scripts

#### Test the Root Endpoint
```bash
./backend/api/tests/testRoot.sh
```
Returns API information and available endpoints.

#### Test Visual Question Answering
```bash
# Test car color detection
./backend/api/tests/testCarColor.sh
# Expected response: {"answer":"yellow"}

# Test dog action recognition
./backend/api/tests/testDogAction.sh
# Expected response: {"answer":"eating"}

# Test elephant color detection
./backend/api/tests/testElephantColor.sh
# Expected response: {"answer":"green"}
```

### Sample Images Included
- `car.png` - Yellow car for color detection testing
- `dog.png` - Dog eating for action recognition testing  
- `elephant.png` - Green elephant for color detection testing

## 📡 API Endpoints

### GET `/`
Returns API information and documentation.

**Response:**
```json
{
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
```

### POST `/vqa`
Submit a question and image for visual question answering.

**Parameters:**
- `question` (string): Question about the image
- `image` (file): Image file to analyze

**Response:**
```json
{
  "answer": "red"
}
```

## 🏗️ Project Structure

```
├── backend/
│   └── api/
│       ├── app.py              # FastAPI application
│       ├── vqa_service.py      # VQA business logic
│       └── tests/              # Test scripts and sample images
│           ├── testRoot.sh     # Test root endpoint
│           ├── testCarColor.sh # Test car color question
│           ├── testDogAction.sh # Test dog action question
│           ├── testElephantColor.sh # Test elephant color question
│           ├── car.png         # Sample car image (yellow)
│           ├── dog.png         # Sample dog image (eating)
│           └── elephant.png    # Sample elephant image (green)
├── logs/                       # Local logs directory (mounted from container)
├── Dockerfile                  # Container configuration
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## 📊 Model Information

- **Model**: `dandelin/vilt-b32-finetuned-vqa`
- **Type**: Vision-and-Language Transformer (ViLT)
- **Task**: Visual Question Answering
- **Source**: Hugging Face Model Hub

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions, please open an issue in the repository.
