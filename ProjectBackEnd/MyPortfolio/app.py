from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

app = Flask(__name__)
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/images/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SECRET_KEY'] = '1234terfsdghjykutyo675645yergfre4547o87967-+-'
db = SQLAlchemy(app)
migrate=Migrate(app,db)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(10), nullable=False)
    text=db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(20))
    # linkedin-link=db.Column(db.String(100))
    # github-link=db.Column(db.String(100))
    # ig-link=db.Column(db.String(100))
    # fb-link=db.Column(db.String(100))
    # twitter-link=db.Column(db.String(100))

    def __repr__(self):
        return f'About me: {self.title}'


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20))
    

    def __repr__(self):
        return f'My portfolio: {self.title}'


class Testimonal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.String(100), nullable=False)
    name=db.Column(db.String(20), nullable=False)
    job=db.Column(db.String(20))
    

    def __repr__(self):
        return f'Testimonals: {self.title}'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    text=db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(20))
    

    def __repr__(self):
        return f'My Blog: {self.title}'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    number=db.Column(db.String(20))
    email=db.Column(db.String(20), nullable=False)
    subject=db.Column(db.String(20), nullable=False)
    message=db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'My Blog: {self.title}'




@app.route('/')
def portfolio():
    about=About.query.get(1) 
    portfolio=Portfolio.query.all() 
    blog=Blog.query.all() 
    testimonal=Testimonal.query.all() 
    print(about)

    return render_template('home.html',portfolio=portfolio,aboutitem=about,blog=blog,testimonal=testimonal)

@app.route('/admin/portfolio-list')
def admin_portfolio_list():
    portfolio = Portfolio.query.all()
    return render_template('admin/portfolio-list.html', portfolio=portfolio)



############################################ ADMIN PANEL #########################################################

@app.route('/admin/add-about', methods=['GET', 'POST'])
def add_about():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        aboutitem = About(
          title = request.form.get('title'),
          text = request.form.get('text'),
          image = filename  
        #   linkedin-link = request.form.get('linkedin-link')
        )
        db.session.add(aboutitem)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-about.html')




@app.route('/admin/add-portfolio', methods=['GET', 'POST'])
def add_portfolio():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        portwork = Portfolio(
          title = request.form.get('title'),
          image = filename  
        )
        db.session.add(portwork)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-portfolio.html')
    

@app.route('/admin/edit-portfolio/<int:id>/', methods=['GET', 'POST'])
def edit_portfolio(id):
    portwork = Portfolio.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        portwork.title = request.form.get('title')
        portwork.image = filename
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/edit-portfolio.html', portwork=portwork)


@app.route('/admin/delete-portfolio/<int:id>', methods=['GET','POST'])
def delete_portfolio(id):
    portwork = Portfolio.query.get_or_404(id)
    db.session.delete(portwork)
    db.session.commit()
    return redirect(url_for('portfolio'))




@app.route('/admin/add-testimonal', methods=['GET', 'POST'])
def add_testimonal():
    if request.method == 'POST':
        testimonalsitem = Testimonal(
          text = request.form.get('testimonal'),
          name = request.form.get('title'),
          job = request.form.get('job')
        )
        db.session.add(testimonalsitem)
        db.session.commit()
        return redirect(url_for('blog'))
    return render_template('admin/add-testimonal.html')


@app.route('/admin/add-blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blogitem = Blog(
          title = request.form.get('title'),
          text = request.form.get('short-text'),
          image = filename  
        )
        db.session.add(blogitem)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-blog.html')

   
@app.route('/contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        person = Contact(
          name = request.form.get('name'),
          number = request.form.get('number'),
          email = request.form.get('email'),
          subject = request.form.get('subject'),
          message = request.form.get('message'),
        )
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('contact'))
    # return render_template('admin/add-portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)

