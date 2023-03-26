from flask import Flask, jsonify, request

import requests
import os
import json

app = Flask(__name__)

DEBUG = True
THREADED = True
PORT = 8080
API_KEY = ""


@app.route('/')
def n3twatch_homepage():
    return '<p>Hello, World!</p>', 200


@app.route("/dwn", methods=["POST"])
def n3twatch_download_catcher():
    if 'path' in request.json:
        if path := request.json['path']:
            print("New File Downloaded:", path)
            with open(path, 'rb') as file:
                headers = {
                    "accept": "application/json",
                    "x-apikey": API_KEY
                }
                scan_res = requests.post(
                    "https://www.virustotal.com/api/v3/files",
                    headers=headers,
                    files={
                        "file": (path, file)
                    })
                data_src = json.loads(scan_res.text)
                data_url = data_src["data"]["links"]["self"]
                result_res = requests.get(data_url, headers=headers)
                print(result_res.text)
    return jsonify({}), 200


def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', PORT))
    app.run(debug=DEBUG, threaded=THREADED, host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
