import tweepy
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Twitter API keys from the .env file
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Set up Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def extract_tweet_id(tweet_url):
    """Extract tweet ID from a Twitter URL."""
    try:
        # Regex to capture tweet ID from various types of Twitter URLs
        tweet_id_match = re.search(r"status/(\d+)", tweet_url)
        if tweet_id_match:
            return tweet_id_match.group(1)
        else:
            return None
    except Exception as e:
        return None

def fetch_tweet_text(tweet_url):
    """Fetch tweet text using Twitter API."""
    tweet_id = extract_tweet_id(tweet_url)
    if not tweet_id:
        return "Invalid Twitter URL"
    
    try:
        tweet = client.get_tweet(tweet_id, tweet_fields=["text"])
        return tweet.data["text"] if tweet.data else "Tweet not found"
    except Exception as e:
        return f"Error fetching tweet: {e}"
