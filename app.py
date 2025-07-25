from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def about():
    return render_template('index.html')


@app.route('/projetos')
def projects():
    return render_template('index.html')


@app.route('/contato')
def contact():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
