from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api import monitoring, alerts, incidents
from app.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - initialize database tables
    try:
        await init_db()
    except Exception as e:
        print(f"Database initialization warning: {e}")
    yield
    # Shutdown

app = FastAPI(
    title="DevOps Monitoring & Incident Response System",
    description="Comprehensive monitoring, alerting, and incident management system",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(monitoring.router, prefix="/api/v1/monitoring", tags=["monitoring"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["alerts"])
app.include_router(incidents.router, prefix="/api/v1/incidents", tags=["incidents"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "DevOps Monitoring System"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
