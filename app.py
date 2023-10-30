from flask import Flask, jsonify, request, render_template, redirect
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

PORT = os.environ['PORT']
ROOT_PATH = os.environ['ROOT_PATH']
SAFE_PATH = os.environ['SAFE_PATH']
DEBUG = os.environ['DEBUG']
THREADED = os.environ['THREADED']
API_KEY = os.environ['API_KEY']
root_path = ROOT_PATH
safe_path = SAFE_PATH

@app.route('/')
def n3twatch_homepage():
    return render_template("splash_page.html", root_path = root_path, safe_path = safe_path)

@app.route("/path_updater", methods=["POST"])
def n3twatch_path_updater():
    global root_path, safe_path
    if request.form.get("submit")=="Submit":
        root_path = request.form.get("root_path")
        safe_path = request.form.get("safe_path")
    elif request.form.get("submit")=="Reset":
        root_path=ROOT_PATH
        safe_path=SAFE_PATH
    return redirect("/")

@app.route("/dwnld_state", methods=["POST"])
def n3twatch_download_catcher():
    if "download_state" and "path" in request.json:
        if root_path in request.json["path"]:
            headers = {"api-key": API_KEY,'accept': 'application/json',}
            data = {'scan_type': 'all',
                'no_share_third_party': '',
                'allow_community_access': '',
                'comment': '',
                'submit_name': '',
            }
            download_path = request.json["path"]
            print(f"Yeees, download complete at {download_path}")
            files = {
                'file': (download_path, open(download_path, 'rb')),  # Adjust the 'image/jpeg' to match your file type
            }
            response = requests.post(os.environ["API_FILE_UPLOAD_URL"], headers=headers, data=data, files=files).json()
            sha = response["sha256"]
            response = requests.get(os.environ["API_SUMMARY_URL"]+f"{sha}/summary", headers=headers).json()
            if response["threat_score"]:
                print("Kill it with fire")
                os.remove(download_path)
            else:
                print("All clear")
                filename = os.path.basename(download_path)
                os.rename(download_path, safe_path+filename)
        else:
            print("Noooooo, my plan has failed")
    return jsonify({}), 200




def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', PORT))
    app.run(debug=DEBUG, threaded=THREADED, host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
