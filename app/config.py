"""
Application configuration and utilities
"""

from typing import Dict, Any


def get_app_info() -> Dict[str, Any]:
    """
    Get application information
    """
    return {
        "name": "AI Backend",
        "version": "1.0.0",
        "description": "A simple FastAPI backend service"
    }
