from cProfile import run
from flask import Flask
from config import Config
from extensions import db
from flask_restful import Api

app = Flask(__name__)

# Configuration 
app.config.from_object(Config)

db.init_app(app)


api = Api(app, version="1.0", title="Flask Api Todos an Notes")


if __name__ == "__main__":
    app.run(port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG)