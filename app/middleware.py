"""
Middleware for logging API requests and responses
"""

import time
import uuid
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.logging_config import log_api_request, log_api_response


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all API requests and responses"""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Start timing
        start_time = time.time()
        
        # Get request details
        method = request.method
        url = str(request.url)
        client_ip = request.client.host if request.client else "unknown"
        user_agent = request.headers.get("user-agent", "unknown")
        
        # Read request body if present
        request_body = None
        if method in ["POST", "PUT", "PATCH"]:
            try:
                body = await request.body()
                if body:
                    request_body = body.decode("utf-8")
            except Exception:
                request_body = "Unable to read request body"
        
        # Log the request
        log_api_request(
            request_id=request_id,
            method=method,
            url=url,
            client_ip=client_ip,
            user_agent=user_agent,
            request_body=request_body
        )
        
        # Process the request
        response = await call_next(request)
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Get response details
        status_code = response.status_code
        
        # Read response body if present
        response_body = None
        if hasattr(response, 'body'):
            try:
                response_body = response.body.decode("utf-8") if response.body else None
            except Exception:
                response_body = "Unable to read response body"
        
        # Log the response
        log_api_response(
            request_id=request_id,
            method=method,
            url=url,
            status_code=status_code,
            response_time=response_time,
            response_body=response_body
        )
        
        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id
        
        return response
