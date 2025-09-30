"""
Root-level main.py for Vercel dev compatibility
This file imports the FastAPI app from the app module
"""

from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
