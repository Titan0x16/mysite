
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_sslify import SSLify
import git
import os

app = Flask(__name__)
sslify = SSLify(app)

# @app.route('/')
# def hello_world():
#     return 'Hello from Git28!'

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
    	filepath = os.path.abspath(os.path.dirname(__file__))
    	repo = git.Repo(filepath)
    	origin = repo.remotes.origin

    	origin.pull()
    	return 'Updated PythonAnywhere successfully', 200
    else:
    	path = os.getcwd()
    	path2 = os.path.abspath(os.path.dirname(__file__))
    	return f'Hello from Git47! {path} {path2}'

if __name__ == '__main__':
    app.run()