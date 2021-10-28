from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import PasswordInput

class ContactForm(FlaskForm):

    name = StringField('Full Name', render_kw = {"placeholder": "Your name..."}, validators=[DataRequired(), Length(min=5, max=122)])
    email = StringField('E-mail', render_kw = {"placeholder": "Your e-mail..."}, validators=[DataRequired(), Email()])
    message = TextAreaField('Message', render_kw = {"placeholder": "Your message..."})
    submit = SubmitField('Send')


class Adminlogin(FlaskForm):
    login=StringField('username',render_kw = {"placeholder": "login..."},validators=[DataRequired()])
    password=StringField('password',render_kw = {"placeholder": "password..."},validators=[DataRequired()],widget=PasswordInput())
    submit=SubmitField('Send')