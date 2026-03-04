from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Cloud Run!"

@app.route("/health")
def health():
    return "Service is running"