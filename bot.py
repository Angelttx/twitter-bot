"""
Twitter Bot Template
"""
import tweepy
from config import CONFIG

# Setup
client = tweepy.Client(
    bearer_token=CONFIG['bearer_token'],
    consumer_key=CONFIG['api_key'],
    consumer_secret=CONFIG['api_secret'],
    access_token=CONFIG['access_token'],
    access_token_secret=CONFIG['access_token_secret']
)

# Post a tweet
def tweet(message):
    response = client.create_tweet(text=message)
    print(f"Tweeted: {message}")
    return response

# Like a tweet
def like(tweet_id):
    client.like(tweet_id)
    print(f"Liked tweet {tweet_id}")

# Follow a user
def follow(user_id):
    client.follow_user(user_id)
    print(f"Followed user {user_id}")

if __name__ == "__main__":
    tweet("Hello from my Twitter Bot! 🤖")
