"""The Delta web service."""

import flask
import logging

import epsilon


log = logging.getLogger(__name__)

app = flask.Flask(__name__)


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/delta")
def handle_delta():
    """Compute some values."""
    if "X-Request-ID" in flask.request.headers:
        flask.g.request_id = flask.request.headers["X-Request-ID"]

    log.info("Delta /delta called")

    log.info("Creating an epsilon object ...")
    e = epsilon.Epsilon()
    log.info("Successfully created an epsilon object")

    log.info("Initiating computation ...")
    e.compute()
    log.info("Successfully computed data")

    return flask.jsonify(delta=e.data)


log.info("The Delta web service is ready and waiting for requests")
