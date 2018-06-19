"""Micro service for Sesam applications that converts data to base64"""
import json
import base64
import os
import logging
from pprint import pprint
from flask import Flask, request, Response, abort

APP = Flask(__name__)

LOG_LEVEL = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))
logging.basicConfig(level=LOG_LEVEL)  # dump log to stdout
PAYLOAD_PROPERTY = os.environ.get('PAYLOAD_PROPERTY', 'entities')


@APP.route("/", methods=["GET", "POST"])
def encode_payload():
    """micro service entry point"""
    logging.info("Serving request from %s with content-type: %s", request.remote_addr,
                 request.content_type)
    if "application/json" == request.content_type or "text/plain" == request.content_type:
        payload_to_convert = request.get_json(force=True)
    else:
        abort(415)  # unsupported media type

    if not payload_to_convert:
        abort(500)

    return Response(
        generate_json(encode(payload_to_convert.get(PAYLOAD_PROPERTY).encode("utf-8"))),
        mimetype='application/json'
    )


def generate_json(data):
    """generates json entity that can be consumed by sesam instance"""
    return json.dumps({PAYLOAD_PROPERTY: data.decode("utf-8")})


def encode(data):
    """encode given data as base64"""
    return base64.b64encode(data)


def decode(base64_data):
    """decode base64 string"""
    return base64.b64decode(base64_data)


if __name__ == '__main__':
    logging.info("STarting service")
    APP.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('PORT', 5000))
