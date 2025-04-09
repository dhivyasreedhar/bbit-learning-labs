"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str

def format_article(article: dict) -> Article:
    """Format a dictionary into an Article dataclass."""
    return Article(
        author=article["author"],
        title=article["title"],
        body=article["body"],
        publish_date=datetime.fromisoformat(article["publish_date"]),
        image_url=article["image_url"],
        url=article["url"]
    )
def format_articles(articles: list[dict]) -> list[Article]:
    """Format a list of dictionaries into a list of Article dataclasses."""
    return [format_article(article) for article in articles]




def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    redis_client = None  
    # Assuming redis_client is defined and connected
    articles = redis_client.lrange("articles", 0, -1)
    if articles:
        return format_articles([eval(article) for article in articles])
    # If no articles are found, return an empty list
    else:
        return []
    
    



def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date
    articles = get_all_news()
    if articles:
        # Sort articles by publish_date in descending order
        sorted_articles = sorted(articles, key=lambda x: x.publish_date, reverse=True)
        # Return the most recent article
        return sorted_articles[0]
    # If no articles are found, return None
    else:
        return None
