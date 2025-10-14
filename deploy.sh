#!/bin/bash

# Simple deployment script for AWS CodePipeline
# Handles basic deployment, service restart, and verification

set -e

# Configuration
APP_DIR="/home/ec2-user/deploy"
APP_PORT=8000
APP_URL="http://localhost:${APP_PORT}"

echo "🚀 Starting deployment process..."

# Navigate to application directory
cd "$APP_DIR"

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Stop existing application
echo "🛑 Stopping existing application..."
pkill -f "python.*main.py" 2>/dev/null || true
sleep 2

# Start application
echo "▶️  Starting application..."
nohup python main.py > app.log 2>&1 &
sleep 5

# Verify application is running
echo "🔍 Verifying deployment..."
if curl -f -s "${APP_URL}/health" > /dev/null; then
    echo "✅ Deployment successful!"
    echo "🌐 Application running at: $APP_URL"
else
    echo "❌ Deployment failed!"
    exit 1
fi
