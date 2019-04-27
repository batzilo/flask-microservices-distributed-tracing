"""The Gamma web service."""

import os
import flask
import logging
import requests


log = logging.getLogger(__name__)

app = flask.Flask(__name__)

delta_endpoint = os.environ.get("DELTA_ENDPOINT", None)
if not delta_endpoint:
    raise RuntimeError("Please set the DELTA_ENDPOINT environment variable")


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/spam", methods=["POST"])
def handle_spam():
    """Get some data from delta."""
    if "X-Request-ID" in flask.request.headers:
        flask.g.request_id = flask.request.headers["X-Request-ID"]

    log.info("Gamma /spam called")

    log.info("Requesting data from delta ...")
    resp = requests.get("%s/delta" % delta_endpoint,
                        headers={"X-Request-ID": flask.g.request_id})
    log.info("Delta responded with status code %s and data `%s'",
             resp.status_code, resp.json())

    return flask.jsonify(spam=["ham", "eggs"], delta=resp.json())


log.info("The Gamma web service is ready and waiting for requests")
