import logging
from database import db_session
from models import Hack, Submission, HackCorpus
from ngrams import build_bad_advice

def build_hack():
    return jsonify({'hack':build_bad_advice(db_session), 'category':'lifehacks'})

def submit_hack():
    tweet_id = request.args['tweet_id']
    user = request.args['user']
    screen_name = request.args['screen_name']
    category = request.args['category']
    tweet_contents = request.args['tweet_contents']
    tags = request.args['tags']
    url = request.args['url']
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
        res1 = db_session.execute("SELECT * FROM hackcorpus WHERE " +
                                 "to_tsvector('english', text) @@ to_tsquery({})".format(search_terms))
        res2 = db_session.execute("SELECT * FROM submissions WHERE ARRAY{}::varchar[] && tags".format(str(str_tags)))
    res1 = [x for x in res1]
    res2 = [x for x in res2]
    return {'hackcorpus':res1, 'users':res2}

def get_top():
    category = request.args['category']
    res = db_session.execute('SELECT * FROM submissions WHERE category == {} LIMIT 10' +
                             'ORDER BY DESC favorites')
  

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
