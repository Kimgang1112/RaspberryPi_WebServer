from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'home'

@app.route('/hello/')
def hello():
    return 'hello'


@app.route('/hi/')
def hi():
    return 'hi'

@app.route('/<name>')
def name(name):
    return f'hello {name}'

if __name__=="__main__":
    app.run(host='0.0.0.0')

print(__name__)
