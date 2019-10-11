from flask import Flask, request
import logging

app = Flask(__name__)

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

    print(content)
    return content

if __name__ == "__main__":
    app.run()
