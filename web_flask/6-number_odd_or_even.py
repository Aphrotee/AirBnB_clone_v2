#!/usr/bin/python3
"""
This a script that starts a Flask web application
"""

from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Returns string when queried"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns string when queried"""
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """Returns string when queried"""
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_route(text='is_cool'):
    """Returns string when queried"""
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>')
def number(n):
    """Returns string when queried"""
    n = int(n)
    return '%s is a number' % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """Returns string when queried"""
    n = int(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Returns string when queried"""
    n = int(n)
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
