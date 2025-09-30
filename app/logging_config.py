"""
Logging configuration for AI Backend API
"""

import logging
import logging.handlers
import os
from datetime import datetime
from typing import Dict, Any
import json


class CustomFormatter(logging.Formatter):
    """Custom formatter for structured logging"""
    
    def format(self, record):
        # Create a structured log entry
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        
        # Add extra fields if they exist
        if hasattr(record, 'request_id'):
            log_entry['request_id'] = record.request_id
        if hasattr(record, 'method'):
            log_entry['method'] = record.method
        if hasattr(record, 'url'):
            log_entry['url'] = record.url
        if hasattr(record, 'status_code'):
            log_entry['status_code'] = record.status_code
        if hasattr(record, 'response_time'):
            log_entry['response_time'] = record.response_time
        if hasattr(record, 'client_ip'):
            log_entry['client_ip'] = record.client_ip
        if hasattr(record, 'user_agent'):
            log_entry['user_agent'] = record.user_agent
        
        return json.dumps(log_entry, ensure_ascii=False)


def setup_logging() -> None:
    """Setup logging configuration"""
    
    # Check if running in serverless environment (Vercel)
    is_serverless = os.getenv("VERCEL") == "1" or os.getenv("AWS_LAMBDA_FUNCTION_NAME") is not None
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Remove existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Console handler with colored output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    if not is_serverless:
        # File handlers only for non-serverless environments
        # Create logs directory if it doesn't exist
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        
        # File handler for general logs
        file_handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_dir, "app.log"),
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = CustomFormatter()
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
        
        # Separate handler for API request/response logs
        api_handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_dir, "api_requests.log"),
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        api_handler.setLevel(logging.INFO)
        api_formatter = CustomFormatter()
        api_handler.setFormatter(api_formatter)
        
        # Create API logger
        api_logger = logging.getLogger("api")
        api_logger.setLevel(logging.INFO)
        api_logger.addHandler(api_handler)
        api_logger.propagate = False  # Don't propagate to root logger
        
        # Create application logger
        app_logger = logging.getLogger("app")
        app_logger.setLevel(logging.INFO)
        app_logger.addHandler(file_handler)
        app_logger.propagate = False
    else:
        # For serverless environments, use console logging with JSON format
        console_formatter = CustomFormatter()
        console_handler.setFormatter(console_formatter)
        
        # Create API logger for serverless
        api_logger = logging.getLogger("api")
        api_logger.setLevel(logging.INFO)
        api_logger.addHandler(console_handler)
        api_logger.propagate = False
        
        # Create application logger for serverless
        app_logger = logging.getLogger("app")
        app_logger.setLevel(logging.INFO)
        app_logger.addHandler(console_handler)
        app_logger.propagate = False


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance"""
    return logging.getLogger(name)


def log_api_request(
    request_id: str,
    method: str,
    url: str,
    client_ip: str,
    user_agent: str,
    request_body: str = None
) -> None:
    """Log API request details"""
    logger = get_logger("api")
    logger.info(
        "API Request",
        extra={
            'request_id': request_id,
            'method': method,
            'url': url,
            'client_ip': client_ip,
            'user_agent': user_agent,
            'request_body': request_body
        }
    )


def log_api_response(
    request_id: str,
    method: str,
    url: str,
    status_code: int,
    response_time: float,
    response_body: str = None
) -> None:
    """Log API response details"""
    logger = get_logger("api")
    logger.info(
        "API Response",
        extra={
            'request_id': request_id,
            'method': method,
            'url': url,
            'status_code': status_code,
            'response_time': response_time,
            'response_body': response_body
        }
    )
