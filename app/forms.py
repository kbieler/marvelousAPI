from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    alias = StringField('Alias', validators=[DataRequired()])
    name = StringField('Full Name', validators=[DataRequired()])
    description = StringField('Description')
    comics_appear= StringField('Comic Appearances')
    super_power = StringField('Super Power(s)', validators=[DataRequired()])
    owner = StringField('Your API Token', validators=[DataRequired()])
    submit = SubmitField



