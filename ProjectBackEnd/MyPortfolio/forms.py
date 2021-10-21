from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from  wtforms.validators import DataRequired, Length, Email, ValidationError

class ContactForm(FlaskForm):

    full_name = StringField('Full Name', render_kw = {"placeholder": "Your name..."}, validators=[DataRequired(), Length(min=5, max=122)])
    email = StringField('E-mail', render_kw = {"placeholder": "Your e-mail..."}, validators=[DataRequired(), Email()])
    subject = StringField('Subject', render_kw = {"placeholder": "Subject..."})
    message = TextAreaField('Message', render_kw = {"placeholder": "Your message..."})
    submit = SubmitField('Send feedback')


    # def validate_email(self):
    #     if self.email.data == 'shukranrma@gmail.com':
    #         raise ValidationError(message='This email has already taken')


from app import Contact
