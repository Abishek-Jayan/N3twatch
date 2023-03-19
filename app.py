from flask import Flask

import os

app = Flask(__name__)
DEBUG = True
THREADED = True
PORT = 8080


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


def main() -> None:
    # Server start
    port = int(os.environ.get('PORT', PORT))
    app.run(debug=DEBUG, threaded=THREADED, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
