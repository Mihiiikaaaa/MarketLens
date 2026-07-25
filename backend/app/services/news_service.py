import requests

from app.core.config import settings


BASE_URL = "https://newsapi.org/v2/everything"


def fetch_news(query: str):

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
        "apiKey": settings.NEWS_API_KEY,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=20,
    )

    response.raise_for_status()

    return response.json()["articles"]