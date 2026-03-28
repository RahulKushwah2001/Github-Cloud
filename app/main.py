from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.routes import router

app = FastAPI(
    title="GitHub Cloud Connector",
    description="A FastAPI service to interact with GitHub APIs",
    version="1.0.0"
)

app.include_router(router, prefix="/api", tags=["API Endpoints"])


@app.get("/", response_class=HTMLResponse, tags=["Root"])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎉 GITHUB CLOUD CONNECTOR </title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 40px;
                background: #f5f5f5;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            .info {
                color: #666;
                line-height: 1.6;
            }
            .endpoints {
                margin-top: 20px;
            }
            .endpoint {
                background: #f8f9fa;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                font-weight: bold;
            }
            a {
                color: #3498db;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Welcome to GITHUB CLOUD CONNECTOR</h1>
            <div class="info">
                <p>Here is GITHUB CLOUD which is required to build a GitHub Connector that can authenticate with GitHub.</p>
                <p>Use the links below to explore endpoints and check server status.</p>
            </div>
            <div class="endpoints">
                <div class="endpoint">📚 API Documentation: <a href="/docs">Swagger UI</a></div>
                <div class="endpoint">🏥 Health Check: <a href="/health">Status</a></div>
                <div class="endpoint">📑 API Reference: <a href="/redoc">ReDoc</a></div>
            </div>
        </div>
    </body>
    </html>
    """

# Health Endpoint
@app.get("/health", tags=["Root"])
def health():
    return {"status": "OK", "service": "GITHUB CONNECTOR"}