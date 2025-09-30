# AI Backend API

A simple and clean FastAPI backend service that provides RESTful API endpoints.

## Project Structure

```
ai-backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main FastAPI application
│   └── config.py        # Application configuration
├── tests/               # Test files (to be added)
├── docs/                # Documentation (to be added)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Automatic Documentation**: Interactive API docs available at `/docs`
- **Type Hints**: Full type support with Pydantic models
- **Clean Architecture**: Organized folder structure for scalability

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

## Development

This project follows a clean and minimal structure:

- `app/main.py`: Contains the FastAPI application and route definitions
- `app/config.py`: Application configuration and utilities
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
