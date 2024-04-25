from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Mrs Loini is the best lecturer'
