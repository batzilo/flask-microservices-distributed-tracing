"""The Alpha web service."""

import alpha
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = alpha.app
