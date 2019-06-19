from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# test for about page
testData = {'username': 'Ryan'}


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ryan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Cool, you are learning Flask!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I bet no Feathren will read this.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/about')
def about():
    return render_template('about.html', user=testData)