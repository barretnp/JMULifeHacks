from flask import Flask
app = Flask(__name__)

from database import db_session
from models import Hack

@app.route("/")
def hello():
    return "<h1>MUTHA FUCKA</h1>"

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
