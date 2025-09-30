# AI Backend API

A simple and clean FastAPI backend service that provides RESTful API endpoints.

## Project Structure

```
ai-backend/
├── api/
│   └── index.py             # Vercel entry point
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── config.py            # Application configuration
│   ├── logging_config.py    # Logging configuration
│   └── middleware.py        # Request/response logging middleware
├── logs/                    # Log files directory (local only)
│   ├── app.log             # General application logs
│   └── api_requests.log    # API request/response logs
├── tests/                   # Test files (to be added)
├── docs/                    # Documentation (to be added)
├── main.py                  # Root-level entry point for Vercel dev
├── requirements.txt         # Python dependencies
├── runtime.txt              # Python runtime version for Vercel
├── vercel.json              # Vercel deployment configuration
├── deploy.sh                # Automated deployment script
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
- **Vercel Ready**: Pre-configured for easy deployment on Vercel serverless platform

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

## Vercel Deployment

This project is pre-configured for easy deployment on Vercel. Follow these steps:

### Prerequisites
- Vercel account (free at [vercel.com](https://vercel.com))
- Git repository (GitHub, GitLab, or Bitbucket)

### Deployment Steps

#### Option 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Navigate to project directory:**
   ```bash
   cd /Users/himanshu.singh2/Desktop/LangChain/ai-backend
   ```

4. **Deploy:**
   ```bash
   vercel --prod
   ```

5. **Follow the prompts:**
   - Link to existing project? `N`
   - Project name: `ai-backend` (or your preferred name)
   - Directory: `./` (current directory)
   - Override settings? `N`

#### Option 2: Deploy via Vercel Dashboard

1. **Push your code to Git:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-git-repo-url>
   git push -u origin main
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your Git repository
   - Vercel will automatically detect the Python configuration

3. **Configure deployment:**
   - Framework Preset: `Other`
   - Root Directory: `./`
   - Build Command: Leave empty (Vercel handles this automatically)
   - Output Directory: Leave empty

### Vercel Configuration Files

The project includes these Vercel-specific files:

- **`vercel.json`**: Main configuration file
- **`api/index.py`**: Entry point for Vercel serverless functions
- **`runtime.txt`**: Specifies Python 3.11 runtime
- **`requirements.txt`**: Updated with serverless-compatible dependencies

### Environment Variables

You can set environment variables in the Vercel dashboard:

1. Go to your project dashboard
2. Navigate to Settings → Environment Variables
3. Add any required environment variables

### Post-Deployment

After deployment, your API will be available at:
- **Production URL**: `https://your-project-name.vercel.app`
- **API Endpoints**:
  - `https://your-project-name.vercel.app/` - Root endpoint
  - `https://your-project-name.vercel.app/helloworld` - Hello World endpoint
  - `https://your-project-name.vercel.app/docs` - Interactive API documentation

### Logging on Vercel

- **Local Development**: Logs are written to files in the `logs/` directory
- **Vercel Production**: Logs are output to console and visible in Vercel's function logs
- **Log Format**: Structured JSON format for easy parsing

### Troubleshooting

**Common Issues:**

1. **Import Errors**: Ensure all dependencies are in `requirements.txt`
2. **Timeout Issues**: Vercel has a 10-second timeout for hobby plans
3. **Memory Limits**: Vercel hobby plan has 1024MB memory limit
4. **Cold Starts**: First request may be slower due to serverless cold starts
5. **404 Errors**: Make sure you're accessing the correct URLs (not `/api/index.py`)

**Debug Commands:**
```bash
# Test locally with Vercel CLI
vercel dev

# Check deployment logs
vercel logs

# View function logs in dashboard
# Go to Functions tab in Vercel dashboard

# Test imports locally
python3 -c "from api.index import handler; print('✅ Import successful')"
```

**Local Development:**
```bash
# Run FastAPI directly (for testing)
cd /Users/himanshu.singh2/Desktop/LangChain/ai-backend
python3 app/main.py

# Then test at: http://localhost:8000/
```

**Correct API URLs:**
- Root: `https://your-project.vercel.app/`
- Hello World: `https://your-project.vercel.app/helloworld`
- Docs: `https://your-project.vercel.app/docs`

## Dependencies

- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations
- **Python-multipart**: For handling form data
- **Mangum**: ASGI adapter for AWS Lambda and serverless environments

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
