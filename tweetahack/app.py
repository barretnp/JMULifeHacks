from flask import Flask
app = Flask(__name__)

from database import db_session
from models import Hack
from ngrams import build_bad_advice
from flask import jsonify, send_from_directory

@app.route("/")
def hello():
    return send_from_directory('templates', 'index.html')

@app.route("/build_hack")
def build_hack():
    return jsonify({'hack':build_bad_advice(db_session), 'category':'lifehacks'})

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
    app.run(host='0.0.0.0', port=8080)
