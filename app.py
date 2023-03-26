from flask import Flask, jsonify, request

import requests
import os

app = Flask(__name__)
DEBUG = True
THREADED = True
PORT = 8080


@app.route('/')
def n3twatch_homepage():
    return '<p>Hello, World!</p>', 200


@app.route("/dwn", methods=["POST"])
def n3twatch_download_catcher():
    file = request.json
    print("New File Downloaded:", file.get("path"))

    return jsonify({}), 200


def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', PORT))
    app.run(debug=DEBUG, threaded=THREADED, host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
