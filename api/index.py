"""
Vercel entry point for AI Backend API
This file serves as the entry point for Vercel serverless deployment
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

# Export the FastAPI app for Vercel
handler = app
