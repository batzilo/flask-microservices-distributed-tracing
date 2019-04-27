"""The Alpha web service."""

import os
import flask
import logging
import requests

import utils


log = logging.getLogger(__name__)

app = flask.Flask(__name__)

beta_endpoint = os.environ.get("BETA_ENDPOINT", None)
if not beta_endpoint:
    raise RuntimeError("Please set the BETA_ENDPOINT environment variable")

gamma_endpoint = os.environ.get("GAMMA_ENDPOINT", None)
if not gamma_endpoint:
    raise RuntimeError("Please set the GAMMA_ENDPOINT environment variable")


@app.before_request
def before_request():
    """Generate a unique request ID."""
    flask.g.request_id = utils.generate_request_id()


@app.after_request
def after_request(response):
    """Return the unique request ID."""
    response.headers["Request_ID"] = flask.g.request_id
    return response


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/foo", methods=["POST"])
def handle_foo():
    """Invoke beta and then gamma."""
    log.info("Alpha /foo called")

    data = {}

    data.update({"foo": "42"})

    log.info("Sending request to beta ...")
    resp = requests.post("%s/bar" % beta_endpoint,
                         headers={"X-Request-ID": flask.g.request_id})
    log.info("Beta responded with status code %s and data `%s'",
             resp.status_code, resp.json())

    data.update(resp.json())

    log.info("Sending request to gamma ...")
    resp = requests.post("%s/spam" % gamma_endpoint,
                         headers={"X-Request-ID": flask.g.request_id})
    log.info("Gamma responded with status code %s and data `%s'",
             resp.status_code, resp.json())

    data.update(resp.json())

    log.info("The overall response is `%s'", data)

    return flask.jsonify(data=data)


log.info("The Alpha web service is ready and waiting for requests")
