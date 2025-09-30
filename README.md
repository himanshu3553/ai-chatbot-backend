# AI Backend API

A simple and clean FastAPI backend service that provides RESTful API endpoints.

## Project Structure

```
ai-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── config.py            # Application configuration
│   ├── logging_config.py    # Logging configuration
│   └── middleware.py        # Request/response logging middleware
├── logs/                    # Log files directory
│   ├── app.log             # General application logs
│   └── api_requests.log    # API request/response logs
├── tests/                   # Test files (to be added)
├── docs/                    # Documentation (to be added)
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Automatic Documentation**: Interactive API docs available at `/docs`
- **Type Hints**: Full type support with Pydantic models
- **Clean Architecture**: Organized folder structure for scalability
- **Comprehensive Logging**: Request/response logging with timestamps and structured JSON format
- **Log Rotation**: Automatic log file rotation to prevent disk space issues

## API Endpoints

### GET /
Returns basic API information and available endpoints.

**Response:**
```json
{
  "message": "AI Backend API is running",
  "version": "1.0.0",
  "endpoints": {
    "hello": "/helloworld"
  }
}
```

### GET /helloworld
Returns a simple "Hello World" message.

**Response:**
```json
{
  "message": "Hello World"
}
```

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd ai-backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
```bash
python app/main.py
```

### Using Uvicorn directly
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

## Testing the API

You can test the API using curl:

```bash
# Test root endpoint
curl http://localhost:8000/

# Test hello world endpoint
curl http://localhost:8000/helloworld
```

Or visit the interactive documentation at http://localhost:8000/docs to test the endpoints directly in your browser.

## Dependencies

- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations
- **Python-multipart**: For handling form data

## Logging

The application includes comprehensive logging functionality:

### Log Files
- **`logs/app.log`**: General application logs with structured JSON format
- **`logs/api_requests.log`**: Detailed API request/response logs

### Log Features
- **Structured JSON Format**: All logs are in JSON format for easy parsing
- **Request Tracking**: Each request gets a unique request ID
- **Response Time Tracking**: Measures and logs response times
- **Client Information**: Logs client IP and user agent
- **Request/Response Bodies**: Captures request and response data
- **Automatic Rotation**: Log files rotate when they reach 10MB (keeps 5 backups)

### Log Format Example
```json
{
  "timestamp": "2025-09-30T09:55:31.617804Z",
  "level": "INFO",
  "logger": "api",
  "message": "API Request",
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "method": "GET",
  "url": "http://localhost:8000/helloworld",
  "client_ip": "127.0.0.1",
  "user_agent": "curl/7.68.0",
  "status_code": 200,
  "response_time": 0.001234
}
```

## Development

This project follows a clean and minimal structure:

- `app/main.py`: Contains the FastAPI application and route definitions
- `app/config.py`: Application configuration and utilities
- `app/logging_config.py`: Logging configuration and utilities
- `app/middleware.py`: Request/response logging middleware
- `requirements.txt`: Lists all Python dependencies with versions

## Future Enhancements

- Add database integration
- Implement authentication and authorization
- Add comprehensive test suite
- Add logging and monitoring
- Implement API versioning
- Add request/response validation models

## License

This project is open source and available under the MIT License.
