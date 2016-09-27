import os
import random
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from rollforbugs_website.utils import render_markdown

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
# Add custom symbols to Jinja
app.jinja_env.globals.update(markdown=render_markdown)

fortunes = []

# Load fortunes from file
fortune_file_name = app.config.get('FORTUNE_FILE', None)
if fortune_file_name and os.path.exists(fortune_file_name):
    f = open(fortune_file_name, 'r')
    for line in f:
        # Ignore empty lines
        line = line.strip()
        if not (line == ''):
            fortunes.append(line)
if len(fortunes) == 0:
    fortunes.append('No fortunes?!  How unfortunate...')


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/blog')
def blog_page():
    title = 'Blog'
    posts = [
        {
            'author': {'name': 'Elon Musk'},
            'body': 'Boy howdy Tesla is an amazing company!',
            'title': 'assert(Tesla == Awesome)',
            'created': '2016-08-16'
        },
        {
            'author': {'name': 'Elon Musk'},
            'body': '*Mmmm* gurl that SpaceX tho _oh yes_\nBring him home baby',
            'title': 'Fly me to ~~the moon~~ Mars',
            'created': '2016-08-15'
        }
    ]
    return render_template('blog.html', title=title, posts=posts)


@app.route('/about')
def about_page():
    title = 'About'
    return render_template('about.html', title=title)


@app.route('/fortune')
def fortune_api():
    return random.choice(fortunes)


@app.route('/projects/shitty-keyboard')
def projects_shitty_keyboard_page():
    title = 'Shitty Keyboard'
    return render_template('projects/shitty_keyboard.html', title=title)


if __name__ == '__main__':
    app.run()
