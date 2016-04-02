import logging
from database import db_session
from models import Hack, Submission, HackCorpus
from ngrams import build_bad_advice
from datetime import datetime
from flask import jsonify

def give_bad_advice(category='lifehacks'):
    return {'hack':build_bad_advice(db_session)}

def submit_hack(tweet_id=None, user=None, screen_name=None, category=None, tweet_contents=None,
		tags=None, url=None):
    created_at = datetime.now()
    post = Submission(tweet_id=tweet_id, user=user, screen_name=screen_name,
                      category=category, tweet_contents=tweet_contents, tags=tags,
                      url=rul)
    try:
        db_session.add(post)
        db_session.commit()
    except:
        logging.error("ERROR CREATING HACK")

def lookup_hacks(tags=[], operator='|'):
    """
    :param tags: List of hashtag tokens to be used as search terms
    :return : List of hack results
    """
    str_tags = tags
    if len(str_tags) > 1:
        search_terms = ' {} '.format(operator).join(str_tags).join(['\'', '\''])
    elif len(str_tags) == 1:
        search_terms = str_tags[0].join(['\'', '\''])
    if len(str_tags) == 0:
        res = None
    else:
        res = db_session.execute("SELECT * FROM hackcorpus WHERE " +
                                 "to_tsvector('english', text) @@ to_tsquery({})".format(search_terms))
    return [x for x in res]


def get_top():
    category = request.args['category']
    res = db_session.execute('SELECT * FROM submissions WHERE category == {} LIMIT 10' +
                             'ORDER BY DESC favorites')
