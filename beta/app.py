"""The Beta web service."""

import beta
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = beta.app
