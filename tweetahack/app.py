from flask import Flask
app = Flask(__name__)

import logging
from database import db_session
from models import Hack, Submission, HackCorpus
from ngrams import build_bad_advice
from flask import jsonify, request

@app.route("/")
def hello():
    return "<h1>MUTHA FUCKA</h1>"

@app.route("/build_hack")
def build_hack():
    return jsonify({'hack':build_bad_advice(db_session), 'category':'lifehacks'})

@app.route("/submit_hack")
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

@app.route("/search_hack")
def lookup_hack():
    category = request.args['category']
    text = request.args['text']
    user = request.args['user']
    

@app.route("/add_hack")
def add_hack():
   test_hack = Hack(category='Balls', tags=['Left', 'Right', '', '','','','','','',''], name='Liam',
		    url='http://lemonparty.com', description='fucccccck',
		    location = ['north','west'])
   db_session.add(test_hack)
   db_session.commit()
   return str(db_session.query(Hack).first())


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
