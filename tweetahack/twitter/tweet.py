import tweepy
from init_tweepy import InitTweepy

class Tweet:
    def __init__(self):
        self.api = InitTweepy().get_api()

    def post_tweet(self, tweet):
        self.api.update_status(status=tweet)

    def reply_to_tweet(self, tweet, status):
        self.api.update_status(status="@"+tweet.user.name+" "+status, in_reply_to_status_id=tweet.id)
