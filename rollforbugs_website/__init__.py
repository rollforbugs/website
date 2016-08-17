from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from rollforbugs_website import fortune

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
# Add custom symbols to Jinja
app.jinja_env.globals.update(get_fortune=fortune.get_fortune)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/blog')
def blog_page():
    title = 'Blog'
    return render_template('blog.html', title=title)


@app.route('/about')
def about_page():
    title = 'About'
    return render_template('about.html', title=title)


@app.route('/fortune')
def fortune_api():
    return fortune.get_fortune()


if __name__ == '__main__':
    app.run()
