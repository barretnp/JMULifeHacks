import tweepy
from init_tweepy import InitTweepy
from mentions    import Mentions
class Tweet:
    def __init__(self):
        self.api      = InitTweepy().get_api()
        self.mentions = Mentions() 

    def post_tweet(self, tweet):
        self.api.update_status(status=tweet)

    def reply_to_tweets(self, tweets, status):
        for tweet in tweets:
            self.api.update_status(status="@"+tweet.user.screen_name+" "+status, in_reply_to_status_id=tweet.id)
