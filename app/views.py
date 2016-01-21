from flask import render_template
from flask import send_from_directory
from app import app

items = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Brandon'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user,
                           items=items)


@app.route('/images')
def images():
    return render_template('images.html',
                           title='Images',
                           items=items)


@app.route('/profile/<id>')
def profile(id):
    return render_template('profile.html',
                           id=id,
                           item='two')


@app.route('/media/<regex("([\w\d_/-]+)?.(?:jpe?g|gif|png)"):filename>')
def media_file(filename):
    return send_from_directory(app.config['MEDIA_THUMBNAIL_FOLDER'], filename)
