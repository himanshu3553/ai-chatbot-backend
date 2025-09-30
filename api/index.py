"""
Vercel entry point for AI Backend API
This file serves as the entry point for Vercel serverless deployment
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Import the FastAPI app
from app.main import app

# Export the FastAPI app for Vercel
# Vercel expects a 'handler' variable for Python functions
handler = app
