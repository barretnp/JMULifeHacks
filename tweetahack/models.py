from sqlalchemy import Column, Integer, String 
from sqlalchemy.dialects.postgresql import ARRAY  as psarray
from sqlalchemy.types import DateTime as psDateTime
from database import Base
from datetime import datetime
import json


class Submission(Base):
    __tablename__ = 'submissions'
    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer)
    coordinates = Column(String(100))
    user = Column(String(50))
    screen_name = Column(String(100))
    category = Column(String(140))
    tweet_contents = Column(String(140))
    tags = Column(psarray(String(10)))
    url = Column(String(140))
    created_at = Column(psDateTime)
    
    def __init__(self, user=None, tweet_id=None, tweet_contents=None,
                  tags=None, category=None, url=None):
        self.user = user
        self.category = category
	self.tweet_contents=tweet_contents

class Hacks(Base):
    __tablename__ = 'hacks'
    id = Column(Integer, primary_key=True)
    category = Column(String(50))
    tags = Column(psarray(String(10)))
    name = Column(String(140))
    url = Column(String(140))
    description = Column(String(300))
    popularity = Column(Integer)
    location = Column(psarray(String(2)))

    def __init__(self, category=None, tags=None, name=None,
		 url=None, description=None, popularity=1, location=None):
        self.category=category
	self.tags=tags
	self.name=name
	self.url=url
	self.description=description
	self.popularity=popularity
	self.location=location 
    
    def __repr__():
	return json.loads(dict(self._fields))

