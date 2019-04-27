"""The Gamma web service."""

import gamma
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = gamma.app
