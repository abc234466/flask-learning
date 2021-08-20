from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return 'You are trying to login the website!'

def show_the_login_form():
    return 'Login forms'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)