import tweepy
class Mentions:

    def __init__(self):
        consumer_key = 'msGHNyOrL3JMHVW8LJqo7qiql'
        consumer_secret = 'CdyLn42TEbNMiwLK6mGbXBq4O4dyvtz6Jt1FdIHpM7IJm1uLbW'
        access_token = '716039483037257728-UnxLEVPC4aYBp0UzPQQloXqwc4k0sTy'
        access_token_secret = 'OokAlMSd7uh0CEDRqLlfGmuOLZgncyK1lUfaSzFqWW4m1'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def get_mentions(self, count=1, since=None):
        return self.api.mentions_timeline(since_id=since, count=count)

    def get_mention_id(self):
        return self.api.mentions_timeline(count=1)[0].id

    def process_nprevious(self, max_id, count=1):
        return self.api.mentions_timeline(max_id=(max_id-1), count=count)

    #def process_allprevious(self, max_id, rate=None):
     #   if len(process_nprevious(max_id)) > 0:
      #      return [].extend(process_allprevious())
       # else:
        #    return []
            
