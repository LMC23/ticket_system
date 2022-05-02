from flask import Flask
from flask_cors import CORS

from routes import users, auth

app = Flask(__name__)
# Enable cors for frontend app
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5501/", "https://www.google.ro"]}})

app.register_blueprint(users.users_blueprint)
app.register_blueprint(auth.auth_blueprint, url_prefix="/auth")


@app.route("/")
def hello():
    return "Hello world!"


# Only executed when calling the script directly
if __name__ == "__main__":
    app.run(debug=True)
