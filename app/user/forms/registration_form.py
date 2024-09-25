from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, validators
from app.user.models.user import User


class registration_form(FlaskForm):
    """
    Registration form for creating a new user account.

    Fields:
        username (StringField): User's chosen username, required with length between 3 and 20 characters.
        email (StringField): User's email address, required and must be unique.
        pwd (PasswordField): User's password, required with a minimum length of 8 characters.
        cpwd (PasswordField): Confirmation of the password, must match 'pwd'.

    Methods:
        validate_email: Custom validator to check if the email is already registered.
        validate_uname: Custom validator to check if the username is already taken.
    """

    username = StringField(
        [
            validators.InputRequired(),
            validators.Length(3, 20, message="Please provide a valid name"),
            validators.Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(
        [validators.InputRequired(), validators.Email(), validators.Length(1, 64)]
    )
    pwd = PasswordField([validators.InputRequired(), validators.Length(8, 72)])
    cpwd = PasswordField(
        [
            validators.InputRequired(),
            validators.Length(8, 72),
            validators.EqualTo("pwd", message="Passwords must match !"),
        ]
    )

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

    def validate_uname(self, uname):
        if User.query.filter_by(username=uname.data).first():
            raise ValidationError("Username already taken!")
