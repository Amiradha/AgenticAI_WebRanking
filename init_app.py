from flask import Flask
from routes import bp

def init_app(app: Flask):
    app.register_blueprint(bp)