# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(message="Movie title is required.")])
    description = TextAreaField('Movie Description', validators=[DataRequired(message="Description is required.")])
    poster = FileField('Movie Poster', validators=[
        FileRequired(message="A poster image is required."),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], message="Only image files (jpg, jpeg, png, gif) are allowed.")
    ])
# Add any form classes for Flask-WTF here
