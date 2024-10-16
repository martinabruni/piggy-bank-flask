from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, validators


class LoginForm(FlaskForm):
    """
    Login form for user authentication.

    Fields:
        email (StringField): User's email address, required and must be a valid format.
        pwd (PasswordField): User's password, required with a length between 8 and 72 characters.
    """

    email = StringField(
        [validators.InputRequired(), validators.Email(), validators.Length(1, 64)]
    )
    pwd = PasswordField([validators.InputRequired(), validators.Length(min=8, max=72)])
