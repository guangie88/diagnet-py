from flask import Flask, request
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/")
def ping():
    return "I'm alive!"

@app.route("/<path:path>", methods=["GET", "POST", "PUT"])
def diag(path):
    content = """
Path: {} {}
Content-Type: {}
Content-Length: {}

Body:
{}
""".format(
    request.method, path,
    request.content_type,
    request.content_length,
    request.data)

    app.logger.info("%s", content)
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
