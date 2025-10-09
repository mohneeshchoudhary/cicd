from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="CICD Learning App", description="A simple FastAPI app to learn CI/CD")

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CICD Learning App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: white;
                padding: 3rem;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
                text-align: center;
                max-width: 600px;
                margin: 2rem;
            }
            h1 {
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            p {
                color: #666;
                font-size: 1.2rem;
                line-height: 1.6;
                margin-bottom: 2rem;
            }
            .highlight {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 25px;
                font-weight: bold;
                display: inline-block;
                margin: 1rem 0;
            }
            .footer {
                color: #999;
                font-size: 0.9rem;
                margin-top: 2rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 FastAPI CICD Learning</h1>
            <p>Welcome to our simple FastAPI application!</p>
            <div class="highlight">This is a demo to teach students how to setup CICD Pipeline</div>
            <p>I am Mohneesh who is learning it</p>
            <p>This application demonstrates a basic FastAPI setup that can be used for learning Continuous Integration and Continuous Deployment practices.</p>
            <div class="footer">
                Built with FastAPI | Ready for CI/CD Pipeline
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "CICD Learning App is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
