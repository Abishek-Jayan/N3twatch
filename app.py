from flask import Flask

import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, threaded=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
