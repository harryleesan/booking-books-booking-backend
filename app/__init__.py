from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from prometheus_flask_exporter import PrometheusMetrics
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
