import os

from flask_cors import CORS
from flask_talisman import Talisman


def configure_security(app):
    """Apply the required Talisman headers and CORS policy."""
    CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})
    Talisman(app, force_https=False, content_security_policy=False)
