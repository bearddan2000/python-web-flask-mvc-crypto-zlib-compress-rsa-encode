import json
from user import User
from security.encode import Encode
from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, logout_user, login_required

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
# app name

def unauthorized():
    return render_template('error.html', code="403"), 500

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'
login_manager.unauthorized_handler( unauthorized)

msg = ''
encoder = Encode()
userList = [User(0, 'admin', encoder)
            , User(1, 'super', encoder)
            , User(2, 'user', encoder)]

@login_manager.user_loader
def load_user(user_id):
    return next((x for x in userList if x.id == user_id), None)

@app.route('/', methods=['GET'])
def hello():
    return render_template(
    "index.html",
    err='',
    success=msg
    )

@app.route('/', methods=['POST'])
def login():
    info = request.form
    username = info.get('username', '')
    password = info.get('password', '')
    # password = encoder.hash_password(password)
    user = next((x for x in userList if x.name == username and encoder.verify(x.password, password)), None)

    if user:
        login_user(user)
        return render_template("protected.html")
    else:
        return render_template(
        "index.html",
        err="User: %s with password: %s not found" % (username, password),
        success=''
        )

@app.route('/logout', methods=['POST'])
def logout():
    msg="Logout successful"
    logout_user()

@app.route('/protected', methods=['GET'])
@login_required
def protected():
    return render_template("protected.html")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
