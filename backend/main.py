from backend.fact_checker import check_misinformation
from backend.twitter_utils import fetch_tweet_text

def run_fact_checking_pipeline(text=None, tweet_url=None):
    """
    Function to run the fact-checking pipeline for either text or tweet URL.
    :param text: Text input (optional)
    :param tweet_url: Tweet URL (optional)
    :return: Fact-check result
    """
    if text:
        result = check_misinformation(text)
        return {"text": text, "fact_check_result": result}
    
    if tweet_url:
        tweet_text = fetch_tweet_text(tweet_url)
        if "Error" in tweet_text:
            return {"error": "Invalid tweet URL"}
        result = check_misinformation(tweet_text)
        return {"tweet_url": tweet_url, "tweet_text": tweet_text, "fact_check_result": result}

# Run a test if this script is executed directly
if __name__ == "__main__":
    # Sample test for text input
    text_input = "Some sample misinformation text here."
    print(run_fact_checking_pipeline(text=text_input))

    # Sample test for tweet URL input
    tweet_url_input = "https://twitter.com/someuser/status/123456789"
    print(run_fact_checking_pipeline(tweet_url=tweet_url_input))
