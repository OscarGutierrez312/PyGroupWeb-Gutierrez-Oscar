from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired()])
    price = IntegerField('Price',validators=[DataRequired()])
    marca = StringField('Mark',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    category_id = IntegerField('Category_id',validators=[DataRequired()])