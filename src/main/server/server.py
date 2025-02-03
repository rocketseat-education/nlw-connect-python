from flask import Flask
from src.main.routes.event import event_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
