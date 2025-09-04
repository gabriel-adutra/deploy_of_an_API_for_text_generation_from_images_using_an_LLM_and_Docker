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

### Using Docker

#### 1. Clone the Repository
```bash
git clone https://github.com/gabriel-adutra/deploy_of_an_API_for_text_generation_from_images_using_an_LLM_and_Docker.git
cd deploy_of_an_API_for_text_generation_from_images_using_an_LLM_and_Docker
```

#### 2. Build the Docker Image
```bash
docker build -t vqa-api:latest .
```

#### 3. Run the Container
```bash
docker run -dit --name vqa-container -p 3000:3000 vqa-api:latest
```

#### 4. Check if the API is Running
```bash
docker logs vqa-container
```

You should see output indicating the FastAPI server is running on port 3000.

**Note**: The first run will download the ViLT model (~1.5GB), which may take a few minutes.

## 🧪 Testing the API

### Using Test Scripts (Linux/macOS)

Make sure the test scripts are executable:
```bash
chmod +x backend/api/tests/*.sh
```

#### Test the Root Endpoint
```bash
./backend/api/tests/testRoot.sh
```

This will return API information and available endpoints.

#### Test Visual Question Answering
```bash
# Test with car image
./backend/api/tests/testCarColor.sh

# Test with dog image
./backend/api/tests/testDogAction.sh

# Test with elephant image
./backend/api/tests/testElephantColor.sh
```

**Note**: Make sure you have the test images (`car.png`, `elephant.png`, `dog.png`) in the same directory as the test scripts.

### Using curl (Cross-platform)

#### Test the Root Endpoint
```bash
curl -X GET "http://localhost:3000/" -H "accept: application/json"
```

#### Test Visual Question Answering
```bash
# Test with car image
curl -X POST "http://localhost:3000/vqa" \
  -H "accept: application/json" \
  -F "question=Which color is the car in the image?" \
  -F "image=@car.png"

# Test with dog image
curl -X POST "http://localhost:3000/vqa" \
  -H "accept: application/json" \
  -F "question=What is the dog doing in the image?" \
  -F "image=@dog.png"

# Test with elephant image
curl -X POST "http://localhost:3000/vqa" \
  -H "accept: application/json" \
  -F "question=Which color is the elephant in the image?" \
  -F "image=@elephant.png"
```

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
│       └── tests/              # Test scripts
│           ├── testRoot.sh     # Test root endpoint
│           ├── testCarColor.sh # Test car color question
│           ├── testDogAction.sh # Test dog action question
│           └── testElephantColor.sh # Test elephant color question
├── Dockerfile                  # Container configuration
├── docker-compose.yml          # Development environment

├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## 🔧 Development

### Using Docker (Individual Container)

For direct Docker deployment:

```bash
# Build the Docker image
docker build -t vqa-api:latest .

# Run the container
docker run -dit --name vqa-container -p 3000:3000 vqa-api:latest

# Check if the API is running
docker logs vqa-container
```

### Using Docker Compose (Recommended for Development)

The project includes a `docker-compose.yml` file for easy development setup.

Run the following command:
```bash
docker-compose up -d
```

This will:
- Build the Docker image
- Start the container with volume mounting for development
- Set up health checks
- Configure automatic restart

### Stopping the Services

```bash
# Stop Docker Compose
docker-compose down

# Stop Docker container
docker stop vqa-container
docker rm vqa-container
```

### Troubleshooting

#### Common Issues

1. **Port 3000 already in use:**
   ```bash
   # Find process using port 3000
   lsof -i :3000  # macOS/Linux
   netstat -ano | findstr :3000  # Windows
   
   # Kill the process or use a different port
   docker run -dit --name vqa-container -p 3001:3000 vqa-api:latest
   ```

2. **Model download fails:**
   - Check internet connection
   - Ensure you have enough disk space (~2GB)
   - Try running with `--no-cache` flag:
     ```bash
     docker build --no-cache -t vqa-api:latest .
     ```

3. **Permission denied on test scripts:**
   ```bash
   chmod +x backend/api/tests/*.sh
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
