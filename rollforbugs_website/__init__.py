from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
@app.route('/index')
def render_index():
    return render_template('index.html')


@app.route('/blog')
def render_blog():
    return render_template('blog.html')


@app.route('/about')
def render_about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
