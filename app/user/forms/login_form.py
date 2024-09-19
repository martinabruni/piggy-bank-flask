from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, validators


class login_form(FlaskForm):
    email = StringField(
        [validators.InputRequired(), validators.Email(), validators.Length(1, 64)]
    )
    pwd = PasswordField([validators.InputRequired(), validators.Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username = StringField([validators.Optional()])
