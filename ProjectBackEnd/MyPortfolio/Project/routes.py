from flask import render_template, request, redirect, url_for
from flask_wtf import form
from werkzeug.utils import secure_filename
from . models import About,Portfolio, Testimonial,Blog,Contact,Admin
from Project import app,db,os,bcrypt,login_manager
from . forms import ContactForm,Adminlogin
from flask_login import login_user,login_required,logout_user
from flask_login import logout_user


@app.route('/')
def portfolio():
    aboutall=About.query.all() 
    length=len(aboutall)-1
    about=aboutall[length]
    portfolio=Portfolio.query.all() 
    blog=Blog.query.all() 
    testimonial=Testimonial.query.all() 
    form=ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect('contact')

    return render_template('home.html',portfolio=portfolio,aboutitem=about,blog=blog,testimonial=testimonial,form=form)


############################################ About #########################################################

@app.route('/admin/add-about', methods=['GET', 'POST'])
@login_required
def add_about():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        aboutitem = About(
          title = request.form.get('title'),
          text = request.form.get('text'),
          image = filename, 
          linkedin = request.form.get('linkedin'),
          github = request.form.get('github'),
          fb = request.form.get('fb')
        )
        db.session.add(aboutitem)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-about.html')


@app.route('/admin/about-list')
@login_required
def admin_about_list():
    about = About.query.all()
    return render_template('admin/about-list.html', about=about)


@app.route('/admin/edit-about/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_about(id):
    aboutitem = About.query.get_or_404(id)
    if request.method == 'POST':

        aboutitem.title = request.form.get('title')
        aboutitem.text = request.form.get('text')
        aboutitem.linkedin = request.form.get('linkedin')
        aboutitem.github = request.form.get('github')
        aboutitem.fb = request.form.get('fb')
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/edit-about.html', aboutitem=aboutitem)


@app.route('/admin/delete-about/<int:id>', methods=['GET','POST'])
@login_required
def delete_about(id):
    aboutitem = About.query.get_or_404(id)
    db.session.delete(aboutitem)
    db.session.commit()
    return redirect(url_for('portfolio'))


############################################ Portfolio #########################################################

@app.route('/admin/add-portfolio', methods=['GET', 'POST'])
@login_required
def add_portfolio():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        portwork = Portfolio(
          title = request.form.get('title'),
          link = request.form.get('link'),
          image = filename  
        )
        db.session.add(portwork)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-portfolio.html')
    

@app.route('/admin/portfolio-list')
@login_required
def admin_portfolio_list():
    portfolio = Portfolio.query.all()
    return render_template('admin/portfolio-list.html', portfolio=portfolio)


@app.route('/admin/edit-portfolio/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_portfolio(id):
    portwork = Portfolio.query.get_or_404(id)
    if request.method == 'POST':

        portwork.title = request.form.get('title')
        portwork.link = request.form.get('link')
        db.session.commit()
        return redirect(url_for('admin_portfolio_list'))
    return render_template('admin/edit-portfolio.html', portwork=portwork)


@app.route('/admin/delete-portfolio/<int:id>', methods=['GET','POST'])
@login_required
def delete_portfolio(id):
    portwork = Portfolio.query.get_or_404(id)
    db.session.delete(portwork)
    db.session.commit()
    return redirect(url_for('admin_portfolio_list'))


############################################ Testimonial #########################################################

@app.route('/admin/add-testimonial', methods=['GET', 'POST'])
@login_required
def add_testimonial():
    if request.method == 'POST':
        testimonialitem = Testimonial(
          text = request.form.get('text'),
          name = request.form.get('name'),
          job = request.form.get('job')
        )
        db.session.add(testimonialitem)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-testimonial.html')


@app.route('/admin/testimonial-list')
@login_required
def admin_testimonial_list():
    testimonial = Testimonial.query.all()
    return render_template('admin/testimonial-list.html', testimonial=testimonial)


@app.route('/admin/edit-testimonial/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_testimonial(id):
    testimonialitem = Testimonial.query.get_or_404(id)
    if request.method == 'POST':
        testimonialitem.text = request.form.get('text')
        testimonialitem.name = request.form.get('name')
        testimonialitem.job = request.form.get('job')
        db.session.commit()
        return redirect(url_for('admin_testimonial_list'))
    return render_template('admin/edit-testimonial.html', testimonialitem=testimonialitem)


@app.route('/admin/delete-testimonial/<int:id>', methods=['GET','POST'])
@login_required
def delete_testimonial(id):
    testimonialitem = Testimonial.query.get_or_404(id)
    db.session.delete(testimonialitem)
    db.session.commit()
    return redirect(url_for('admin_testimonial_list'))


############################################ Blog #########################################################

@app.route('/admin/add-blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blogitem = Blog(
          title = request.form.get('title'),
          text = request.form.get('text'),
          link = request.form.get('link'),
          image = filename  
        )
        db.session.add(blogitem)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-blog.html')


@app.route('/admin/blog-list')
@login_required
def admin_blog_list():
    blog = Blog.query.all()
    return render_template('admin/blog-list.html', blog=blog)


@app.route('/admin/edit-blog/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    blogitem = Blog.query.get_or_404(id)
    if request.method == 'POST':

        blogitem.title = request.form.get('title')
        blogitem.text = request.form.get('text')
        blogitem.link = request.form.get('link')
        db.session.commit()
        return redirect(url_for('admin_blog_list'))
    return render_template('admin/edit-blog.html', blogitem=blogitem)


@app.route('/admin/delete-blog/<int:id>', methods=['GET','POST'])
@login_required
def delete_blog(id):
    blogitem = Blog.query.get_or_404(id)
    db.session.delete(blogitem)
    db.session.commit()
    return redirect(url_for('admin_blog_list'))


############################################ Contact #########################################################

@app.route('/', methods=['GET', 'POST'])
# @login_required
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('/', form=form)


@app.route('/admin/contact-list')
@login_required
def admin_contact_list():
    form = Contact.query.all()
    return render_template('admin/contact-list.html', form=form)


@app.route('/admin/delete-contact/<int:id>', methods=['GET','POST'])
@login_required
def delete_contact(id):
    form = Contact.query.get_or_404(id)
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('admin_contact_list'))


############################################ Admin #########################################################

@app.route('/admin',methods=['GET','POST'])
def login():
    form=Adminlogin()
    if form.validate_on_submit():

        user=Admin.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('admin_about_list'))
        return redirect(url_for('login'))
    return render_template('admin/login.html',addata=form)


@app.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for('portfolio'))   


@app.route("/admin/loginadd",methods=['GET','POST'])
@login_required
def loginadd():
    
    form=Adminlogin()
    if form.validate_on_submit():
        user_row_password=form.password.data
        pas_hash=bcrypt.generate_password_hash(user_row_password).decode('utf-8')
        
        user=Admin(
            login=form.login.data,      
            password=pas_hash
        )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('admin/admincreatelog.html',form=form) 