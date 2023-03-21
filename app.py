from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'User info: {name} , {id}'


if __name__ == '__main__':
    app.run(debug=True)
