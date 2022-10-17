from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                           message='social media automation server is running')


if __name__ == '__main__':
    app.run(debug=True)
