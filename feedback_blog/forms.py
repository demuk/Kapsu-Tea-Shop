from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class FeedbackForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	message = StringField('message', validators=[DataRequired()])
	submit = SubmitField('Send')

	