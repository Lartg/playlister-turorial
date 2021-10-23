from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html', msg='Flask is kinda cool I guess')

if __name__ == "__main__":
  app.run(debug=True)
