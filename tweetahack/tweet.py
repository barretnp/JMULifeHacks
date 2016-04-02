import tweepy
import re
import app
import random
import math
from init_tweepy import InitTweepy
from mentions    import Mentions
from models      import HackCorpus 
from database    import db_session
from sqlalchemy  import literal
from detect      import classify

class Tweet:    
    def __init__(self, count=5, since_id=1):
        self.api      = InitTweepy().get_api()
        self.mentions = Mentions(self.api) 
        self.since_id = since_id
        self.count = count

    def parse(self, text=None):
        if text == None:
            return None
        return text.replace('@tweetahack', '').replace('#', '')
                 
    def post_tweet(self, tweet):
        self.api.update_status(status=tweet)

    def mention_response(self, tweet, string):
        self.api.update_status(in_reply_to_status_id=tweet.id, status= u'@'+ (unicode(str(tweet.user.screen_name))+ u' ' + unicode(string)))

    def reply_to_tweets(self, replies):
        for (tweet, status) in replies:
            self.mention_response(tweet, status)

    def getRandomHack(self, hack_list):
        index = int(math.floor(random.random() * len(hack_list)))
        return hack_list[index]
        

    def maintain(self):
        #grab most recent tweets at tweetahack
        tweets = self.mentions.get_mentions(since=self.since_id, count=self.count)
        if len(tweets) > 0:
            #update since_id for the most recently accessed mention
            self.since_id = tweets[0].id
            
            replies = []

            for tweet in tweets:
                if len(tweet.entities['hashtags']) > 0 and reduce(lambda x, y: x | y, [hashtag['text'] == 'submit' for hashtag in tweet.entities['hashtags']]):
                    #make postgre object using parsed body of tweet (removed @... and #) with id and tags as array. 
                    clean_text = self.parse(tweet.text.replace('#submit',''))
                    if clean_text != None:
                        #if tweet.contributors is not None:
                           #screen_name = tweet.contributors[0]['screen_name']
                        #else:
                        #screen_name = "None"
                        #hashtags = tweet.entities['hashtags']
                        #tweet_id = tweet.id
		        #tweet_contents = tweet.text
      			#urls = tweet.entities['urls']
                        #self.submit(hashtags, tweet_id, urls, screen_name, tweet_contents)
                        self.mention_response(tweet, 'your submission has been noted')
                
                else: #user want's hack
                    search_text = tweet.text.replace('@tweetahack', '')
                    #self.mention_response(tweet, 'Searching for ' + search_text + ' now!')
		    hashtags = map( lambda x: x['text'] if x['text'] is not 'submit' else None, tweet.entities['hashtags'])
                    
                    result = []

                    if len(hashtags) > 0: 
                       result = app.lookup_hacks(hashtags, operator = "&")
   
                       if len(result) == 0:
                       	    result = app.lookup_hacks(hashtags, operator = "|")
                       
		       	    if len(result) == 0:
                        	  result = ["Sorry no results found"]
		       
		    
		       replies.append((tweet, self.getRandomHack(result)))
	    
		    else:
		       print "nick barret dcuks"
	self.reply_to_tweets(replies)
		




                   # r = requests.get('/search_hack', {'hashtags': hashtags}		    
