"""
FastAPI application for AI Backend
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI instance
app = FastAPI(
    title="AI Backend API",
    description="A simple FastAPI backend service",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    Root endpoint that returns API information
    """
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
    return JSONResponse(content={"message": "Hello World"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
