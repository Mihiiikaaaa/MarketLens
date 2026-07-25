from dateutil import parser
from sqlalchemy.orm import Session

from app.models.news import NewsArticle
from app.services.news_service import fetch_news


def ingest_news(
    db: Session,
    query: str,
):

    articles = fetch_news(query)

    count = 0

    for article in articles:

        exists = (
            db.query(NewsArticle)
            .filter(
                NewsArticle.url == article["url"]
            )
            .first()
        )

        if exists:
            continue

        news = NewsArticle(
            title=article["title"] or "",
            source=article["source"]["name"],
            url=article["url"],
            content=article["content"] or "",
            published_at=parser.parse(
                article["publishedAt"]
            ),
        )

        db.add(news)

        count += 1

    db.commit()

    return count