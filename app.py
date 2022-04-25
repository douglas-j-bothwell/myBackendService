from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'myBackendService 0.0.1 says Hello, Docker!'
