
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
        repo = git.Repo(os.getcwd() + '/mysite')
        origin = repo.remotes.origin

        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
    	path = os.getcwd()
        return 'Hello from Git42!'.format(path)

if __name__ == '__main__':
    app.run()