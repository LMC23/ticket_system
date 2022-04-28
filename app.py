from flask import Flask
from flask_cors import CORS

from routes import users

app = Flask(__name__)
# Enable cors for frontend app
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5501/", "https://www.google.ro"]}})

app.register_blueprint(users.users_blueprint)


@app.route("/")
def hello():
    return "Hello world!"


# Only executed when calling the script directly
if __name__ == "__main__":
    app.run(debug=True)
