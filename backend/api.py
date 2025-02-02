from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.fact_checker import check_misinformation
from backend.twitter_utils import fetch_tweet_text

# Initialize FastAPI app
app = FastAPI()

class TextRequest(BaseModel):
    text: str

class TweetRequest(BaseModel):
    tweet_url: str

@app.post("/check-text/")
async def check_text(request: TextRequest):
    """Receive text and return fact-check result"""
    result = check_misinformation(request.text)
    return {"fact_check_result": result}

@app.post("/check-tweet/")
async def check_tweet(request: TweetRequest):
    """Receive tweet URL and return fact-check result"""
    tweet_text = fetch_tweet_text(request.tweet_url)
    if "Error" in tweet_text:
        raise HTTPException(status_code=400, detail="Invalid tweet URL")
    result = check_misinformation(tweet_text)
    return {"tweet_text": tweet_text, "fact_check_result": result}
