from flask import Flask, jsonify, request, render_template, redirect

import requests
import os
import json

app = Flask(__name__)

DEBUG = True
THREADED = True
PORT = 8080
API_KEY = ""
ROOT_PATH = r"C:\Users\abish\Downloads\toscan"
root_path = ROOT_PATH

@app.route('/')
def n3twatch_homepage():
    return render_template("splash_page.html", path = root_path)

@app.route("/path_updater", methods=["POST"])
def n3twatch_path_updater():
    global root_path
    if request.form.get("submit")=="Submit":
        root_path = request.form.get("root_path")
    elif request.form.get("submit")=="Reset":
        root_path=ROOT_PATH
    return redirect("/")

@app.route("/dwnld_state", methods=["POST"])
def n3twatch_download_catcher():
    if "download_state" and "path" in request.json:
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
