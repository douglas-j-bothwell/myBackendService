from flask import Flask
beapp = Flask(__name__)

@beapp.route('/')
def hello_world():
    return 'myBackendService 1.2.6 says Hello, Docker!'
