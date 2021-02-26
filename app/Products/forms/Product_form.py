from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])
    price = IntegerField('price',validators=[DataRequired()])
    color = StringField('color',validators=[DataRequired()])
    description = TextAreaField('description',validators=[DataRequired()])
    category_id = IntegerField('category_id',validators=[DataRequired()])