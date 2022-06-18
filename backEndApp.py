from flask import Flask
beapp = Flask(__name__)

@beapp.route('/')
def hello_world():
    return 'myBackendService 0.0.1 says Hello, Docker!'
