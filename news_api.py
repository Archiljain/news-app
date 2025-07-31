import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

Base_url = "https://newsapi.org/v2"

def get_top_headlines():
    url = f"{Base_url}/top-headlines?"
    param = {
        "country": "in",
        "apikey": API_KEY,
        "pagesize": 10
    }
    response = requests.get(url, params=param)
    return response.json().get("articles", [])
def search_news(query):
    url = f"{Base_url}/everything"
    param = {
        "q": query,
        "apikey": API_KEY,
        "language": "en",
        "pagesize": 10
    }
    response = requests.get(url, params=param)
    return response.json().get("articles", [])
