from flask import Flask, request
import logging
import os

from werkzeug.contrib.fixers import ProxyFix

# Globals
MIN_BODY_PRINT_LENGTH = 6
body_print_length = os.getenv("BODY_PRINT_LENGTH")
if body_print_length:
    body_print_length = int(body_print_length)
if body_print_length < MIN_BODY_PRINT_LENGTH:
    print("Body print length cannot be less than {}, exiting...", MIN_BODY_PRINT_LENGTH)
    exit(1)
body_print_length_lhs = body_print_length // 2 if body_print_length else None
body_print_length_rhs = body_print_length - body_print_length_lhs if body_print_length else None

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def ping():
    return "I'm alive!"

@app.route("/<path:path>", methods=["GET", "POST", "PUT"])
def diag(path):
    # For now, we are expecting JSON all the time
    body_str = str(request.json)
    if body_print_length and len(body_str) > body_print_length:
        body_str_truncated = body_str[:body_print_length_lhs] + "..." + body_str[len(body_str)-body_print_length_rhs:]
    else:
        body_str_truncated = body_str

    content = """
Path: {} /{}
Headers: {}
Body:
{}
""".format(
    request.method, path,
    request.headers,
    body_str_truncated)

    app.logger.info("%s", content)
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
