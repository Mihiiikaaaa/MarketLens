from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.news_ingestion import ingest_news

router = APIRouter()


@router.post("/news/ingest")
def ingest(
    query: str,
    db: Session = Depends(get_db),
):

    total = ingest_news(
        db,
        query,
    )

    return {
        "inserted": total
    }