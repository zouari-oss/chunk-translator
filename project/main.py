from app.core.config import settings
from fastapi import FastAPI
from app.routers import translate

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


# Include routers
app.include_router(translate.router)


# Add Stander routes
@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.VERSION}


@app.get("/")
def root():
    return {"message": "Welcome to Chunck Translator API"}
