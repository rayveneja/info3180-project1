from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class AddPropertiesForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    num_rooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    num_baths = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Townhouse', 'Townhouse')])
    location =StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])