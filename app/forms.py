from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, EqualTo


class AvengerInfoForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    avenger_name = StringField('Avenger Name', validators = [DataRequired()])
    phone_num = StringField('Phone Number', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()
