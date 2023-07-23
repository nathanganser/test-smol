from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import configurations
from config import Config

# Initialize the Flask application
app = Flask(__name__)

# Load configurations
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after creating the app and db to avoid circular imports
from app import routes
