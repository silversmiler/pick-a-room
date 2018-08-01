"""
export FLASK_APP=web.py
flask run
- OR -
pipenv install gunicorn
gunicorn web:app
"""
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    bob = '<p><a href="bob">bob</a></p>'
    pam = '<p><a href="pickroom">Pick-a-Room</a></p>'
    sue = '<p><a href="sue">sue</a></p>'
    output = '<p>Hello, World!</p>'+bob+pam+sue
    return output

@app.route('/pickroom')
def hello_bob():
    All = ['office'] * 5 + ['bathroom/closet/foyer'] * 3 + ['library'] * 3 + ['living room'] * 5 + \
        ['dining room'] * 3 + ['kitchen eating area'] * 5 + ['kitchen'] * 5 + ['pantry'] + ['shoe closet'] + \
        ['garage'] + ['front porch'] + ['back porch upper'] + ['back porch lower'] + ['Sarah room and bathroom'] * 3 + \
        ['Sarah study'] * 3 + ['master bath and closet'] * 3 + ['laundry/hall/stairs'] * 2 + \
        ['guest room and bathroom'] * 3 + ['master bedroom and sitting'] * 3 + ['basement TV'] * 2 + \
        ['basement living/hall/bathroom'] + ['basement front bed and closet'] + ['basement back bed'] + ['workshop']
    y = random.randrange(len(All))
    return All[y]

@app.route('/sue')
def sue():
    return 'Hello, sue!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
