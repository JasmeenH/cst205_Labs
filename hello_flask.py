from flask import Flask,render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2
@app.route('/')
def hello():
  return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
   s1 = '<p>Genevieve M. : afaik</p> '
   s2 = 'Have a nice day!'
   return s1 + s2

# Task 3
@app.route('/jasmeen')
def t_test():
   return render_template('template.html')
