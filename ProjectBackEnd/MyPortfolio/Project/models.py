from Project import db,login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(10))
    text=db.Column(db.String(500))
    image = db.Column(db.String(20))
    linkedin=db.Column(db.String(100))
    github=db.Column(db.String(100))
    fb=db.Column(db.String(100))
    # twitter=db.Column(db.String(100))

    def __repr__(self):
        return f'About me: {self.title}'


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(1), nullable=False)
    link=db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(20))
    

    def __repr__(self):
        return f'My portfolio: {self.title}'


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.String(100), nullable=False)
    name=db.Column(db.String(20), nullable=False)
    job=db.Column(db.String(20))
    

    def __repr__(self):
        return f'Testimonials: {self.name}'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    text=db.Column(db.String(100), nullable=False)
    link=db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(20))
    

    def __repr__(self):
        return f'My Blog: {self.title}'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(20), nullable=False)
    message=db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f'My Blog: {self.email}'


class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login= db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f'Admin: {self.login}'