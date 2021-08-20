from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/<username>')
def hello_user(username):
    return f"Hello {escape(username)}!"

with app.test_request_context():
    print(url_for('hello_world'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
