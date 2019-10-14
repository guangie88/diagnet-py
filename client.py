import json
import requests
import os
import time

def main():
    url = os.environ["URL"]
    method = os.environ["METHOD"]
    content_length = int(os.environ["CONTENT_LENGTH"])
    sleep = int(os.environ["SLEEP"])
    verbose = bool(os.getenv("VERBOSE", "0"))

    # We assume to always send JSON array of string, so the min must be 4
    if content_length < 4:
        raise Exception("Content-Length must be more 4")

    if sleep < 1:
        raise Exception("Sleep seconds cannot be less than 1")

    CONTENT_TYPE = "application/json"
    payload = ["x" * (content_length - 4)]
    payload_json = json.dumps(payload)

    while True:
        r = requests.request(
            method,
            url,
            headers={"Content-Type": CONTENT_TYPE},
            data=payload_json)

        if verbose:
            print(r.text)

        time.sleep(sleep)

if __name__ == "__main__":
    main()
