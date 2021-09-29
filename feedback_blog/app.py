from flask import Flask, app, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from forms import FeedbackForm


app = Flask(__name__)
app.config['SECRET-KEY'] = 'JAGCS8UPIQHOhsgdx7a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'

db = SQLAlchemy(app)

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False)
	message = db.Column(db.String(147), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
	    return f"Customer('{self.username}', '{self.message}')"	

@app.route('/feedback', methods = ['POST', 'GET'])
def feedback():
	form = FeedbackForm
	return render_template('index.html', form=form)

if __name__== '__main__':
	app.run(debug=True)
