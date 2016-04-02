import tweepy
from init_tweepy import InitTweepy
from mentions    import Mentions
from models      import * 
from database    import db_session
from sqlalchemy  import literal

class Tweet:    
    def __init__(self, count=5):
        self.api      = InitTweepy().get_api()
        self.mentions = Mentions(self.api) 
        self.since_id = 1 
        self.count = count

    def post_tweet(self, tweet):
        self.api.update_status(status=tweet)

    def reply_to_tweets(self, replies):
        for (tweet, status) in replies:
            self.api.update_status(status="@"+tweet.user.screen_name+" "+status, in_reply_to_status_id=tweet.id)

    def get_and_reply(self):
        #grab most recent tweets at tweetahack
        tweets = self.mentions.get_mentions(since=self.since_id, count=self.count)
        if len(tweets) > 0:
            #update since_id for the most recently accessed mention
            self.since_id = tweets[0].id
            
            replies = []

            for tweet in tweets:
            #query db
                try:
                    query = db_session.query(HackCorpus).filter(HackCorpus.category==tweet.text.split()[1])
                    if db_session.query(literal(True)).filter(query.exists()).scalar():
                        replies.append((tweet, "you said a magic word, I hope"))
                except:
                    pass

#            print replies
            self.reply_to_tweets(replies)
