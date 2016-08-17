from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from rollforbugs_website import fortune
from rollforbugs_website import render_markdown

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
# Add custom symbols to Jinja
app.jinja_env.globals.update(get_fortune=fortune.get_fortune)
app.jinja_env.globals.update(markdown=render_markdown.render_markdown)


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
    return fortune.get_fortune()


if __name__ == '__main__':
    app.run()
