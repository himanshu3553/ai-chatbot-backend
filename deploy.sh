#!/bin/bash

# Vercel Deployment Script for AI Backend
# This script helps deploy the FastAPI application to Vercel

echo "🚀 AI Backend - Vercel Deployment Script"
echo "========================================"

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Vercel CLI. Please install manually:"
        echo "   npm install -g vercel"
        exit 1
    fi
fi

echo "✅ Vercel CLI is available"

# Check if user is logged in
if ! vercel whoami &> /dev/null; then
    echo "🔐 Please login to Vercel..."
    vercel login
fi

echo "✅ Logged in to Vercel"

# Deploy the application
echo "🚀 Deploying to Vercel..."
vercel --prod

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Deployment successful!"
    echo "📝 Your API is now live on Vercel!"
    echo ""
    echo "🔗 Next steps:"
    echo "   1. Check your Vercel dashboard for the deployment URL"
    echo "   2. Test your endpoints:"
    echo "      - GET / (root endpoint)"
    echo "      - GET /helloworld (hello world endpoint)"
    echo "      - GET /docs (interactive API documentation)"
    echo ""
    echo "📊 Monitor your deployment:"
    echo "   - View logs: vercel logs"
    echo "   - Check functions: vercel dashboard → Functions tab"
else
    echo "❌ Deployment failed. Check the error messages above."
    exit 1
fi
