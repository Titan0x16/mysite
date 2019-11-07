
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_sslify import SSLify
import git

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def hello_world():
    return 'Hello from Git27!'

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo()
        origin = repo.remotes.origin

        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    app.run()