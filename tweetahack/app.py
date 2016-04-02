from flask import Flask
app = Flask(__name__)

from database import db_session
from models import Hack
from ngrams import build_bad_advice
from flask import jsonify

def build_hack():
    return jsonify({'hack':build_bad_advice(db_session), 'category':'lifehacks'})

def add_hack():
   db_session.add(test_hack)
   db_session.commit()
   return str(db_session.query(Hack).first())


def shutdown_session(exception=None):
    db_session.remove()
