from flask import Flask
import json

def create_app(environment="test"):
    app = Flask(__name__)
    if environment == "production":
        with open('./config_prod.json', "r") as f:
            print(f.read())
        app.config.from_json('./config_prod.json')
        port = 5000
    else:
        with open('./config_test.json', "r") as f:
            print(f.read())
        app.config.from_json("config_test.json")
        port = 5001
    with app.app_context():
        from . import views
        from . import apis
    return app

if __name__ == '__main__':
    create_app()


