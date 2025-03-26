from flask import Flask,render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2
@app.route('/')
def hello():
  return '<h1>Hello world from Flask!</h1>'

@app.route('/welcome')
def wc():
   # I didn't ask anyone during class so I just made up
   s1 = '<p>Student 1: LOL (Laugh out Loud)</p> '
   s2 = '<p>Student 2: BRB (Be Right Back)</p>'
   return s1 + s2

# Task 3
@app.route('/jasmeen')
def t_test():
   return render_template('template.html')
