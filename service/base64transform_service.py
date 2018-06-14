from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def encode_payload():
    payload_to_convert = request.data;
    return Response(
        encode(payload_to_convert),
        mimetype='application/base64'
    )


def encode(data):
    return base64.b64encode(data)


def decode(base64_data):
    return base64.b64decode(base64_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('PORT', 5001))
