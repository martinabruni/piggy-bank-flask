from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators

class AccountForm(FlaskForm):
    """
    Form for creating a new account.

    Fields:
        name (StringField): Name of the account, required.
        initial_balance (FloatField): Initial balance for the account, optional.
    """
    name = StringField('Account Name', [
        validators.InputRequired(),
        validators.Length(min=1, max=100)
    ])
    initial_balance = FloatField('Initial Balance', [
        validators.Optional(),
        validators.NumberRange(min=0.0)
    ])
