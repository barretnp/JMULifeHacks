import tweepy

class Mentions:

    def __init__(self, api):
        self.api = api

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
            
