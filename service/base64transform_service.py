"""Micro service for Sesam applications that converts data to base64"""
import json
import base64
import os
import logging

from flask import Flask, request, Response

APP = Flask(__name__)

LOG_LEVEL = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))
logging.basicConfig(level=LOG_LEVEL) # dump log to stdout


@APP.route("/", methods=["GET"])
def encode_payload():
    """micro service entry point"""
    logging.info("Serving request from %s", request.remote_addr)
    payload_to_convert = request.data
    return Response(
        generate_json(encode(payload_to_convert)),
        mimetype='application/json'
    )


def generate_json(data):
    """generates json entity that can be consumed by sesam instance"""
    return json.dumps({"_id": data.decode("utf-8")})


def encode(data):
    """encode given data as base64"""
    return base64.b64encode(data)


def decode(base64_data):
    """decode base64 string"""
    return base64.b64decode(base64_data)


if __name__ == '__main__':
    logging.info("STarting service")
    APP.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('PORT', 5000))
