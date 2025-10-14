#!/bin/bash

# Simple AWS CodePipeline PostScript
set -e

echo "🚀 Starting deployment..."

# Go to app directory
cd /home/ec2-user/deploy

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Stop old app if running
pkill -f "python.*main.py" 2>/dev/null || true
sleep 2

# Start the app
echo "▶️ Starting FastAPI app..."
nohup python main.py > app.log 2>&1 &
sleep 5

# Check if it's working
echo "🔍 Checking if app is running..."
if curl -f -s http://localhost:8000/health > /dev/null; then
    echo "✅ Deployment successful! App is running on http://localhost:8000"
else
    echo "❌ Deployment failed!"
    exit 1
fi