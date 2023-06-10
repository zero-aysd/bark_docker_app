# FastAPI Prompt Processing

This project demonstrates a FastAPI app for processing prompts.

## Getting Started

1. Clone the repository.

2. Install the required dependencies:

    pip install -r requirements.txt

3. Start the FastAPI sever with docker-compose

4. Send a POST request to `http://localhost:8000/prompt/` with the prompt content in the request body.

## API Endpoint

### `POST /prompt/`

This endpoint processes a prompt and returns the corresponding output.

#### Request

- Method: `POST`
- URL: `http://localhost:8000/prompt/`
- Headers:
- `Content-Type: application/json`
- Body (JSON):
```json
{
 "prompt": "Enter your prompt here"
}

Response
    Success (200 OK):  json
    
    {
    "Output": "Base64 encoded output"
    }

Failure (500 Internal Server Error): Internal Server Error, Request Failed