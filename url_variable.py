from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}."

@app.route('/user/<int:user_id>')
def get_get_profile(user_id):
    return f"Hi, your ID is {user_id}."

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Your subpath: {escape(subpath)}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
