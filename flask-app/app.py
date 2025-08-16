from flask import Flask
import os

app = Flask(__name__)
@app.route('/')
def wish():
    return "Hello, World! This is a Flask app running on Google Cloud Build."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))