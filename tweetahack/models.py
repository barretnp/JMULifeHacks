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
    user = Column(String(50))
    screen_name = Column(String(100))
    category = Column(String(140))
    tweet_contents = Column(String(140))
    tags = Column(psarray(String(100)))
    url = Column(String(140))
    created_at = Column(psDateTime)
    
    def __init__(self, user=None, screen_name=None,
                 tweet_id=None, tweet_contents=None,
                 tags=None, category=None, url=None):
        self.user = user
        self.screen_name = screen_name
        self.category = category
	self.tweet_contents = tweet_contents
        self.tags = tags
        self.tweet_id = tweet_id
        self.created_at = datetime.now()
        

class Hack(Base):
    __tablename__ = 'hacks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(50))
    tags = Column(psarray(String(50)))
    name = Column(String(140))
    text = Column(String(140))

    def __init__(self, category=None, tags=None, name=None,
		 text=""):
        self.category=category
	self.tags=tags
	self.name=name
	self.text=text
	 
    
    def __repr__(self):
	return "<h1>{}</h1>".format(self.name)

class Category(Base):
    __tablename__='categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    tags = Column(psarray(String(50)))
    
    def __init__(self, name=None, tags=None):
        self.name = name
	self.tags = tags


class HackCorpus(Base):
    __tablename__='hackcorpus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category=Column(String(50))
    url = Column(String(500))
    link = Column(String(200))
    text=Column(String(2000))
    title=Column(String(1000))
    favorites=Column(Integer)

    def __init__(self, text="", category=None, url="", title="", favorites=0):
        self.title=title
        self.favorites=favorites
        self.text=text
        self.category=category
	self.url=url
