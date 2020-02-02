"""
# ----------------------------------------------------------------------
forms.py

WTForms Validator documentation:
https://wtforms.readthedocs.io/en/stable/validators.html
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, InputRequired, Email, Length

"""
class SignupForm(Form):
    first_name = StringField('First Name', [InputRequired("First name is required")])
    last_name = StringField('Last Name', [InputRequired("Last name is required")])

    Per documentation: Validates an email address. Note that this uses a very primitive regular expression
    and should only be used in instances where you later verify by other means,
    such as email activation or lookups.

    email = StringField("Email", [InputRequired("Email is required"), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Passwords must be 6 chars or more")])
    submit = SubmitField('Sign me up!')
"""

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired("You must enter your first name!")])
    last_name = StringField('Last Name', validators=[DataRequired("You must enter your last name!")])
    """
    Per documentation: Validates an email address. Note that this uses a very primitive regular expression
    and should only be used in instances where you later verify by other means,
    such as email activation or lookups.
    """
    birthdate = DateField('birthdate', format='%Y-%m-%d')
    email = StringField("Email", [InputRequired("Please enter your email address"), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Passwords must be 6 chars or more")])
    submit = SubmitField('Sign me up!')
