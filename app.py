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

@app.route("/dwnld_state", methods=["POST"])
def n3twatch_download_catcher():
    root_path = r"C:\Users\abish\Downloads\toscan"
    if "download_state" and "path" in request.json:
        print(root_path+ " "+ request.json["path"])
        if root_path in request.json["path"]:
            download_path = request.json["path"]
            print(f"Yeees, download complete at {download_path}")
        else:
            print("Noooooo, my plan has failed")
    return jsonify({}), 200




def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', PORT))
    app.run(debug=DEBUG, threaded=THREADED, host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
