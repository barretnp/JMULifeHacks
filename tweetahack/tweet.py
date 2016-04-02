import tweepy
from init_tweepy import InitTweepy
from mentions    import Mentions
from models      import Hacks 
from database    import db_session


class Tweet:
    def __init__(self, count=5):
        self.api      = InitTweepy().get_api()
        self.mentions = Mentions(self.api) 
        self.since_id = 1 
        self.count = count

    def post_tweet(self, tweet):
        self.api.update_status(status=tweet)

    def reply_to_tweets(self, tweets, status):
        for tweet in tweets:
            self.api.update_status(status="@"+tweet.user.screen_name+" "+status, in_reply_to_status_id=tweet.id)

    def get_and_reply(self):
        #grab most recent tweets at tweetahack
        tweets = self.mentions.get_mentions(since=self.since_id, count=self.count)
        if len(tweets) > 0:
            #update since_id for the most recently accessed mention
            self.since_id = tweets[0].id
            
            for tweet in tweets:
            #query db
                print db_session.query().filter_by(category='budgetfood').get(1)           
                #self.reply_to_tweets(tweet, "testing out my new feature!")
