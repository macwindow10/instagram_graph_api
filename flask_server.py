from flask import Flask, render_template, redirect, url_for, request, session
from insights import getAllPost, getCreds

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    credential_params = getCreds()
    posts = getAllPost()
    return render_template('index.html',
                           instagram_username=credential_params['ig_username'],
                           posts=posts,
                           message='social media automation server is running')


if __name__ == '__main__':
    app.run(debug=True)
