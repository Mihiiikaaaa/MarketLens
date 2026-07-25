from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logger import logger
from app.api.news import router as news_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Market Intelligence Platform",
)

app.include_router(health_router)
app.include_router(news_router)

logger.info("MarketLens backend started.")