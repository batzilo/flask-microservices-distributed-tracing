"""The Delta web service."""

import delta
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = delta.app
