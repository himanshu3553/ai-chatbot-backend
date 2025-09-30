"""
FastAPI application for AI Backend
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.logging_config import setup_logging, get_logger
from app.middleware import LoggingMiddleware

# Setup logging
setup_logging()
logger = get_logger("app")

# Create FastAPI instance
app = FastAPI(
    title="AI Backend API",
    description="A simple FastAPI backend service with comprehensive logging",
    version="1.0.0"
)

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Log application startup
logger.info("AI Backend API starting up...")


@app.get("/")
async def root():
    """
    Root endpoint that returns API information
    """
    logger.info("Root endpoint accessed")
    return {
        "message": "AI Backend API is running",
        "version": "1.0.0",
        "endpoints": {
            "hello": "/helloworld"
        }
    }


@app.get("/helloworld")
async def hello_world():
    """
    Hello World endpoint that returns a simple greeting
    """
    logger.info("Hello World endpoint accessed")
    return JSONResponse(content={"message": "Hello World"})


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting server on host=0.0.0.0, port=8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
